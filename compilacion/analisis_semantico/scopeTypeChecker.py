
class ScopeTypeChecker:
      def __init__(self) -> None:
          self.varsType = {}
          self.funcsType = {}

      def check_var(self, symbol: str)-> bool:
          return self.varsType.__contains__(symbol)
      
      def save_varType(self, symbol: str, sym_type) -> bool:
          if not self.check_var(symbol):
                self.varsType[symbol] = sym_type
                return True
          return False
        
      def check_func(self, symbol: str)-> bool:
          return self.funcsType.__contains__(symbol)

      def check_name_fun(self, identifier: str) -> bool:
        return len(list(filter(lambda x : x[0] == identifier, self.funcsType.keys()))) > 0
      
      def save_funcType(self, symbol: str, sym_type) -> bool:
          if not self.check_var(symbol):
                self.funcsType[symbol] = sym_type
                return True
          return False