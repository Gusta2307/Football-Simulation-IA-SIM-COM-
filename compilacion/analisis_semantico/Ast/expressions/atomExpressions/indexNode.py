from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class IndexNode(AtomExpression, Instruction):
    def __init__(self, identifier: str, number: int) -> None:
        self.identifier = identifier
        self.number = number

    def checkSemantic(self, scope: Scope) -> bool:
        return scope.check_var(self.identifier)
    
    def evaluate(self, scope: Scope):
        if scope.check_var(self.identifier):
            var_value = scope.defineVar[self.identifier].evaluate(scope)
            num = self.number.evaluate(scope)
            index = num % len(var_value)
            return var_value[index]
        return None
    
    def execute(self, scope: Scope):
        pass

    def visit(self, scope):
        if scope.check_var(self.identifier):
            self.computed_type = scope.varsType[self.identifier]
            return True
        else:
            self.computed_type = 0
            print(f"List {self.identifier} is not defined")
        return False