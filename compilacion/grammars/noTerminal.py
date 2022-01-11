

class NoTerminal:
    def __init__(self, name : str) -> None:
        self.name = name
        self.productions = []
    
    def add_production(self, production):
        self.productions.append(production)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

#ej: 
# <atom> es un no terminal
# en las reglas sintacticas definimos: <atom> := ID 
#                                              | NUMBER 
# Por tanto las producciones de <atom> son: ID y NUMBER
