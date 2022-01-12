from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.breakNode import BreakNode
from compilacion.analisis_semantico.Ast.instructions.continueNode import ContinueNode
from compilacion.analisis_semantico.scope import Scope


class ForNode(Instruction):
    def __init__(self, item: str, iterable:str, list_items: list, body: list[Instruction]) -> None:
        self.item = item
        self.iter = iterable
        self.list_items = list_items
        self.body = body
    
    def checkSemantic(self, scope: Scope) -> bool:
        if not scope.check_var(self.iter):
            return False

        if scope.define_variables(self.item):
            for elem in self.lists_item:
                if not elem.checkSemantic(scope):
                    return False 
            for ins in self.body:
                if not ins.checkSemantic(scope):
                    return False
            return True
        return False

    def execute(self, scope: Scope):
        if_break = 0
        for items in self.list_items:
            scope.defineVar[self.item] = items
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