from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class NumberNode(AtomExpression):
    def __init__(self, value) -> None:
        self.value = value

    def checkSemantic(self, scope: Scope) -> bool:
        return True
    
    def evaluate(self, scope: Scope):
        return self.value


class IntNode(NumberNode):
    def __init__(self, value: int) -> None:
        super().__init__(value)
    

class FloatNode(NumberNode):
    def __init__(self, value: float) -> None:
        super().__init__(value)