from act.act_jugador.pase import Pase
from config import Config

config = Config()

class Saque_banda(Pase):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        self.__descripcion = f"El jugador {self.agente.nombre} saca de banda a "
        self.tipo = config.ACCIONES.JUGADOR.ACT_SAQUE_BANDA
        self.tiempo = 0.2
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return  partido.estado == config.PARTIDO.ESTADO.DETENIDO and \
                ((partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_RECIBIR_BALON and partido.ultima_accion.estado == config.ACCIONES.ESTADO.RECIBIR_BALON.NO_RECIBE_BALON and partido.ultima_accion.sub_estado == config.ACCIONES.ESTADO.RECIBIR_BALON.BANDA) or \
                (partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_DESPEJAR_BALON and partido.ultima_accion.estado == config.ACCIONES.ESTADO.DESPEJAR_BALON.DESPEJE_BANDA)) and \
                self.agente.equipo != partido.ultima_accion.agente.equipo

    def poscondicion(self, partido):
        partido.pos_balon = None
        partido.estado = config.PARTIDO.ESTADO.EN_JUEGO
        partido.ultima_accion = self
        