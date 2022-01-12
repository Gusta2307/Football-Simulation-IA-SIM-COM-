from typing import List
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope


class FunctionNode(Instruction):
    def __init__(self, identifier: str, return_type: str, args: List[str], arg_types: List[str],  body: List[Instruction]) -> None:
        self.identifier = identifier
        self.return_type = return_type
        self.args = args
        self.arg_types = arg_types
        self.body = body
        self.func_scope = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        func_scope = Scope()
        
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