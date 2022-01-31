from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.analisis_semantico.scope import Scope


class DivNode(BinaryOperator):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def evaluate(self, scope: Scope):
        operand1 = self.left.evaluate(scope)
        operand2 = self.right.evaluate(scope)

        if operand2 == 0: #div entre 0 no valida
            return None
        return operand1 / operand2
