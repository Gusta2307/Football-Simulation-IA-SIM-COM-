import abc
from compilacion.Ast.scope import Scope
from compilacion.Ast.AstNode import AstNode


class Expression(AstNode):
    @abc.abstractclassmethod
    def evaluate(self, scope: Scope):
        pass