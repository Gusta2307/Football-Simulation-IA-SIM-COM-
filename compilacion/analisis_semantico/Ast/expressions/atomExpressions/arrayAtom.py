
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

    
    def visit(self, scope):
        curr_type = None
        for i in range(len(self.items)):
            item = self.items[i]
            item.visit(scope)
            if i == 0:
                curr_type = item.computed_type
            if curr_type != item.computed_type:
                curr_type = "object"
                break
        self.computed_type = curr_type
        return True