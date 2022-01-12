from typing import Iterable
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope

class LenNode(Expression):
    def __init__(self, args: str) -> None:
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        if scope.check_var(self.args):
            if not scope.defineVar[self.args].checkSemantic(scope):
                return False
        return True

    def evaluate(self, scope: Scope):
        if scope.check_var(self.args):
            if scope.defineVar[self.args] is Iterable:
                return len(scope.defineVar[self.args])
            # CREO Q AQUI VA UN ERROR
        return None