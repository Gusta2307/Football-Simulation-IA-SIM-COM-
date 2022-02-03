from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class IndexNode(AtomExpression):
    def __init__(self, identifier: str, number: int) -> None:
        self.identifier = identifier
        self.number = number

    def checkSemantic(self, scope: Scope) -> bool:
        return scope.check_var(self.identifier)
    
    def evaluate(self, scope: Scope):
        if scope.check_var(self.identifier):
            var_value = scope.defineVar[self.identifier]
            num = self.number.evaluate(scope)
            index = num % len(var_value)
            return var_value[index]
        return None