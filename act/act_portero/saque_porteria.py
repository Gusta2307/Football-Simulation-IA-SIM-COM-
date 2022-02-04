import numpy
from act.act_jugador.pase import Pase
from config import Config

config = Config()

class Saque_porteria(Pase):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        self.__descripcion = f"El portero {self.agente.nombre} saca de porteria a "
        self.tipo = config.ACCIONES.JUGADOR.ACT_SAQUE_PORTERIA
        self.tiempo = 0.17
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return ((partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_RECIBIR_BALON and partido.ultima_accion.estado == config.ACCIONES.ESTADO.RECIBIR_BALON.NO_RECIBE_BALON and partido.ultima_accion.sub_estado == config.ACCIONES.ESTADO.RECIBIR_BALON.LINEA_FINAL) or \
            (partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_TIRO_PORTERIA and partido.ultima_accion.estado == config.ACCIONES.ESTADO.TIRO_PORTERIA.POR_FUERA)) and \
                partido.ultima_accion.agente.equipo != self.agente.equipo

    def poscondicion(self, partido):
        partido.pos_balon = None
        partido.estado = config.PARTIDO.ESTADO.EN_JUEGO
        partido.ultima_accion = self
        