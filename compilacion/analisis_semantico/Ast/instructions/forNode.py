from typing import List
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.breakNode import BreakNode
from compilacion.analisis_semantico.Ast.instructions.continueNode import ContinueNode
from compilacion.analisis_semantico.scope import Scope


class ForNode(Instruction):
    def __init__(self, item: str, iterable:str, body: List[Instruction]) -> None:
        self.item = item
        self.iter = iterable
        self.body = body
    
    def checkSemantic(self, scope: Scope) -> bool:
        if not scope.check_var(self.iter.identifier):
            return False

        if scope.define_variables(self.item):
            for ins in self.body:
                if not ins.checkSemantic(scope):
                    return False
            return True
        return False

    def execute(self, scope: Scope):
        if_break = 0
        iterable = scope.defineVar[self.iter.identifier]
        for elem in iterable:
            scope.defineVar[self.item] = elem.evaluate(scope)
            for item_body in self.body:
                if type(item_body) == ContinueNode:
                    break
                elif type(item_body) == BreakNode:
                    if_break = 1
                    break
                else:
                    item_body.execute(scope)
            if if_break:
                break
        scope.defineVar.pop(self.item)