from classes.agente import Agente
from act.act_manager.escoger_alineacion import Escoger_alineacion
from act.act_manager.hacer_cambio import Hacer_cambio
from act.default import Default
import numpy
from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration

from config import Config
config = Config()

class Manager(Agente, Declaration):
    def __init__(self, nombre, pais, experiencia, edad) -> None:
        self.nombre = nombre
        self.pais = pais
        self.experiencia = experiencia
        self.edad = edad
        self.equipo = None

        self.acciones = self.acciones_dict()


    def acciones_dict(self):
        return {
            'ESCOGER_ALINEACION': (Escoger_alineacion(self), 0.5),
            'HACER_CAMBIO': (Hacer_cambio(self), 0.1),
        }
    
    def escoger_accion(self, partido):
        acciones_posibles = list(filter(lambda x: x[0].precondicion(partido), self.acciones.values()))

        temp_p = []
        for item in acciones_posibles:
            temp_p.append(item[1]/len(acciones_posibles))

        temp_p.append(1 - sum(temp_p))
        act = numpy.random.choice(numpy.arange(0, len(temp_p)), p=temp_p)
        
        return Default(self) if act == len(temp_p) - 1 else acciones_posibles[act][0]
    