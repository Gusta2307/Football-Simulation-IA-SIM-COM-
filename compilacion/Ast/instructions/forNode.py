from typing import List
from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope


class ForNode(Instruction):
    def __init__(self, item: str, list_items: list, body: List[Instruction]) -> None:
        self.item = item
        self.list_items = list_items
        self.body = body
    
    def checkSemantic(self, scope: Scope) -> bool:
        #Duda: como item cambia constantemente no se como tratarlo
        pass

    def execute(self, scope: Scope):
        pass