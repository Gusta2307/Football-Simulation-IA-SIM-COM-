from compilacion.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.Ast.scope import Scope


class LessNode(BinaryOperator):
    def evaluate(self, scope: Scope):
        operand1 = self.left.evaluate(scope)
        operand2 = self.right.evaluate(scope)
        return operand1 < operand2
