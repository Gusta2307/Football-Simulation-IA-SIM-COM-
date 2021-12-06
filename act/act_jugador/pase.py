from act.accion import Accion
from config import Config

config = Config()

class Pase(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.__descripcion = f"El jugador {self.agente.nombre} le pasa al balon a "
        self.dest_jugador = None #Jugador que va a recibir el pase
        self.tipo = config.ACT_PASE 
        self.pase_inicial = False
 
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return self.agente == partido.pos_balon if not (partido.pos_balon is None) else False

    def ejecutar(self, partido):
        self.dest_jugador = self.agente.seleccionar_jugador_pase(partido)
        self.poscondicion(partido)
        print(self.descripcion() + self.dest_jugador.nombre)

    def poscondicion(self, partido):
        if partido.estado == config.INICIAR_PARTIDO or partido.estado == config.REANUDAR_PARTIDO:
            partido.estado = config.EN_JUEGO
            partido.pos_balon = self.dest_jugador
            self.pase_inicial = True
        else:
            partido.pos_balon = None
            self.pase_inicial = False
        partido.ultima_accion = self
        