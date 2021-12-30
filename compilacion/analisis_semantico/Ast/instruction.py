import abc
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.Ast.AstNode import AstNode


class Instruction(AstNode):
    @abc.abstractclassmethod
    def execute(self, scope: Scope):
        pass