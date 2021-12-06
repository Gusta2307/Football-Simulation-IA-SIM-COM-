import numpy
from act.accion import Accion
from config import Config

config = Config()

class Hacer_Falta(Accion):
    def __init__(self, agente, **args) -> None:
        self.agente = agente
        self.tipo = config.ACT_HACER_FALTA
        self.args = args
        self.nivel = None
        self.__descripcion = f"El jugador {self.agente.nombre} realizo una falta "
        if self.args != {}:
            self.nivel = self.args['nivel']
            self.__descripcion = self.args['descripcion']

    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.ultima_accion.tipo != config.ACT_HACER_FALTA

    def ejecutar(self, partido):
        if self.nivel == None:
            self.nivel = 0
            while self.nivel == 0:
                self.nivel = numpy.random.choice(numpy.arange(0, 4), p=[self.agente.no_falta, self.agente.falta_leve, self.agente.falta_moderada, self.agente.falta_grave])
        else:
            partido.pos_balon = self.agente


        print(self.descripcion() + config.SEL_NIVEL[self.nivel])
        self.poscondicion(partido)

    def poscondicion(self, partido):
        partido.ultima_accion = self
        # partido.pos_balon = self.agente
        # partido.estado = config.DETENIDO 
        self.nivel = None
        