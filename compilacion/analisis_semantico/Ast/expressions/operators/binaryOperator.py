from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope


class BinaryOperator(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.left.checkSemantic(scope) and self.right.checkSemantic(scope)