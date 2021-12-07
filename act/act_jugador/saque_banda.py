from act.act_jugador.pase import Pase
from config import Config

config = Config()

class Saque_banda(Pase):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        self.__descripcion = f"El jugador {self.agente.nombre} saca de banda a "
        self.tipo = config.ACT_SAQUE_BANDA
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return  partido.estado == config.DETENIDO and \
                ((partido.ultima_accion.tipo == config.ACT_RECIBIR_BALON and partido.ultima_accion.estado == config.NO_RECIBE_BALON and partido.ultima_accion.sub_estado == config.BANDA) or \
                (partido.ultima_accion.tipo == config.ACT_DESPEJAR_BALON and partido.ultima_accion.estado == config.DESPEJE_BANDA)) and \
                self.agente.equipo != partido.ultima_accion.agente.equipo

    def poscondicion(self, partido):
        partido.pos_balon = None
        partido.estado = config.EN_JUEGO
        partido.ultima_accion = self
        