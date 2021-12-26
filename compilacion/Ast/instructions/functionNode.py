from typing import List
from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope


class FunctionNode(Instruction):
    def __init__(self, identifier: str, args: List[str], body: List[Instruction]) -> None:
        self.identifier = identifier
        self.args = args
        self.body = body
        self.func_scope = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        func_scope = scope.create_scope()
        
        for arg in self.args:
            func_scope.define_variables(arg)
        
        self.func_scope = func_scope

        for inst in self.body:
            if not inst.checkSemantic(func_scope):
                return False
                
        return scope.defineFun(self.identifier, self.args)

    def evaluateFunction(self, values):
        for i in range(len(values)):            
            val_type, value = values[i]
            if val_type == 'func':
                self.func_scope.defineFunc[(self.args[i], len(self.args))] = value
            else:
                self.func_scope.defineVar[self.args[i]] = value
        
        for inst in self.body:
            inst.execute(self.func_scope)


    def execute(self, scope: Scope):
        if (scope.check_fun(self.identifier)):
            scope.defineFun[self.identifier] = self
