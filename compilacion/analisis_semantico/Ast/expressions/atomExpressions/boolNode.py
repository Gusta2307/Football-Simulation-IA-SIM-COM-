from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class BoolNode(AtomExpression):
    def __init__(self, value) -> None:
        self.value = value

    def checkSemantic(self, scope: Scope) -> bool:
        return True
    
    def evaluate(self, scope: Scope):
        return self.value

    def __str__(self) -> str:
        return str(self.value)