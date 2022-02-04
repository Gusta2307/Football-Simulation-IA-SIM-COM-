
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope


class ExecuteNode(Instruction):
    def __init__(self, state_game, list_items, player) -> None:
        self.state_game = state_game
        self.list_items = list_items
        self.player = player
    
    def checkSemantic(self, scope: Scope) -> bool:
        func_scope = Scope()
        self.func_scope = func_scope

        for inst in self.list_items:
            if not inst.checkSemantic(func_scope):
                return False
        return True
        # return scope.define_function(self.identifier, self.args)

    def evaluateStrategy(self, values):
        pass    
    
    def execute(self, scope: Scope):
        pass