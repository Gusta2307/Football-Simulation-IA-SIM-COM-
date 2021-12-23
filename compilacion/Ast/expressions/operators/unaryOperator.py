from enum import Enum, auto
from typing import Match
from compilacion.Ast.expression import Expression
from compilacion.Ast.scope import Scope


class UnaryOperator(Expression):
    def __init__(self, expr: Expression) -> None:
        self.expr = expr
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.expr.checkSemantic(scope)