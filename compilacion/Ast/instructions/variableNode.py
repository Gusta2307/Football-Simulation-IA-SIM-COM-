from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope


class VariableNode(Instruction):
    def __init__(self, identifier: str) -> None:
        self.identifier = identifier


    def execute(self, scope: Scope):
        if (scope.check_var(self.identifier)):
            scope.defineVar[self.identifier] = self