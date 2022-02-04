from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class RangeChoiceNode(AtomExpression):
    def __init__(self, list_items, distribution=None) -> None:
        self.list_items = list_items
        self.distribution = distribution

    def checkSemantic(self, scope: Scope) -> bool:
        if self.distribution is not None:
            if not self.distribution.checkSemantic(scope):
                return False
        
        for item in self.list_items:
            if not item.checkSemantic(scope):
                return False
        return True
      
    def evaluate(self, scope: Scope):
        pass
        # if self.distribution is not None:
        #     return self.distribution.evaluate(scope)
        # return None
 