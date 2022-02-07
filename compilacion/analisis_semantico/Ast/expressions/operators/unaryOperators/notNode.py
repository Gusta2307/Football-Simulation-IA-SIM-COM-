from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.expressions.operators.unaryOperator import UnaryOperator
from compilacion.analisis_semantico.scope import Scope


class NotNode(UnaryOperator):
    def __init__(self, expr: Expression) -> None:
        super().__init__(expr)

    def evaluate(self, scope: Scope):
        operand = self.expr.evaluate(scope)
        if type(operand) != bool:
            raise Exception("Operation not support")
        return not operand
    
    def visit(self, scope):
        if not self.expr.visit(scope):
            return False

        if self.expr.computed_type == "bool":
          self.computed_type = self.expr.computed_type
          return True
        print("Type can only be boolean")
        return False
