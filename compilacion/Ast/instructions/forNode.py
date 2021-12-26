from typing import List
from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope


class ForNode(Instruction):
    def __init__(self, item: str, list_items: list, body: List[Instruction]) -> None:
        self.item = item
        self.list_items = list_items
        self.body = body
    
    def checkSemantic(self, scope: Scope) -> bool:
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
        for items in self.list_items:
            scope.defineVar[self.item] = items
            for item_body in self.body:
                item_body.execute(scope)
        scope.defineVar.pop(self.item)