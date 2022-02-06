from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope


class VariableNode(Instruction):
    def __init__(self, identifier: str, var_type: str) -> None:
        self.identifier = identifier
        self.type = var_type
        self.computed_type = None

    def checkSemantic(self, scope: Scope) -> bool:
        return True
    
    def visit(self, scope):
        return True

    def execute(self, scope: Scope):
        pass