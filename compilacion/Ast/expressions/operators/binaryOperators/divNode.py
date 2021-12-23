from compilacion.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.Ast.scope import Scope


class DivNode(BinaryOperator):
    def evaluate(self, scope: Scope):
        operand1 = self.left.evaluate(scope)
        operand2 = self.right.evaluate(scope)

        if operand2 == 0: #div entre 0 no valida
            return None
        return operand1 / operand2
