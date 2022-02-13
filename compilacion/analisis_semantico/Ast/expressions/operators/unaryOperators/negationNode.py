from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.expressions.operators.unaryOperator import UnaryOperator
from compilacion.analisis_semantico.scope import Scope


class NegationNode(UnaryOperator):
      def __init__(self, expr: Expression) -> None:
          super().__init__(expr)

      def evaluate(self, scope: Scope):
        operand = self.expr.evaluate(scope)
        if type(operand) != int and type(operand) != float:
            raise Exception("Operation not support")
        return 0 - operand


      def visit(self, scope):
        if not self.expr.visit(scope):
            return False

        if self.expr.computed_type == "int" or self.expr.computed_type == "float" or self.expr.computed_type == "exec":
          self.computed_type = self.expr.computed_type
          return True
        print("Type can only be numeric")
        return False