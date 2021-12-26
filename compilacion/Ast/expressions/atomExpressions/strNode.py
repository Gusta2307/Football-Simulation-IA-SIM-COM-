from compilacion.Ast.expression import Expression
from compilacion.Ast.scope import Scope

class StrNode(Expression):
    def __init__(self, args: Expression) -> None:
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        if not self.args.checkSemantic(scope):
            return False
        return True

    def execute(self, scope: Scope):
        return str(self.args.evaluate(scope))