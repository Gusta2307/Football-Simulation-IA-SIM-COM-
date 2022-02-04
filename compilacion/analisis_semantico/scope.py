from typing import List


class Scope:
    def __init__(self) -> None:
        self.defineVar = {}
        self.defineFun = {}
        self.pred_functions = []


    def check_var(self, identifier: str)-> bool:
        return self.defineVar.__contains__(identifier)

    def check_fun(self, identifier: str, count_args: int)-> bool:
        return self.defineFun.__contains__((identifier, count_args))
    
    def check_name_fun(self, identifier: str) -> bool:
        return len(list(filter(lambda x : x[0] == identifier, self.defineFun.keys()))) > 0


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
