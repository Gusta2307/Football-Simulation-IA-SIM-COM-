from typing import List
from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope
from compilacion.Ast.expression import Expression


class Conditional(Instruction):
    def __init__(self, condition: Expression, ifBody: List[Instruction], elseBody: List[Instruction]=None) -> None:
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody

    def checkSemantic(self, scope: Scope) -> bool:
        if not self.condition.checkSemantic(scope):
            return False
        
        for inst in self.ifBody:
            if not inst.checkSemantic(scope):
                return False
        
        if self.elseBody is not None:
            for inst in self.elseBody:
                if not inst.checkSemantic(scope):
                    return False 
        return True

    def execute():
        pass
        
        