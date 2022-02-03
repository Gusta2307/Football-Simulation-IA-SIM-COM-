from typing import Iterable
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope

class LenNode(AtomExpression):
    def __init__(self, array) -> None:
        self.array = array
    
    def checkSemantic(self, scope: Scope) -> bool:
        return scope.check_var(self.array.identifier)

    def evaluate(self, scope: Scope):
        if scope.check_var(self.array.identifier):
            return len(scope.defineVar[self.array.identifier])
            # CREO Q AQUI VA UN ERROR
        return None