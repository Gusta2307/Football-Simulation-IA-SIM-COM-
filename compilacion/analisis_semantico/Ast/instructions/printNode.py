from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope

class PrintNode(Instruction):
    def __init__(self, expr) -> None:
        self.expr = expr
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.expr.checkSemantic(scope)

    def execute(self, scope: Scope):
        value = self.expr.evaluate(scope)
        return print(value)
    

    def visit(self, scope):
        return self.expr.visit(scope)