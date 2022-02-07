from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.Ast.instructions.functionNode import FunctionNode
from compilacion.analisis_semantico.scope import Scope


class IdNode(AtomExpression):
    def __init__(self, identifier: str) -> None:
        self.identifier = identifier

    def checkSemantic(self, scope: Scope) -> bool:
        return scope.check_var(self.identifier) or scope.check_name_fun(self.identifier)

    def evaluate(self, scope: Scope):
        if scope.check_var(self.identifier):
            return scope.defineVar[self.identifier]
        elif scope.check_name_fun(self.identifier):
            try:
                return scope.defineFun[(self.identifier, 1)]
            except:
                return None
        return None

    def visit(self, scope):
        if scope.check_var(self.identifier):
            self.computed_type = scope.varsType[self.identifier]
            return True
        elif scope.check_name_fun(self.identifier):
            self.computed_type = scope.funcsType[self.identifier]
            return True
        else:
            self.computed_type = 0
            print(f"Variable {self.identifier} is not declared")
        return False

    def __str__(self) -> str:
        return str(self.identifier)
