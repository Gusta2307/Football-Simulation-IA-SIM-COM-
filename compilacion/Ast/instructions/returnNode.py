from compilacion.Ast.instruction import Instruction
from compilacion.Ast.expression import Expression
from compilacion.Ast.scope import Scope


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