import abc
from classes.partido import Partido

class Agente(abc.ABC):
    @abc.abstractclassmethod
    def acciones_dict(self):
        raise NotImplementedError
    
    @abc.abstractclassmethod
    def escoger_accion(self, partido):
        raise NotImplementedError
    
    



