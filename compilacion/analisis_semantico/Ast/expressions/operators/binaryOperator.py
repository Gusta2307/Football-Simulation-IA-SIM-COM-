from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope


class BinaryOperator(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.left.checkSemantic(scope) and self.right.checkSemantic(scope)

    def visit(self, scope): # se debe hacer uno por cada expresion
        if not self.left.visit(scope) or not self.right.visit(scope):
            return False
        
        if self.left.computed_type != self.right.computed_type:
            if (self.left.computed_type == "int" or self.left.computed_type == "float") and (self.right.computed_type == "float" or self.right.computed_type == "int"):
                self.computed_type = "float"
            elif self.left.computed_type == "exec" or self.right.computed_type == "exec":
                self.computed_type = "exec"
            else:
                self.computed_type = 0
                print(f"Left expression has type {self.left.computed_type} and right expression has type {self.right.computed_type}")
                return False
        else:
            self.computed_type = self.left.computed_type

        return True