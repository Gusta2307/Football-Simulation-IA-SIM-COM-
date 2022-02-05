from typing import List
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.idNode import IdNode
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.functionNode import FunctionNode
from compilacion.analisis_semantico.scope import Scope


class FuncCall(AtomExpression, Instruction):
    def __init__(self, identifier: str, args=[]) -> None:
        self.identifier = identifier
        self.args = args 

    def checkSemantic(self, scope: Scope) -> bool:
        if self.args is not None:
            for expr in self.args:
                if not expr.checkSemantic(scope):
                    return False
            return scope.check_fun(self.identifier, len(self.args))
        return True
    
    def evaluate(self, scope: Scope):
        if scope.check_fun(self.identifier, len(self.args)):
            function = scope.defineFun[(self.identifier, len(self.args))]
            values = []
            for expr in self.args: # los argumentos se buscan en el scope de afuera
                value = expr.evaluate(scope)
                if value is None:
                    return None
                else:
                    if type(expr) == FunctionNode:
                        values.append(('func', value))
                    else:
                        values.append(('id', value))
            return function.evaluateFunction(values)
        return None

    def execute(self, scope: Scope):
        self.evaluate(scope)