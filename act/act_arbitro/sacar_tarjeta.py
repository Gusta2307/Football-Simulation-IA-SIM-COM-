import numpy
from act.accion import Accion
from config import Config

from colorama import Fore
from colorama import Style

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
            print(f"{partido.obtener_tiempo()} {self.descripcion()} {Fore.RED} {self.estado} {Style.RESET_ALL} y {self.sub_estado}")
        else:
            self.sub_estado = config.MUESTRA_AMARILLA
            if partido.ultima_accion.agente.cantidad_tarjetas == 1:
                print(f'{partido.obtener_tiempo()} {self.descripcion()} {Fore.YELLOW} {self.estado} {Style.RESET_ALL} y le {self.sub_estado} y {config.MUESTRA_ROJA} a {partido.ultima_accion.agente.nombre}')
            else:
                print(f'{partido.obtener_tiempo()} {self.descripcion()} {Fore.YELLOW} {self.estado} {Style.RESET_ALL} y le {self.sub_estado} a {partido.ultima_accion.agente.nombre}')
        self.poscondicion(partido)


    def poscondicion(self, partido):
        if self.sub_estado == config.MUESTRA_ROJA or partido.ultima_accion.agente.cantidad_tarjetas == 1:
            eq = partido.eq1 if partido.ultima_accion.agente.equipo == partido.eq1 else partido.eq2
            eq.jugadores_en_campo.remove(partido.ultima_accion.agente)
            # partido.ultima_accion.agente.equipo.estadisticas['TARJETAS ROJAS'] += 1
            partido.reporte.annadir_tarjeta_roja(partido.ultima_accion.agente.equipo.nombre)
            print(f"El jugador {partido.ultima_accion.agente.nombre} es expulsado del partido")
        elif self.sub_estado ==  config.MUESTRA_AMARILLA:
            partido.ultima_accion.agente.cantidad_tarjetas = 1
            # partido.ultima_accion.agente.equipo.estadisticas['TARJETAS AMARILLAS'] += 1
            partido.reporte.annadir_tarjeta_amarilla(partido.ultima_accion.agente.equipo.nombre)

        partido.pos_balon = None
        partido.estado = config.DETENIDO
        partido.ultima_accion = self
