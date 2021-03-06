from act.accion import Accion
from config import Config

config = Config()

class Pase(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tiempo = 0.1
        self.__descripcion = f"El jugador {self.agente.nombre} le pasa al balon a "
        self.dest_jugador = None #Jugador que va a recibir el pase
        self.tipo = config.ACCIONES.JUGADOR.ACT_PASE 
        self.pase_inicial = False
 
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return self.agente == partido.pos_balon and partido.estado != config.PARTIDO.ESTADO.DETENIDO if not (partido.pos_balon is None) else False

    def ejecutar(self, partido):
        self.dest_jugador = self.agente.seleccionar_jugador_pase(partido)
        if self.dest_jugador != None:
            self.poscondicion(partido)
            partido.reporte.annadir_a_resumen(f'{partido.obtener_tiempo()} {self.descripcion()} {self.dest_jugador.nombre}', partido.pt)

    def poscondicion(self, partido):
        if partido.estado == config.PARTIDO.ESTADO.INICIAR_PARTIDO or partido.estado == config.PARTIDO.ESTADO.REANUDAR_PARTIDO:
            partido.estado = config.PARTIDO.ESTADO.EN_JUEGO
            partido.pos_balon = self.dest_jugador
            self.pase_inicial = True
        else:
            partido.pos_balon = None
            self.pase_inicial = False
        partido.ultima_accion = self
        