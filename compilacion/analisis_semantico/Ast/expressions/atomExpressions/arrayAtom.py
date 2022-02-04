
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class ArrayAtomNode(AtomExpression):
    def __init__(self, items) -> None:
        self.items = items

    def checkSemantic(self, scope: Scope) -> bool:
        for item in self.items:
            # print(item)
            if not item.checkSemantic(scope):
                return False
        return True
      
    def evaluate(self, scope: Scope):
        return [i.evaluate(scope) for i in self.items]