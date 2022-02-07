from typing import List
import string

class Scope:
    def __init__(self) -> None:
        self.defineVar = {}
        self.defineFun = {}
        self.originType = {}
        self.pred_functions = []
        self.program_keywords = self.register_keywords()


    def check_var(self, identifier: str)-> bool:
        return self.defineVar.__contains__(identifier)

    def check_fun(self, identifier: str, count_args: int)-> bool:
        return self.defineFun.__contains__((identifier, count_args))

    def check_varType(self, identifier: str)-> bool:
        return self.originType.__contains__(identifier)

    def check_name_fun(self, identifier: str) -> bool:
        return len(list(filter(lambda x : x[0] == identifier, self.defineFun.keys()))) > 0

    def define_variables(self, identifier: str) -> bool:
        if identifier in self.program_keywords:
            print(f"{identifier} is a keyword")
            return False
        if not self.check_var(identifier):
            self.defineVar[identifier] = None
            return True
        print(f"Variable {identifier} is defined")
        return False

    def define_function(self, identifier: str, args: List[str]) -> bool:
        if identifier in self.program_keywords:
            print(f"{identifier} is a keyword")
            return False
        if not self.check_fun(identifier, len(args)):
            self.defineFun[(identifier, len(args))] = (args, None)
            return True
        print(f"Function {identifier} is defined")
        return False

    def register_keywords(self):
        keywords = ['AND','OR','NOT','player','team','manager','referee','game','for','in','print','goalkeeper','len','by','if','elif','else','function','return','strategy','variables','execute','range','rangeint','rangefloat','rangebool','rangechoice','int','float','str','bool','void','object','True','False','break','continue','report']
        return keywords