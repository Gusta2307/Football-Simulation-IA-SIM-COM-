import numpy
from act.accion import Accion
from config import Config
from colorama import Fore
from colorama import Style

config = Config()

class Despejar_balon(Accion):
    def __init__(self, agente, **args) -> None:
        self.agente = agente
        self.tipo = config.ACT_DESPEJAR_BALON
        self.estado = None
        self.__descripcion = f"El jugador {self.agente.nombre} "

    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return partido.ultima_accion.tipo == config.ACT_SAQUE_ESQUINA and partido.ultima_accion.agente.equipo != self.agente.equipo

    def ejecutar(self, partido):
        # CREO QUE NO SE DEBERIA PONER PROBABILIDADES DE DESPEJE A LOS JUGADORES
        # EL DESPEJE ES UNA ACCION QUE PUEDE SALIR PARA DONDE SEA LITERALMENTE

        # BANDA, SAQUE DE ESQUINA, BALON SUELTO
        despeje = numpy.random.choice(numpy.arange(0, 3), p=[0.35, 0.3, 0.35])

        if despeje:
            self.estado = config.DESPEJE_LINEA_FINAL
        elif not despeje:
            self.estado = config.DESPEJE_BANDA
        else:
            self.estado = config.DESPEJE_JUGADOR

        print(f'{self.descripcion()}{Fore.GREEN}{self.estado}{Style.RESET_ALL}')

        self.poscondicion(partido)

    def poscondicion(self, partido):
        partido.ultima_accion = self
        partido.pos_balon = None
        if self.estado == config.DESPEJE_LINEA_FINAL or self.estado == config.DESPEJE_BANDA:
            partido.estado = config.DETENIDO 
        