from act.act_jugador.pase import Pase
from config import Config

config = Config()

class Saque_esquina(Pase):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        self.__descripcion = f"El jugador {self.agente.nombre} saca de esquina a "
        self.tipo = config.ACT_SAQUE_ESQUINA
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return  partido.estado == config.DETENIDO and \
                ((partido.ultima_accion.tipo == config.ACT_ATAJAR and partido.ultima_accion.estado == config.REBOTE_LINEA_FINAL) or \
                (partido.ultima_accion.tipo == config.ACT_DESPEJAR_BALON and partido.ultima_accion.estado == config.DESPEJE_LINEA_FINAL)) and \
                partido.ultima_accion.agente.equipo != self.agente.equipo
       
    def poscondicion(self, partido):
        partido.pos_balon = None
        partido.estado = config.EN_JUEGO
        partido.ultima_accion = self
        