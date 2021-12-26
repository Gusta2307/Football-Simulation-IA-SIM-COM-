from typing import List
from compilacion.Ast.expression import Expression
from compilacion.Ast.scope import Scope

class RangeNode(Expression):
    def __init__(self, args: List[Expression]) -> None:
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        for inst in self.args:
            if not inst.checkSemantic(scope):
                return False
        return True

    def evaluate(self, scope: Scope):
        args_evaluated = [item.evaluate(scope) for item in self.args]
        return range(*args_evaluated)