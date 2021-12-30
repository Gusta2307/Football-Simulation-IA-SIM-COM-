from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope

class ReturnNode(Instruction):
    def __init__(self, iterable:str, list_item: list, condition: Expression) -> None:
        self.iter = iterable
        self.list_item = list_item
        self.condition = condition
    
    def checkSemantic(self, scope: Scope) -> bool:
        if not scope.check_var(self.iter):
            return False

        for item in self.list_item:
            if not item.checkSemantic(scope):
                return False
        
        if not self.condition.checkSemantic(scope):
            return False
        
        return True

    def execute(self, scope: Scope):
        raise NotImplementedError
