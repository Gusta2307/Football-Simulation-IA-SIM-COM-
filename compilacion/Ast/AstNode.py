import abc
from compilacion.Ast.scope import Scope


class AstNode(abc.ABC):
    @abc.abstractclassmethod
    def checkSemantic(self, scope: Scope) -> bool:
        pass