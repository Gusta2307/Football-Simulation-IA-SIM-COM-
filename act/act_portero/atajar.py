import numpy
from act.accion import Accion
from config import Config

config = Config()

class Atajar(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.__descripcion = f"El portero {self.agente.nombre} "
        self.estado = None
        self.tipo = config.ACT_ATAJAR
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        if partido.ultima_accion.tipo == config.ACT_TIRO_PORTERIA:
            return partido.ultima_accion.estado == config.A_PORTERIA and partido.ultima_accion.agente.equipo != self.agente.equipo  
        return False

    def ejecutar(self, partido):
        atajar = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.atajar_balon , self.agente.atajar_balon])

        if atajar:
            rebote = numpy.random.choice(numpy.arange(0, 4), p=[self.agente.sin_rebote, self.agente.rebote_banda, self.agente.rebote_linea_final, self.agente.rebote_jugador])
            if rebote == 0:
                self.estado = config.SIN_REBOTE
            elif rebote == 1:
                self.estado = config.REBOTE_BANDA
            elif rebote == 2:
                self.estado = config.REBOTE_LINEA_FINAL
            elif rebote == 3:
                self.estado = config.REBOTE_JUGADOR
            self.poscondicion(partido, atajar, rebote)

            print(self.descripcion() + self.estado)
        else:
            print(f"El jugador {partido.ultima_accion.agente} marco GOOOOOL")
            self.estado = config.NO_ATAJO
            self.poscondicion(partido, atajar, -1)


    def poscondicion(self, partido, atajar, rebote):
        if atajar:
            if rebote == 0:
                partido.pos_balon = self.agente
            elif rebote == 1 or rebote == 2:
                partido.estado = config.DETENIDO
            elif rebote == 3:
                partido.pos_balon = None
            partido.ultima_accion = self    
        else:
            partido.pos_balon = None
            partido.estado = config.REANUDAR_PARTIDO
        