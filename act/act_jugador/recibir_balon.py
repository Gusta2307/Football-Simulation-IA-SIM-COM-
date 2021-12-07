import numpy
from act.accion import Accion
from config import Config

config = Config()

class Recibir_balon(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.__descripcion = f"El jugador {self.agente.nombre} "
        self.tipo = config.ACT_RECIBIR_BALON
        self.estado = None
        self.sub_estado = None
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return ((partido.ultima_accion.tipo == config.ACT_PASE or partido.ultima_accion.tipo == config.ACT_SAQUE_PORTERIA  or partido.ultima_accion.tipo == config.ACT_SAQUE_BANDA) and partido.ultima_accion.dest_jugador == self.agente)  or \
                (partido.ultima_accion.tipo == config.ACT_ATAJAR and partido.ultima_accion.estado == config.REBOTE_JUGADOR)
                

    def ejecutar(self, partido):
        recibir_balon = numpy.random.choice(numpy.arange(0, 2), p=[self.agente.recibir_balon, 1 - self.agente.recibir_balon])
        if recibir_balon:
            self.estado = config.RECIBIR_BALON
            print(self.descripcion() + self.estado)
        else:
            self.estado = config.NO_RECIBE_BALON
            if partido.ultima_accion.tipo == config.ACT_PASE:
                #aqui el balon se fue de largo y vendria un saque de banda o saque de porteria
                saque = numpy.random.choice(numpy.arange(0, 2), p=[0.2, 0.8])
                self.sub_estado = config.BANDA if saque else config.LINEA_FINAL
                print(self.descripcion() + self.estado +' '+ self.sub_estado)

        self.poscondicion(partido)


    def poscondicion(self, partido):
        if self.estado == config.RECIBIR_BALON:
            partido.pos_balon = self.agente
            partido.ultima_accion = self
        else:
            if partido.ultima_accion.tipo == config.ACT_PASE:
                partido.estado = config.DETENIDO
                partido.pos_balon = None
                partido.ultima_accion = self
        