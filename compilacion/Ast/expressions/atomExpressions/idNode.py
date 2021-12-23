from compilacion.Ast.expressions.atomExpression import AtomExpression
from compilacion.Ast.scope import Scope


class IdNode(AtomExpression):
    def __init__(self, identifier: str) -> None:
        self.identifier = identifier

    def checkSemantic(self, scope: Scope) -> bool:
        return scope.check_var(self.identifier)
    
    def evaluate(self, scope: Scope):
        pass