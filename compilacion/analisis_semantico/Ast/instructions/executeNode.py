
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.scope import Scope


class ExecuteNode(Instruction):
    def __init__(self, state_game, list_items, player) -> None:
        self.state_game = state_game
        self.list_items = list_items
        self.player = player
        self.func_scope = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        # self.func_scope = Scope()
        self.func_scope = scope
        self.func_scope.define_variables(self.state_game)
        self.func_scope.define_variables(self.player)
        
        for inst in self.list_items:
            if not inst.checkSemantic(self.func_scope): #Scope
                print("INST ERROR:", inst)
                return False
        return True
        # return scope.define_function(self.identifier, self.args)

    def evaluateStrategy(self):
        for inst in self.list_items:
            print("INSTRUCTION DE EXECUTE", inst)
            if type(inst) == ReturnNode:
                value = inst.execute(self.func_scope)
                print("VALUEEEEEEEE", value)
                if value in self.func_scope.defineVar[self.player].acciones.keys(): #En caso contrario retornar error
                    return value
            value = inst.execute(self.func_scope)
            
            if value is not None:
                return value
    
   # def evaluateFunction(self, values):
#         for i in range(len(values)):            
#             val_type, value = values[i]
#             if val_type == 'func':
#                 self.func_scope.defineFunc[(self.args[i], len(self.args))] = value
#             else:
#                 self.func_scope.defineVar[self.args[i].identifier] = value
        
#         for inst in self.body:
#             if type(inst) == ReturnNode:
#                 value = inst.execute(self.func_scope)
#                 return value
#             value = inst.execute(self.func_scope)
#             if value is not None:
#                 return value

    def execute(self, scope: Scope):
        pass