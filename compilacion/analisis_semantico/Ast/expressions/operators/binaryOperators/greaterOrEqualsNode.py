from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.analisis_semantico.scope import Scope


class GreaterOrEqualsNode(BinaryOperator):
    def evaluate(self, scope: Scope):
        operand1 = self.left.evaluate(scope)
        operand2 = self.right.evaluate(scope)
        return operand1 >= operand2
