from compilacion.Ast.expressions.atomExpression import AtomExpression
from compilacion.Ast.expression import Expression
from compilacion.Ast.scope import Scope


class FuncCall(AtomExpression):
    def __init__(self, identifier: str, args: list[Expression]) -> None:
        self.identifier = identifier
        self.args = args

    def checkSemantic(self, scope: Scope) -> bool:
        for expr in self.args:
            if not expr.checkSemantic(scope):
                return False
        return scope.check_fun(self.identifier, len(self.args))
    
    def evaluate(self, scope: Scope):
        if scope.check_fun(self.identifier, len(self.args)):
            values = []
            for expr in self.args:
                value = expr.evaluate(scope)
                if value is None:
                    return None
                else:
                    values.append(value)

            function = scope.defineFun[(self.identifier, len(self.args))][1]

            for inst in function.body:
                pass

        return None        
