import abc
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.Ast.AstNode import AstNode


class Expression(AstNode):
    def __init__(self) -> None:
        self.computed_type = None

    @abc.abstractclassmethod
    def evaluate(self, scope: Scope):
        pass