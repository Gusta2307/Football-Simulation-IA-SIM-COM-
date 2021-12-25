from typing import List
from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope


class FunctionNode(Instruction):
    def __init__(self, identifier: str, args: List[str], body: List[Instruction]) -> None:
        self.identifier = identifier
        self.args = args
        self.body = body
    
    def checkSemantic(self, scope: Scope) -> bool:
        func_scope = scope.create_scope()
        
        for arg in self.args:
            func_scope.define_variables(arg)
        
        for inst in self.body:
            if not inst.checkSemantic(func_scope):
                return False
                
        return scope.defineFun(self.identifier, self.args)

    def execute(self, scope: Scope):
        pass