from compilacion.Ast.expressions.atomExpression import AtomExpression
from compilacion.Ast.scope import Scope


class IndexNode(AtomExpression):
    def __init__(self, identifier: str, number: int) -> None:
        self.identifier = identifier
        self.number = number

    def checkSemantic(self, scope: Scope) -> bool:
        return scope.check_var(self.identifier)
    
    def evaluate(self, scope: Scope):
        if scope.check_var(self.identifier):
            var_value = scope.defineVar[self.identifier]
            index = self.number % len(var_value.items)
            return var_value.items[index]
        return None