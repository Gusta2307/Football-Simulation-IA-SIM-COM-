from compilacion.Ast.expressions.atomExpression import AtomExpression
from compilacion.Ast.scope import Scope


class NumberNode(AtomExpression):
    def __init__(self, value: float) -> None:
        self.value = value

    def checkSemantic(self, scope: Scope) -> bool:
        return True
    
    def evaluate(self, scope: Scope):
        return self.value