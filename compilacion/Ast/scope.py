from _typeshed import Self
from typing import List
from compilacion.Ast.instructions.functionNode import FunctionNode
from compilacion.Ast.instructions.variableNode import VariableNode


class Scope:
    def __init__(self) -> None:
        self.defineVar = {}
        self.defineFun = {}

    def check_var(self, identifier: str)-> bool:
        return self.defineVar.__contains__(identifier)

    def check_fun(self, identifier: str, count_args: int)-> bool:
        return self.defineFun.__contains__((identifier, count_args))

    def define_variables(self, identifier: str) -> bool:
        if not self.check_var(identifier):
            self.defineVar[identifier] = None
            return True
        return False

    def define_function(self, identifier: str, args: List[str]) -> bool:
        if not self.check_fun(identifier, len(args)):
            self.defineFun[(identifier, len(args))] = (args, None)
            return True
        return False

    def create_scope() -> Self:
        return Scope()