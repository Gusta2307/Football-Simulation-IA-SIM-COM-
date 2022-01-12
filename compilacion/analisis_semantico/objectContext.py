from compilacion.analisis_semantico.type import MyType


class ObjectContext:
    def __init__(self) -> None:
        self.definedTypes = {}
        self.definedSymbols = {}
    

    def get_type(self, typeName: str) -> MyType:
        return self.definedTypes[typeName]

    def type_of(self, symbol: str) -> MyType:
        if self.definedSymbols.__contains__(symbol):
            return self.definedSymbols[symbol]
    

    def define_symbol(self, symbol: str, sym_type: MyType) -> bool:
        if not self.definedSymbols.__contains__(symbol):
            self.definedSymbols[symbol] = sym_type
            return True
        return False
    
    def create_type(self, typeName: str)-> MyType: # seria algo asi
        pass
        # myType = None
        # if typeName == "player":
        #     myType = PlayerType()
        # elif:
        #     #etc
