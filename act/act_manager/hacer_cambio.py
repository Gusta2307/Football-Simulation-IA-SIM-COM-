import random
import numpy
from act.accion import Accion
from config import Config
from utiles import clasificar_jugadores

from colorama import Fore
from colorama import Style

config = Config()

class Hacer_cambio(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACT_HACER_CAMBIOS
        self.cambio = [] # Lista de tuplas (Jugador que entra, Jugador que sale)
        self.__descripcion = f"El manager {self.agente.nombre} del equipo "
        self.tiempo = 0

    
    def descripcion(self):
        return self.__descripcion
    
    def precondicion(self, partido) -> bool:
        return partido.cambios_por_equipo[self.agente.equipo.nombre][0] != 0 and partido.cambios_por_equipo[self.agente.equipo.nombre][1] != 0 and len(partido.cambios_pendiente[self.agente.equipo.nombre]) == 0

    def ejecutar(self, partido):
        total_cambios_posibles = partido.cambios_por_equipo[self.agente.equipo.nombre][1]
        cambios_ha_realizar = random.randint(1, total_cambios_posibles)
        for i in range(cambios_ha_realizar):
            if len(self.agente.equipo.jugadores_en_banca):
                j1 = self.agente.equipo.jugadores_en_banca[random.randint(0, len(self.agente.equipo.jugadores_en_banca) - 1)]
                jugadores_posibles = clasificar_jugadores(self.agente.equipo.jugadores_en_campo)[j1.posicion]
                j2 = jugadores_posibles[random.randint(0, len(jugadores_posibles) - 1)]
                self.cambio.append((j1,j2))
                partido.cambios_pendiente[self.agente.equipo.nombre].append(self)
                self.tiempo += 0.8
            else:
                break


    def poscondicion(self, partido, opt):
        banca = self.agente.equipo.jugadores_en_banca
        campo = self.agente.equipo.jugadores_en_campo
        print(f"El {self.agente.equipo.nombre} va ha realizar cambios")
        for j1, j2 in self.cambio:
            banca.remove(j1)
            campo.remove(j2)
            campo.append(j1)
            if not opt: 
                partido.op._optimizar_agente(j1)
            print(f"ENTRA: {Fore.GREEN}{j1.nombre}{Style.RESET_ALL} SALE: {Fore.RED}{j2.nombre}{Style.RESET_ALL}")

        self.agente.equipo.jugadores_en_banca = banca
        self.agente.equipo.jugadores_en_campo = campo

        tupla = partido.cambios_por_equipo[self.agente.equipo.nombre]
        partido.cambios_por_equipo[self.agente.equipo.nombre] = (tupla[0] - 1, tupla[1] - 1)


    def __str__(self) -> str:
        return f'{self.tipo} -> {self.estado}'
