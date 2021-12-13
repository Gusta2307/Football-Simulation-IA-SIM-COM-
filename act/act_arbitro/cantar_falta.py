import numpy
from act.accion import Accion
from act.act_jugador.hacer_falta import Hacer_Falta
from classes.partido import Partido
from config import Config

config = Config()

class Cantar_falta(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACT_CANTAR_FALTA
        self.tiempo = None
        self.estado = None
        self.falta_jugador = None
        self.__descripcion = f"El arbitro {self.agente.nombre} "
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.ultima_accion.tipo == config.ACT_HACER_FALTA
        config.act
    def ejecutar(self, partido):
        canta = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.cantar_falta, self.agente.cantar_falta])
        
        if not canta: # si no canta falta
            self.estado = config.NO_CANTA_FALTA
            print(f'{partido.obtener_tiempo()} {self.descripcion()} {self.estado}')
            self.tiempo = 0.04
        else:
            self.estado = config.CANTA_FALTA
            self.tiempo = 0.4
            self.falta_jugador = partido.ultima_accion.agente
            tarjeta = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.sacar_tarjeta, self.agente.sacar_tarjeta])
            if tarjeta: #decide mostrar tarjeta
                return self.agente.acciones['SACAR_TARJETA'][0].ejecutar(partido)
            print(f'{partido.obtener_tiempo()} {self.descripcion()} {self.estado}')

        self.poscondicion(partido)

    def poscondicion(self, partido):
        if self.estado == config.NO_CANTA_FALTA:
           partido.estado = config.EN_JUEGO
        elif self.estado == config.CANTA_FALTA:
            partido.ultima_accion.agente.equipo.estadisticas['FALTAS'] += 1
            partido.estado = config.DETENIDO
            partido.pos_balon = None
            partido.ultima_accion = self


    def __str__(self) -> str:
        return f'{self.tipo} -> {self.estado}'
