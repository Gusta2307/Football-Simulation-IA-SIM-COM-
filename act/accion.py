import abc

class Accion(abc.ABC):
    @abc.abstractclassmethod
    def descripcion(self):
        raise NotImplementedError
        
    @abc.abstractclassmethod
    def precondicion(self, partido) -> bool:
        raise NotImplementedError

    @abc.abstractclassmethod
    def ejecutar(self, partido, **args):
        raise NotImplementedError

    @abc.abstractclassmethod
    def poscondicion(self, partido, **args):
        raise NotImplementedError

    