from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope


class BreakNode(Instruction):
    def __init__(self) -> None:
        pass
    
    def checkSemantic(self, scope: Scope) -> bool:
        return True

    def execute(self, scope: Scope):
        pass