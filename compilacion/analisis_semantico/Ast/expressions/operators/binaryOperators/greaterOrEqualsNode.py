from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.analisis_semantico.scope import Scope


class GreaterOrEqualsNode(BinaryOperator):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def evaluate(self, scope: Scope):
        operand1 = self.left.evaluate(scope)
        operand2 = self.right.evaluate(scope)

        if type(operand1) != type(operand2):
            return None

        return operand1 >= operand2
