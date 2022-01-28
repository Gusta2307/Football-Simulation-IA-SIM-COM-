import numpy
from config import Config

config = Config()

class Retroceder_Posicion:
    def __init__(self, agente) -> None:
        self.agente = agente
        self.__descripcion = f"El jugador {self.agente.nombre} retrocede su ubicación en el campo "
        self.tipo = config.ACCIONES.JUGADOR.ACT_RETROCEDER_POSICION
        self.tiempo = 0
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return  self.agente.ubicacion_campo != config.ZONA.DEFENSA

    def ejecutar(self, partido):
        avanzar = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.avanzar_posicion , self.agente.avanzar_posicion])
        if avanzar:
            # print(self.descripcion())
            self.poscondicion(partido)

    def poscondicion(self, partido):
        self.agente.ubicacion_campo = config.ZONA.ANTERIOR_ZONA[self.agente.ubicacion_campo]
        