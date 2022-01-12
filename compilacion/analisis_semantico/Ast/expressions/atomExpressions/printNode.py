from typing import List
from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope

class PrintNode(Expression):
    def __init__(self, args: List[Expression]) -> None:
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        for inst in self.args:
            if not inst.checkSemantic(scope):
                return False
        return True

    def execute(self, scope: Scope):
        args_evaluated = [item.evaluate(scope) for item in self.args]
        return print(*args_evaluated)