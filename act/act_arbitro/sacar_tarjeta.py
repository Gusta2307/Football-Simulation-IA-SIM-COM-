import numpy
from act.accion import Accion
from config import Config

config = Config()

class Sacar_tarjeta(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACT_SACAR_TARJETA
        self.estado = config.CANTA_FALTA
        self.falta_jugador = None
        self.sub_estado = None
        self.__descripcion = f"El arbitro {self.agente.nombre} "
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.ultima_accion.tipo == config.ACT_HACER_FALTA

    def ejecutar(self, partido):
        color = numpy.random.choice(numpy.arange(0, 2), p=[self.agente.sacar_tarjeta_amarilla, 1 - self.agente.sacar_tarjeta_amarilla])
        self.falta_jugador = partido.ultima_accion.agente
        #definir como hacer las probabilidades teniendo en cuenta el tipo de falta que se realizo
        if color:
            self.sub_estado = config.MUESTRA_ROJA
            print(self.descripcion() + self.estado + " y " + self.sub_estado)
        else:
            self.sub_estado = config.MUESTRA_AMARILLA
            if partido.ultima_accion.agente.cantidad_tarjetas == 1:
                print(self.descripcion() + self.estado + ' y le ' + self.sub_estado + " y " + config.MUESTRA_ROJA + f' a {partido.ultima_accion.agente.nombre}')
            else:
                print(self.descripcion() + self.estado + ' y le ' + self.sub_estado + f' a {partido.ultima_accion.agente.nombre}')
        self.poscondicion(partido)


    def poscondicion(self, partido):
        if self.sub_estado == config.MUESTRA_ROJA or partido.ultima_accion.agente.cantidad_tarjetas == 1:
            eq = partido.eq1 if partido.ultima_accion.agente.equipo == partido.eq1 else partido.eq2
            eq.jugadores.remove(partido.ultima_accion.agente)
            print(f"El jugador {partido.ultima_accion.agente.nombre} es expulsado del partido")
        elif self.sub_estado ==  config.MUESTRA_AMARILLA:
            partido.ultima_accion.agente.cantidad_tarjetas = 1

        partido.pos_balon = None
        partido.estado = config.DETENIDO
        partido.ultima_accion = self
