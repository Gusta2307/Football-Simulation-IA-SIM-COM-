from typing import List
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.scope import Scope


class FunctionNode(Instruction):
    def __init__(self, identifier: str, return_type: str, args=[], body: List[Instruction]=None) -> None:
        self.identifier = identifier
        self.return_type = return_type
        self.args = args
        self.body = body
        self.func_scope = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        func_scope = Scope()
        
        for arg in self.args:
            func_scope.define_variables(arg.identifier)
        
        self.func_scope = func_scope

        for inst in self.body:
            if not inst.checkSemantic(func_scope):
                return False
                
        return scope.define_function(self.identifier, self.args)

    def evaluateFunction(self, values):
        for i in range(len(values)):            
            val_type, value = values[i]
            if val_type == 'func':
                self.func_scope.defineFunc[(self.args[i], len(self.args))] = value
            else:
                self.func_scope.defineVar[self.args[i].identifier] = value
        
        for inst in self.body:
            if type(inst) == ReturnNode:
                value = inst.execute(self.func_scope)
                return value
            value = inst.execute(self.func_scope)
            if value is not None:
                return value


    def execute(self, scope: Scope):
        if (scope.check_fun(self.identifier, len(self.args))):
            scope.defineFun[(self.identifier, len(self.args))] = self
