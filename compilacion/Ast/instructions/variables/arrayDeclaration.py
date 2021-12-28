from compilacion.Ast.expression import Expression
from compilacion.Ast.instructions.variableNode import VariableNode
from compilacion.Ast.scope import Scope


class ArrayDeclaration(VariableNode):
    def __init__(self, identifier: str, items: list[Expression]) -> None:
        super().__init__(identifier)
        self.items = items
    
    def checkSemantic(self, scope: Scope) -> bool:
        for item in self.items:
            if not item.checkSemantic(scope):
                return False
        return scope.define_variables(self.identifier)