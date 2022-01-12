from typing import List, Tuple
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.Ast.expression import Expression


class Conditional(Instruction):
    def __init__(self, condition: Expression, ifBody: List[Instruction], elIf: List[Tuple[Expression, List[Instruction]]] = None, elseBody: List[Instruction] = None) -> None:
        self.condition = condition
        self.ifBody = ifBody
        self.elIf = elIf
        self.elseBody = elseBody

    def checkSemantic(self, scope: Scope) -> bool:
        if not self.condition.checkSemantic(scope):
            return False
        
        for inst in self.ifBody:
            if not inst.checkSemantic(scope):
                return False
        
        if self.elIf is not None:
            for t in self.elIf:
                if not t[0].checkSemantic(scope):
                    return False
                for inst in t[1]:
                    if not inst.checkSemantic(scope):
                        return False

        if self.elseBody is not None:
            for inst in self.elseBody:
                if not inst.checkSemantic(scope):
                    return False 
        return True

    def execute(self, scope: Scope):
        eval_cond = self.condition.evaluate(scope)
        if eval_cond:
            self.execute_instructions(scope, self.ifBody)
        elif self.elIf is not None:
            for t in self.elIf:
                if t[0].evaluate(scope):
                    self.execute_instructions(scope, t[1])
                    break                
        else:
            if self.elseBody is not None:
                self.execute_instructions(scope, self.elseBody)
    
    def execute_instructions(scope, instructions):
        for inst in instructions:
                inst.execute(scope)

        
        