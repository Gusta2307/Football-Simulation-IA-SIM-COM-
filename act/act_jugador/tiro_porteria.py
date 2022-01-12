import numpy
from act.accion import Accion
from config import Config
config = Config()

class Tiro_Porteria (Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.estado = None
        self.tiempo = 0.15
        self.tipo = config.ACT_TIRO_PORTERIA
        self.__descripcion = f"El jugador {self.agente.nombre} tira "

    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return self.agente == partido.pos_balon if not (partido.pos_balon is None) else \
                partido.ultima_accion.tipo == config.ACT_SAQUE_ESQUINA and partido.ultima_accion.agente.equipo == self.agente.equipo and \
                partido.ultima_accion.agente != self.agente #esta condicion se podria dar pero es muy pocoooooo probable

    def ejecutar(self, partido):
        tiro = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.tiro_porteria , self.agente.tiro_porteria])
        
        self.estado = config.A_PORTERIA if tiro else config.POR_FUERA

        self.poscondicion(partido)
        
        print(f'{partido.obtener_tiempo()} {self.descripcion()} {self.estado}')

    def poscondicion(self, partido):
        # self.agente.equipo.estadisticas['REMATES'] += 1
        partido.reporte.annadir_remate(self.agente.equipo.nombre)
        partido.pos_balon = None
        partido.ultima_accion = self
        if self.estado == config.POR_FUERA:
            partido.estado = config.DETENIDO


