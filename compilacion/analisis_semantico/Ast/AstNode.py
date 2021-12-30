import abc
from compilacion.analisis_semantico.scope import Scope


class AstNode(abc.ABC):
    @abc.abstractclassmethod
    def checkSemantic(self, scope: Scope) -> bool:
        pass