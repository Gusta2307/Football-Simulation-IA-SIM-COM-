from act.accion import Accion
from config import Config
config = Config()

class Default(Accion):
    def __init__(self, agente) -> None:
        self.agente = agente
        self.tipo = config.ACCIONES.JUGADOR.ACT_DEFAULT
    
    def descripcion(selfq):
        return ""
        #return f"{self.agente.nombre} no hace nada"
        
    def precondicion(self, partido) -> bool:
        return True

    def ejecutar(self, partido):
        return

    def poscondicion(self, partido):
        return