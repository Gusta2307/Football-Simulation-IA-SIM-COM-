from typing import Iterable
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope

class LenNode(Instruction):
    def __init__(self, array) -> None:
        self.array = array
    
    def checkSemantic(self, scope: Scope) -> bool:
        if scope.check_var(self.array):
            if not scope.defineVar[self.array].checkSemantic(scope):
                return False
        return True

    def execute(self, scope: Scope):
        if scope.check_var(self.array):
            if scope.defineVar[self.array] is Iterable:
                return len(scope.defineVar[self.array])
            # CREO Q AQUI VA UN ERROR
        return None