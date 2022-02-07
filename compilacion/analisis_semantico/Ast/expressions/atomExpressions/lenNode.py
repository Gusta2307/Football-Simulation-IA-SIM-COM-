
from typing import Iterable
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.idNode import IdNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.arrayAtom import ArrayAtomNode
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope

class LenNode(AtomExpression):
    def __init__(self, array) -> None:
        self.array = array
    
    def checkSemantic(self, scope: Scope) -> bool:
        return scope.check_var(self.array.identifier)

    def evaluate(self, scope: Scope):
        if type(self.array) == IdNode:
            self.array = scope.defineVar[self.array.identifier]
        value = self.array.evaluate(scope)
        return len(value)


    def visit(self, scope):
        self.computed_type = "int"
        return True