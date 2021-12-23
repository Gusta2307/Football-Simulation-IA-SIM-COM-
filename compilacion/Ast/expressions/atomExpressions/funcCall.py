from typing import List
from compilacion.Ast.expressions.atomExpression import AtomExpression
from compilacion.Ast.expression import Expression
from compilacion.Ast.scope import Scope


class FuncCall(AtomExpression):
    def __init__(self, identifier: str, args: List[Expression]) -> None:
        self.identifier = identifier
        self.args = args

    def checkSemantic(self, scope: Scope) -> bool:
        for expr in self.args:
            if not expr.checkSemantic(scope):
                return False
        return scope.check_fun(self.identifier, len(self.args))
    
    def evaluate(self, scope: Scope):
        pass