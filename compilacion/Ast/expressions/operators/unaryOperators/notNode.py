from compilacion.Ast.expressions.operators.unaryOperator import UnaryOperator
from compilacion.Ast.scope import Scope


class NotNode(UnaryOperator):
    def evaluate(self, scope: Scope):
        operand = self.expr.evaluate(scope)
        return not operand
