from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope


class ContinueNode(Instruction):
    def __init__(self) -> None:
        pass
    
    def checkSemantic(self, scope: Scope) -> bool:
        return True

    def execute(self, scope: Scope):
        pass