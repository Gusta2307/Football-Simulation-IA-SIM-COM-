class Estrategia:
    def __init__(self, variables:dict, execute) -> None:
        self.variables = variables 
        self.execute = execute
    

    def evaluar(self, partido, jugador):
        self.execute.func_scope.defineVar[self.execute.state_game] = partido
        self.execute.func_scope.defineVar[self.execute.player] = jugador
        
        for v in self.variables.keys():
            self.execute.func_scope.defineVar[v]= self.variables[v]
        return self.execute.evaluateStrategy()


