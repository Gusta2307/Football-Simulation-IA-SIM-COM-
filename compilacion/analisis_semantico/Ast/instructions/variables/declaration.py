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
    def __init__(self, identifier: str, var_type: str, args: List[AttributeNode]=[]) -> None:
        super().__init__(identifier, var_type)
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        if self.args != []: 
            for arg in self.args:
                if not arg.checkSemantic(scope):
                    return False    
        return scope.define_variables(self.identifier)

    def execute(self, scope: Scope):
        if scope.check_var(self.identifier):  
            inst = None
            argumentos = create_dict(self.args, scope)
            if self.type == "player":
                if check_type("player", argumentos, scope):
                    inst = Jugador(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
            elif self.type == "team":
                if check_type("team", argumentos, scope):
                    inst = Equipo(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
                 
            elif self.type == "goalkeeper":
                if check_type("goalkeeper", argumentos, scope):
                    inst = Portero(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
                
            elif self.type == "referee":
                if check_type("referee", argumentos, scope):
                    inst = Arbitro(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
            elif self.type == "manager":
                if check_type("manager", argumentos, scope):
                    inst = Manager(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
                
            elif self.type == "rangeint":
                if check_type("rangeint", argumentos, scope):
                    inst = RangeInt(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
            elif self.type == "rangefloat":
                if check_type("rangefloat", argumentos, scope):
                    inst = RangeFloat(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
                
            elif self.type == "rangebool":
                if check_type("rangebool", argumentos, scope):
                    inst = RangeBool(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
            elif self.type == "rangechoice":
                if check_type("rangechoice", argumentos, scope):
                    inst = RangeChoice(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
            elif self.type == "game":
                if check_type("game", argumentos, scope):
                    inst = Partido(**argumentos)
                else:
                    raise Exception(f"Invalid arguments in {self.identifier}")
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
