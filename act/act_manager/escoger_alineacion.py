import random
import numpy
from act.accion import Accion
from utiles import clasificar_jugadores, print_alineacion
from config import Config

config = Config()

class Escoger_alineacion(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACCIONES.MANAGER.ACT_ESCOGER_ALINEACION
        self.__descripcion = f"El manage {self.agente.nombre} ha elegido la alineacion para el partido "
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.estado == config.PARTIDO.ESTADO.INICIAR_PARTIDO


    def ejecutar(self, partido):
        # CUANDO SE ANNADAN MAS JUGADORES AL EQUIPO QUISIERA QUE EL MANAGER
        # ESCOJA ENTRE VARIOS ESQUEMAS DE JUEGO DIFERENTES ES DECIR [3, 3, 4, 1] [2, 4, 4, 1], [1, 4, 5, 1].... ETC
        # escoger_esquema = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.tiro_porteria , self.agente.tiro_porteria])
        escoger_esquema = config.ACCIONES.MANAGER.ESQUEMA_DE_JUEGO[0].copy()
        posicion_jugadores = clasificar_jugadores(self.agente.equipo.jugadores)

        # SELECCIONAR JUGADORES EN CAMPO
        jugadores_campo = []
        for i in range(len(config.POSICIONES.POS)):
            cant = escoger_esquema[i]
            while cant > 0:
                j = random.randint(0, len(posicion_jugadores[config.POSICIONES.POS[i]]) - 1)
                jugadores_campo.append(posicion_jugadores[config.POSICIONES.POS[i]].pop(j))
                cant -= 1
        self.agente.equipo.jugadores_en_campo = jugadores_campo

        
        jugadores_banca = []
        posibles_jugadores_banca = []
        for l in posicion_jugadores.values():
            posibles_jugadores_banca += l

        for i in range(config.PARTIDO.CONFIG.CANT_JUGADORES_BANCA):
            j = random.randint(0, len(posibles_jugadores_banca) - 1)
            jugadores_banca.append(posibles_jugadores_banca.pop(j))
            if not len(posibles_jugadores_banca):
                break
        self.agente.equipo.jugadores_en_banca = jugadores_banca
        
        # print(self.descripcion())

        # print_alineacion(escoger_esquema, jugadores_campo)

        # self.poscondicion(partido)

    def poscondicion(self, partido):
        # CUAL SERIA LA POSCONDICION DE ESTA ACCION?? :/
        pass


    def __str__(self) -> str:
        return f'{self.tipo} -> {self.estado}'
