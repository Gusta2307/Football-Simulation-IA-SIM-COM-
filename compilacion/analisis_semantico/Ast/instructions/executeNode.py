
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.scope import Scope
import copy
from compilacion.analisis_semantico.scopeTypeChecker import ScopeTypeChecker

class ExecuteNode(Instruction):
    def __init__(self, state_game, list_items, player) -> None:
        self.state_game = state_game
        self.list_items = list_items
        self.player = player
        self.func_scope = None
        self.return_type = "str"
    
    def checkSemantic(self, scope: Scope) -> bool:
        self.func_scope = scope
        self.func_scope.define_variables(self.state_game)
        self.func_scope.define_variables(self.player)
        
        for inst in self.list_items:
            if not inst.checkSemantic(self.func_scope): #Scope
                return False
        return True

    def evaluateStrategy(self):
        for inst in self.list_items:
            if type(inst) == ReturnNode:
                value = inst.execute(self.func_scope)
                if value in self.func_scope.defineVar[self.player].acciones.keys(): #En caso contrario retornar error
                    return value
            value = inst.execute(self.func_scope)
            if value is not None:
                return value

    def execute(self, scope: Scope):
        pass
    
    def visit(self, scope):
        exeScope = ScopeTypeChecker()
        exeScope.funcsType = copy.deepcopy(scope.funcsType)
        exeScope.varsType = copy.deepcopy(scope.varsType)

        if not exeScope.check_var(self.state_game):
            exeScope.varsType[self.state_game] = "game"
        else:
            print(f"{self.state_game} is declared")
            return False
        
        if not exeScope.check_var(self.player):
            exeScope.varsType[self.player] = "player"
        else:
            print(f"{self.player} is declared")
            return False

        for item in self.list_items:
            if not item.visit(exeScope):
                return False
            if type(item) == ReturnNode:
                if self.return_type != item.expr.computed_type:
                    print(f"Return type is {self.return_type} and expression to return has type {item.expr.computed_type}")
                    return False
                return item.expr.computed_type == "str"
        return False