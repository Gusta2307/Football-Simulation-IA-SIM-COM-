from typing import List
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.Ast.attributeNode import AttributeNode
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.type import MyType


class Declaration(VariableNode):
    def __init__(self, identifier: str, var_type: str, args: List[AttributeNode]) -> None:
        super().__init__(identifier)
        super().__init__(var_type)
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        for arg in self.args:
            if not arg.checkSemantic(scope):
                return False
        return scope.define_variables(self.identifier)