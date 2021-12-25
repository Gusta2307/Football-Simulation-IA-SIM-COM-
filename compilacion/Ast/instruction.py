import abc
from compilacion.Ast.scope import Scope
from compilacion.Ast.AstNode import AstNode


class Instruction(AstNode):
    @abc.abstractclassmethod
    def execute(self, scope: Scope):
        pass