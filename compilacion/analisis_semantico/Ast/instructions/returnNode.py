from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope


class ReturnNode(Instruction):
    def __init__(self, expr: Expression = None) -> None:
        self.expr = expr
        self.value = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        if not self.expr.checkSemantic(scope):
            return False
        return True

    def execute(self, scope: Scope):
        self.value = self.expr.evaluate(scope)
        return self.value