from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.analisis_semantico.scope import Scope


class AddNode(BinaryOperator):
    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__(left, right)

    def evaluate(self, scope: Scope):
        operand1 = self.left.evaluate(scope)
        operand2 = self.right.evaluate(scope)
        
        if type(operand1) != type(operand2) and ((type(operand1) != int and type(operand1) != float and type(operand1) != str) or (type(operand2) != int and type(operand2) != float) and type(operand1) != str):
            raise Exception("Operation not support")
            
        return operand1 + operand2

    def visit(self, scope):
        if not self.left.visit(scope) or not self.right.visit(scope):
            return False
        
        if self.left.computed_type != self.right.computed_type:
            if (self.left.computed_type == "int" or self.left.computed_type == "float") and (self.right.computed_type == "float" or self.right.computed_type == "int"):
                self.computed_type = "float"
                return True
            elif (self.left.computed_type == "int" or self.left.computed_type == "rangeint") and (self.right.computed_type == "rangeint" or self.right.computed_type == "int"):
                self.computed_type = "int"
                return True
            elif (self.left.computed_type == "float" or self.left.computed_type == "rangefloat") and (self.right.computed_type == "rangefloat" or self.right.computed_type == "float"):
                self.computed_type = "float"
                return True
            elif (self.left.computed_type == "bool" or self.left.computed_type == "rangebool") and (self.right.computed_type == "rangebool" or self.right.computed_type == "bool"):
                self.computed_type = "bool"
                return True
            elif self.left.computed_type == "exec" or self.right.computed_type == "exec":
                self.computed_type = "exec"
                return True
            else:
                self.computed_type = 0
                print(f"Left expression has type {self.left.computed_type} and right expression has type {self.right.computed_type}")
                return False
        else:
            if self.left.computed_type == "str" or self.left.computed_type == "int" or self.left.computed_type == "float":            
                self.computed_type = self.left.computed_type
                return True
            else:
                print(f"Type can only be numeric or str")
        return False