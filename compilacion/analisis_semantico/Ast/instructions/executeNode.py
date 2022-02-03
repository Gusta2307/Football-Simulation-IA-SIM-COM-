
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope


class ExecuteNode(Instruction):
    def __init__(self, identifier, list_items, player) -> None:
        self.identifier = identifier
        self.list_items = list_items
        self.player = player
    
    def checkSemantic(self, scope: Scope) -> bool:
        return super().checkSemantic(scope)

    def execute(self, scope: Scope):
        return super().execute(scope)