
class ObjectContext:
    def __init__(self) -> None:
        self.definedTypes = {}
        self.definedSymbols = {}

    def get_type(self, typeName: str):
        return self.definedTypes[typeName]

    def type_of(self, symbol: str):
        if self.definedSymbols.__contains__(symbol):
            return self.definedSymbols[symbol]
    
    def define_symbol(self, symbol: str, sym_type) -> bool:
        if not self.definedSymbols.__contains__(symbol):
            self.definedSymbols[symbol] = sym_type
            return True
        return False