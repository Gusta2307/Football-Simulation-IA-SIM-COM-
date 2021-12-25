from compilacion.Ast.expression import Expression
from compilacion.Ast.instructions.variableNode import VariableNode
from compilacion.Ast.scope import Scope


class AssignNode(VariableNode):
    def __init__(self, identifier: str, value: Expression) -> None:
        super().__init__(identifier)
        self.value = value
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.value.checkSemantic(scope) and scope.define_variables(self.identifier)