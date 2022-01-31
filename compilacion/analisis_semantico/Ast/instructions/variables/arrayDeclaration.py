from typing import List
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.scope import Scope


class ArrayDeclaration(VariableNode):
    def __init__(self, identifier: str, var_type: str, items) -> None:
        super().__init__(identifier, var_type)
        self.items = items
    
    def checkSemantic(self, scope: Scope) -> bool:
        for item in self.items:
            if not item.checkSemantic(scope):
                return False
        return scope.define_variables(self.identifier)

    def execute(self, scope: Scope):
        if scope.check_var(self.identifier):
            scope.defineVar[self.identifier] = self.items