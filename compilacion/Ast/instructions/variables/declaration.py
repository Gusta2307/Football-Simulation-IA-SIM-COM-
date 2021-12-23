from typing import List
from compilacion.Ast.expressions.atomExpression import AtomExpression
from compilacion.Ast.instructions.variableNode import VariableNode
from compilacion.Ast.scope import Scope


class Declaration(VariableNode):
    def __init__(self, identifier: str, args: List[str]) -> None:
        super().__init__(identifier)
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        for arg in self.args:
            if arg.value is not AtomExpression or not arg.checkSemantic(scope):
                return False
        return scope.define_variables(self.identifier)

    def execute():
        pass