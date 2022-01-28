from act.act_jugador.pase import Pase
from config import Config

config = Config()

class Saque_esquina(Pase):
    def __init__(self, agente) -> None:
        super().__init__(agente)
        self.__descripcion = f"El jugador {self.agente.nombre} saca de esquina a "
        self.tipo = config.ACCIONES.JUGADOR.ACT_SAQUE_ESQUINA
        self.tiempo = 0.4
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return  partido.estado == config.PARTIDO.ESTADO.DETENIDO and \
                ((partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_ATAJAR and partido.ultima_accion.estado == config.ACCIONES.ESTADO.ATAJAR.REBOTE_LINEA_FINAL) or \
                (partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_DESPEJAR_BALON and partido.ultima_accion.estado == config.ACCIONES.ESTADO.DESPEJAR_BALON.DESPEJE_LINEA_FINAL)) and \
                partido.ultima_accion.agente.equipo != self.agente.equipo
       
    def poscondicion(self, partido):
        # self.agente.equipo.estadisticas['TIROS DE ESQUINA'] += 1
        partido.reporte.annadir_tiro_esquina(self.agente.equipo.nombre)
        partido.pos_balon = None
        partido.estado = config.PARTIDO.ESTADO.EN_JUEGO
        partido.ultima_accion = self
        