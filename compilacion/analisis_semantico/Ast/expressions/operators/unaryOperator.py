from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope


class UnaryOperator(Expression):
    def __init__(self, expr: Expression) -> None:
        self.expr = expr
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.expr.checkSemantic(scope)
