from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope

class PrintNode(Instruction):
    def __init__(self, expr) -> None:
        self.expr = expr
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.expr.checkSemantic(scope)
        # for inst in self.expr:
        #     if not inst.checkSemantic(scope):
        #         return False
        # return True

    def execute(self, scope: Scope):
        value = self.expr.evaluate(scope)
        return print(value)
        # args_evaluated = [item.evaluate(scope) for item in self.expr]
        # return print(*args_evaluated)