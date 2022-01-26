import abc

class Agente(abc.ABC):
    @abc.abstractclassmethod
    def acciones_dict(self):
        raise NotImplementedError
    
    @abc.abstractclassmethod
    def escoger_accion_agente(self, partido):
        raise NotImplementedError
    
    



