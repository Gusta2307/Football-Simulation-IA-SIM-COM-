import numpy
from config import Config

config = Config()

class Avanzar_Posicion:
    def __init__(self, agente) -> None:
        self.agente = agente
        self.__descripcion = f"El jugador {self.agente.nombre} avanza su ubicación en el campo "
        self.tipo = config.ACCIONES.JUGADOR.ACT_AVANZAR_POSICION
        self.tiempo = 0
    
    def descripcion(self):
        return self.__descripcion
        
    def precondicion(self, partido) -> bool:
        return  self.agente.ubicacion_campo != config.ZONA.ATAQUE 

    def ejecutar(self, partido):
        avanzar = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.agente.avanzar_posicion , self.agente.avanzar_posicion])
        if avanzar:
            self.poscondicion(partido)
            partido.reporte.annadir_a_resumen(f'{partido.obtener_tiempo()} {self.descripcion()}', partido.pt)
    


    def poscondicion(self, partido):
        self.agente.ubicacion_campo = config.ZONA.SIGUIENTE_ZONA[self.agente.ubicacion_campo]
        