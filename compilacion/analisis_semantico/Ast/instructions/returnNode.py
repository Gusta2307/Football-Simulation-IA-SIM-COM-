from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope


class ReturnNode(Instruction):
    def __init__(self, expr: Expression = None) -> None:
        self.expr = expr
        self.value = None
        self.computed_type = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        if self.expr is not None and not self.expr.checkSemantic(scope):
            return False
        return True

    def execute(self, scope: Scope):
        if self.expr is None:
            return None

        self.value = self.expr.evaluate(scope)
        return self.value
    
    def visit(self, scope):
        if self.expr is None:
            self.computed_type = "void"
        else:
            if self.expr.visit(scope):
                self.computed_type = self.expr.computed_type
                return True
            return False
            