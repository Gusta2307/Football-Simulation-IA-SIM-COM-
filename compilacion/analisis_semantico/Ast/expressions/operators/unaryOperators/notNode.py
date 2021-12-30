from compilacion.analisis_semantico.Ast.expressions.operators.unaryOperator import UnaryOperator
from compilacion.analisis_semantico.scope import Scope


class NotNode(UnaryOperator):
    def evaluate(self, scope: Scope):
        operand = self.expr.evaluate(scope)
        return not operand
