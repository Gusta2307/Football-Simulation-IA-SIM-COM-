from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class IdNode(AtomExpression):
    def __init__(self, identifier: str) -> None:
        self.identifier = identifier

    def checkSemantic(self, scope: Scope) -> bool:
        v = scope.check_var(self.identifier)
        v1 = scope.check_name_fun(self.identifier)
        print("v:", v)
        print("v1:", v1)
        return v or v1
        # return scope.check_var(self.identifier) or scope.check_name_fun(self.identifier)
    
    def evaluate(self, scope: Scope):
        if scope.check_var(self.identifier):
            print("ENTREE EXEcUTE ID")
            return scope.defineVar[self.identifier]
        return None

    def visit(self, scope):
        if scope.check_symbol(self.identifier):
            self.computed_type = scope.varsType[self.identifier]
            return True
        else:
            self.computed_type = 0
            print(f"This {self.identifier} is not declared")
        return False
    
    def __str__(self) -> str:
        return str(self.identifier)