from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.analisis_semantico.scope import Scope


class EqualsNode(BinaryOperator):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def evaluate(self, scope: Scope):
        operand1 = self.left.evaluate(scope)
        operand2 = self.right.evaluate(scope)

        if type(operand1) != type(operand2) and ((type(operand1) != int and type(operand1) != float) or (type(operand2) != int and type(operand2) != float)):
            raise Exception("Operation not support")
            
        return operand1 == operand2
