from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope


class VariableNode(Instruction):
    def __init__(self, identifier: str, var_type: str) -> None:
        self.identifier = identifier
        self.type = var_type


    def execute(self, scope: Scope):
        if scope.check_var(self.identifier):
            scope.defineVar[self.identifier] = self