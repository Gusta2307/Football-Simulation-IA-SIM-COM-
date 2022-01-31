from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class RangeFloatNode(AtomExpression):
    def __init__(self, value1, value2, distribution=None) -> None:
        self.value1 = value1
        self.value2 = value2
        self.distribution = distribution

    def checkSemantic(self, scope: Scope) -> bool:
        if not self.value1.checkSemantic(scope):
            return False
        
        if not self.value2.checkSemantic(scope):
              return False
        
        if self.distribution is not None:
            return self.distribution.checkSemantic(scope)
        
        return True
          
    def evaluate(self, scope: Scope):
        pass