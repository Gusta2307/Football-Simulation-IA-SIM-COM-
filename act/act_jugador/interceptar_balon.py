import numpy
from act.accion import Accion
from act.act_jugador.hacer_falta import Hacer_Falta
from config import Config

config = Config()

class Interceptar_balon(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACCIONES.JUGADOR.ACT_INTERCEPTAR_BALON
        self.estado = None
        self.tiempo = 0.1
        self.__descripcion = f"El jugador {self.agente.nombre} intercepto el balon "
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_PASE and partido.ultima_accion.agente.equipo != self.agente.equipo and partido.estado != config.PARTIDO.ESTADO.INICIAR_PARTIDO and not partido.ultima_accion.pase_inicial

    def ejecutar(self, partido):
        nivel = numpy.random.choice(numpy.arange(0, 4), p=[self.agente.no_falta, self.agente.falta_leve, self.agente.falta_moderada, self.agente.falta_grave])
        
        if nivel == 0: # si no cometio falta
            self.estado = config.ACCIONES.ESTADO.INTERCEPCION.SIN_FALTA
            self.poscondicion(partido)
            print(f'{partido.obtener_tiempo()} {self.descripcion()} {self.estado}')
        else:
            self.estado = config.ACCIONES.ESTADO.INTERCEPCION.CON_FALTA
            act = Hacer_Falta(self.agente, nivel=nivel, descripcion=self.descripcion() + self.estado + " ")
            act.ejecutar(partido)

    def poscondicion(self, partido):
        # self.agente.equipo.estadisticas['BALONES RECUPERADOS'] += 1
        partido.reporte.annadir_balon_recuperado(self.agente.equipo.nombre)
        # partido.ultima_accion.agente.equipo.estadisticas['BALONES PERDIDOS'] += 1
        partido.reporte.annadir_balon_perdido(partido.ultima_accion.agente.equipo.nombre)
        partido.pos_balon = self.agente
        partido.ultima_accion = self
        