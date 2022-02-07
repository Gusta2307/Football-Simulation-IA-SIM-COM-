import numpy
from act.accion import Accion
from config import Config

config = Config()

class Cantar_falta(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACCIONES.ARBITRO.ACT_CANTAR_FALTA
        self.tiempo = None
        self.estado = None
        self.falta_jugador = None
        self.__descripcion = f"El arbitro {self.agente.nombre} "
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_HACER_FALTA
        
    def ejecutar(self, partido):
        canta = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.cantar_falta, self.agente.cantar_falta])
        
        if not canta: # si no canta falta
            self.estado = config.ACCIONES.ESTADO.ARBITRO.NO_CANTA_FALTA
            partido.reporte.annadir_a_resumen(f'{partido.obtener_tiempo()} {self.descripcion()} {self.estado}', partido.pt)
            self.tiempo = 0.04
        else:
            self.estado = config.ACCIONES.ESTADO.ARBITRO.CANTA_FALTA
            self.tiempo = 0.4
            self.falta_jugador = partido.ultima_accion.agente
            tarjeta = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.sacar_tarjeta, self.agente.sacar_tarjeta])
            if tarjeta: #decide mostrar tarjeta
                return self.agente.acciones['SACAR_TARJETA'][0].ejecutar(partido)
            partido.reporte.annadir_a_resumen(f'{partido.obtener_tiempo()} {self.descripcion()} {self.estado}', partido.pt)

        self.poscondicion(partido)

    def poscondicion(self, partido):
        if self.estado == config.ACCIONES.ESTADO.ARBITRO.NO_CANTA_FALTA:
           partido.estado = config.PARTIDO.ESTADO.EN_JUEGO
        elif self.estado == config.ACCIONES.ESTADO.ARBITRO.CANTA_FALTA:
            partido.reporte.annadir_falta(partido.ultima_accion.agente.equipo.nombre, partido.pt)
            partido.ultima_accion.agente.reporte.annadir_falta()
            partido.estado = config.PARTIDO.ESTADO.DETENIDO
            partido.pos_balon = None
            partido.ultima_accion = self


    def __str__(self) -> str:
        return f'{self.tipo} -> {self.estado}'
