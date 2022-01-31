from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class RangeBoolNode(AtomExpression):
    def __init__(self, distribution=None) -> None:
        self.distribution = distribution

    def checkSemantic(self, scope: Scope) -> bool:
      if self.distribution is not None:
          return self.distribution.checkSemantic(scope)
      return True
      
    def evaluate(self, scope: Scope):
      if self.distribution is not None:
          return self.distribution.evaluate(scope)
      return None