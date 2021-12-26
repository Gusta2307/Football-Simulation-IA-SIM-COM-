from typing import List
from compilacion.Ast.expressions.atomExpression import AtomExpression
from compilacion.Ast.expression import Expression
from compilacion.Ast.expressions.atomExpressions.idNode import IdNode
from compilacion.Ast.instructions.functionNode import FunctionNode
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
        if scope.check_fun(self.identifier, len(self.args)):
            function = scope.defineFun[(self.identifier, len(self.args))][1]
            values = []
            for expr in self.args:
                value = expr.evaluate(function.func_scope)
                if value is None:
                    return None
                else:
                    if type(expr) == FunctionNode:
                        values.append(('func', value))
                    else:
                        values.append(('id', value))
            return function.evaluateFunction(values)
        return None        
