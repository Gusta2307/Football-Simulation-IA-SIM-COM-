from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope


class ReturnNode(Instruction):
    def __init__(self, args: Expression = None) -> None:
        self.args = args
        self.value = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        if not self.args.checkSemantic(scope):
            return False
        return True

    def execute(self, scope: Scope):
        self.value = self.args.evaluate(scope)