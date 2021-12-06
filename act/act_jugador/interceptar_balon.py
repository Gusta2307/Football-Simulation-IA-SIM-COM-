import numpy
from act.accion import Accion
from act.act_jugador.hacer_falta import Hacer_Falta
from config import Config

config = Config()

class Interceptar_balon(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACT_INTERCEPTAR_BALON
        self.estado = None
        self.__descripcion = f"El jugador {self.agente.nombre} intercepto el balon "
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.ultima_accion.tipo == config.ACT_PASE and partido.ultima_accion.agente.equipo != self.agente.equipo and partido.estado != config.INICIAR_PARTIDO and not partido.ultima_accion.pase_inicial

    def ejecutar(self, partido):
        nivel = numpy.random.choice(numpy.arange(0, 4), p=[self.agente.no_falta, self.agente.falta_leve, self.agente.falta_moderada, self.agente.falta_grave])
        
        if nivel == 0: # si no cometio falta
            self.estado = config.SIN_FALTA
            self.poscondicion(partido)
            print(self.descripcion() + self.estado)
        else:
            self.estado = config.CON_FALTA
            act = Hacer_Falta(self.agente, nivel=nivel, descripcion=self.descripcion() + self.estado + " ")
            act.ejecutar(partido)

    def poscondicion(self, partido):
        partido.pos_balon = self.agente
        partido.ultima_accion = self
        