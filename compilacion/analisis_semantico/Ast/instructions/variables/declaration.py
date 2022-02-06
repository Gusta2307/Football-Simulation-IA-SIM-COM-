from typing import List
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.Ast.attributeNode import AttributeNode
from compilacion.analisis_semantico.scope import Scope
from utiles import create_dict
from utiles import check_type
from classes.jugador import Jugador
from classes.equipo import Equipo
from classes.portero import Portero
from classes.arbitro import Arbitro
from classes.manager import Manager
from classes.partido import Partido
from IA.range import RangeInt
from IA.range import RangeBool
from IA.range import RangeFloat
from IA.range import RangeChoice


class Declaration(VariableNode):
    def __init__(self, identifier: str, var_type: str, args = []) -> None:
        super().__init__(identifier, var_type)
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        if self.args is not None:
            for arg in self.args:
                print(arg)
                if not arg.checkSemantic(scope):
                    return False    
        return scope.define_variables(self.identifier)

    def execute(self, scope: Scope):
        if scope.check_var(self.identifier):  # prop = value, ej: name, Messi, tipo
            inst = None
            argumentos = create_dict(self.args, scope)
            if self.type == "player":
                #nombre, pos, list_prob, estrategia = None # player p1 = ([AttributeNode(name, Messi, string), AttribuNode(age, 20, int)])
                inst = Jugador(**argumentos)
                # if check_type("player", argumentos, scope):
                    # inst = jugador(**argumentos)
                    # print("BIEN")
            elif self.type == "team": 
                inst = Equipo(**argumentos) 
            elif self.type == "goalkeeper":
                inst = Portero(**argumentos)
            elif self.type == "referee":
                inst = Arbitro(**argumentos)
            elif self.type == "manager":
                inst = Manager(**argumentos)
            elif self.type == "rangeint":
                inst = RangeInt(**argumentos)
            elif self.type == "rangefloat":
                inst = RangeFloat(**argumentos)
            elif self.type == "rangebool":
                inst = RangeBool(**argumentos)
            elif self.type == "rangechoice":
                inst = RangeChoice(**argumentos)
            elif self.type == "game":
                inst = Partido(**argumentos)
            scope.defineVar[self.identifier] = inst
            return inst
            
    
    def __str__(self) -> str:
        string = ""
        for i in range(len(self.args)):
            string += str(self.args[i])
            if i != len(self.args) - 1:
                string += ", "
        return string

    
    def visit(self, scope): # los errores de declaration se ven en ejecucion
        for attr in self.args:
            if not attr.visit(scope):
                return False
        self.computed_type = self.type
        scope.save_varType(self.identifier, self.type)
        return True
