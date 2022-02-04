from typing import List
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.Ast.attributeNode import AttributeNode
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.type import MyType
from utiles import create_dict
from utiles import check_type
from classes.jugador import Jugador
from classes.equipo import Equipo
from classes.portero import Portero
from classes.arbitro import Arbitro
from classes.manager import Manager


class Declaration(VariableNode):
    def __init__(self, identifier: str, var_type: str, args) -> None:
        super().__init__(identifier, var_type)
        self.args = args
    
    def checkSemantic(self, scope: Scope) -> bool:
        for arg in self.args:
            print(arg)
            if not arg.checkSemantic(scope):
                return False
        return scope.define_variables(self.identifier)

    def execute(self, scope: Scope):
        print("args:", self.args)
        if scope.check_var(self.identifier):  # prop = value, ej: name, Messi, tipo
            inst = None
            argumentos = create_dict(self.args, scope)
            if self.type == "player":
                #nombre, pos, list_prob, estrategia = None # player p1 = ([AttributeNode(name, Messi, string), AttribuNode(age, 20, int)])
                inst = Jugador(**argumentos)
                # if check_type("player", argumentos):
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
            scope.defineVar[self.identifier] = inst
            
    
    def __str__(self) -> str:
        string = ""
        for i in range(len(self.args)):
            string += str(self.args[i])
            if i != len(self.args) - 1:
                string += ", "
        return string

    

