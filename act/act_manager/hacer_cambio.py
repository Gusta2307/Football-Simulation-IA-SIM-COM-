import random
import numpy
from act.accion import Accion
from config import Config
from utiles import clasificar_jugadores
from IA.range import Range
from classes.reporte import Reporte_Jugador
from colorama import Fore, Style

config = Config()

class Hacer_cambio(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACCIONES.MANAGER.ACT_HACER_CAMBIOS
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
                # print(j1.posicion)
                jugadores_posibles = clasificar_jugadores(self.agente.equipo.jugadores_en_campo)[j1.posicion]
                if jugadores_posibles:
                    j2 = jugadores_posibles[random.randint(0, len(jugadores_posibles) - 1)]
                if len(list(filter(lambda x: j1 in x or j2 in x, self.cambio))) or len(list(filter(lambda x: j1 in x or j2 in x,partido.cambios_pendiente[self.agente.equipo.nombre]))):
                    continue
                self.cambio.append((j1,j2))
                partido.cambios_pendiente[self.agente.equipo.nombre].append(self)
                self.tiempo += 0.8
            else:
                break


    def poscondicion(self, partido, opt):
        banca = self.agente.equipo.jugadores_en_banca
        campo = self.agente.equipo.jugadores_en_campo
        partido.reporte.annadir_a_resumen(f"El {self.agente.equipo.nombre} va ha realizar cambios", partido.pt)
        for j1, j2 in self.cambio:
            try:
                banca.remove(j1)
                campo.remove(j2)
                campo.append(j1)
            except:
                continue

            # if not opt: 
            #     partido.op._optimizar_agente(j1)
            # elif j1.estrategia is not None:
            #     for v in j1.estrategia.variables.keys():
            #         if isinstance(j1.estrategia.variables[v], Range):
            #             j1.estrategia.variables[v] = j1.estrategia.variables[v].get_value()
            partido.reporte.annadir_a_resumen(f"ENTRA: {Fore.GREEN}{j1.nombre}{Style.RESET_ALL} SALE: {Fore.RED}{j2.nombre}{Style.RESET_ALL}", partido.pt)

        self.agente.equipo.jugadores_en_banca = banca
        self.agente.equipo.jugadores_en_campo = campo

        tupla = partido.cambios_por_equipo[self.agente.equipo.nombre]
        partido.cambios_por_equipo[self.agente.equipo.nombre] = (tupla[0] - 1, tupla[1] - 1)


    def __str__(self) -> str:
        return f'{self.tipo} -> {self.estado}'
