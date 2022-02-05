from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope


class ReturnNode(Instruction):
    def __init__(self, expr: Expression = None) -> None:
        self.expr = expr
        self.value = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        if not self.expr.checkSemantic(scope):
            print("ID ERROR:", self.expr)
            return False
        return True

    def execute(self, scope: Scope):
        print("SCOPE EXE EXE", scope.defineVar)
        self.value = self.expr.evaluate(scope)
        print("TIPO DE VAL:", self.expr)
        print("VALUE EN RETURN:", self.value)
        return self.value