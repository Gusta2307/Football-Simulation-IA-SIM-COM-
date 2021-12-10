from act.act_jugador.pase import Pase
from config import Config
config = Config()

class Saque_falta(Pase):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACT_SAQUE_FALTA
        self.estado = None
        self.tiempo = 0.7
        self.__descripcion = f"El jugador {self.agente.nombre} saca falta "
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return (partido.ultima_accion.tipo == config.ACT_CANTAR_FALTA or partido.ultima_accion.tipo == config.ACT_SACAR_TARJETA) and partido.ultima_accion.estado == config.CANTA_FALTA and partido.estado == config.DETENIDO and partido.ultima_accion.falta_jugador.equipo != self.agente.equipo

    def poscondicion(self, partido):
        partido.estado = config.EN_JUEGO
        partido.pos_balon = None
        partido.ultima_accion = self
