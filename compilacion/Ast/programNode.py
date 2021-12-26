from typing import List
from compilacion.Ast import AstNode
from compilacion.Ast.instruction import Instruction
from compilacion.Ast.scope import Scope


class ProgramNode(AstNode):
    def __init__(self, statement: List[Instruction]) -> None:
        self.statement = statement

    
    def checkSemantic(self, scope: Scope) -> bool:
        for inst in self.statement:
            if not inst.checkSemantic(scope):
                return False
        return True
    
    def execute(self, scope: Scope):
        if self.checkSemantic(scope):
            for inst in self.statement:
                inst.execute(scope)
