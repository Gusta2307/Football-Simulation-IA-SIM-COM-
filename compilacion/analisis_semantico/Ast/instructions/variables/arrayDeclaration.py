from typing import List
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.scope import Scope


class ArrayDeclaration(VariableNode):
    def __init__(self, identifier: str, var_type: str, items) -> None:
        super().__init__(identifier)
        super().__init__(var_type)
        self.items = items
    
    def checkSemantic(self, scope: Scope) -> bool:
        for item in self.items:
            if not item.checkSemantic(scope):
                return False
        return scope.define_variables(self.identifier)