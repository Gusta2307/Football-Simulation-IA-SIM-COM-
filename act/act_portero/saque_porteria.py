import numpy
from act.act_jugador.pase import Pase
from config import Config

config = Config()

class Saque_porteria(Pase):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        self.__descripcion = f"El portero {self.agente.nombre} saca de porteria a "
        self.tipo = config.ACT_SAQUE_PORTERIA
        self.tiempo = 0.17
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return ((partido.ultima_accion.tipo == config.ACT_RECIBIR_BALON and partido.ultima_accion.estado == config.NO_RECIBE_BALON and partido.ultima_accion.sub_estado == config.LINEA_FINAL) or \
            (partido.ultima_accion.tipo == config.ACT_TIRO_PORTERIA and partido.ultima_accion.estado == config.POR_FUERA)) and \
                partido.ultima_accion.agente.equipo != self.agente.equipo

    def poscondicion(self, partido):
        partido.pos_balon = None
        partido.estado = config.EN_JUEGO
        partido.ultima_accion = self
        