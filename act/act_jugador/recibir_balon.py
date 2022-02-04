import numpy
from act.accion import Accion
from config import Config

config = Config()

class Recibir_balon(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.__descripcion = f"El jugador {self.agente.nombre} "
        self.tipo = config.ACCIONES.JUGADOR.ACT_RECIBIR_BALON
        self.estado = None
        self.tiempo = 0.05
        self.sub_estado = None
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return ((partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_PASE or partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_SAQUE_PORTERIA  or\
                partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_SAQUE_BANDA or partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_SAQUE_FALTA) and \
                partido.ultima_accion.dest_jugador == self.agente)  or \
                partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_ATAJAR and partido.ultima_accion.estado == config.ACCIONES.ESTADO.ATAJAR.REBOTE_JUGADOR or \
                partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_DESPEJAR_BALON and partido.ultima_accion.estado == config.ACCIONES.ESTADO.DESPEJAR_BALON.DESPEJE_JUGADOR
                

    def ejecutar(self, partido):
        recibir_balon = numpy.random.choice(numpy.arange(0, 2), p=[self.agente.recibir_balon, 1 - self.agente.recibir_balon])
        if recibir_balon:
            self.estado = config.ACCIONES.ESTADO.RECIBIR_BALON.RECIBIR_BALON
            # print(f'{partido.obtener_tiempo()} {self.descripcion()}  {self.estado}')
        else:
            self.estado = config.ACCIONES.ESTADO.RECIBIR_BALON.NO_RECIBE_BALON
            if partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_PASE:
                #aqui el balon se fue de largo y vendria un saque de banda o saque de porteria
                saque = numpy.random.choice(numpy.arange(0, 2), p=[0.2, 0.8])
                self.sub_estado = config.ACCIONES.ESTADO.RECIBIR_BALON.BANDA if saque else config.ACCIONES.ESTADO.RECIBIR_BALON.LINEA_FINAL
                partido.reporte.annadir_a_resumen(f'{partido.obtener_tiempo()} {self.descripcion()} {self.estado} {self.sub_estado}', partido.pt)

        self.poscondicion(partido)


    def poscondicion(self, partido):
        if self.estado == config.ACCIONES.ESTADO.RECIBIR_BALON.RECIBIR_BALON:
            # self.agente.equipo.estadisticas['PASES'] += 1
            partido.reporte.annadir_pase(self.agente.equipo.nombre, partido.pt)
            partido.pos_balon = self.agente
            partido.ultima_accion = self
        else:
            if partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_PASE:
                # self.agente.equipo.estadisticas['BALONES PERDIDOS'] += 1
                partido.reporte.annadir_balon_perdido(self.agente.equipo.nombre, partido.pt)
                partido.estado = config.PARTIDO.ESTADO.DETENIDO
                partido.pos_balon = None
                partido.ultima_accion = self
        