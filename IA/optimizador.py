from IA.range import *
import copy
# from classes.partido import Partido
from utiles import es_mejor
from IA.estrategia import Estrategia
class Optimizador:
    def __init__(self, partido):
        self.partido = partido

    
    def optimizar(self):
        mejores_variables = [] #aqui es donde se va a guardar por cada agente el diccionario de variables con los mejores valores y despues es lo que se va a devolver
        diccionario_variables = dict()
        for a in self.partido.eq1.jugadores_en_campo + self.partido.eq2.jugadores_en_campo:
            variables = dict() #guardamos las variables originales, o sea, los rangos, pues las vamos a ir modificando
            for v in a.estrategia.variables.keys():
                if isinstance(a.estrategia.variables[v], Range):
                    variables[v] = copy.deepcopy(a.estrategia.variables[v])
                    a.estrategia.variables[v] = a.estrategia.variables[v].get_value()  
            
            diccionario_variables[a] = copy.deepcopy(variables)


        for a in self.partido.eq1.jugadores_en_campo + self.partido.eq2.jugadores_en_campo:
            # for v in diccionario_variables[a].keys():
            #     mejor_valor = None
            #     mejor_reporte = None
            #     for i in range(1):
            #         valor_actual = diccionario_variables[a][v].get_value()
            #         a.estrategia.variables[v] = valor_actual
            #         reporte_actual= copy.deepcopy(self.partido).simular(True)
            #         if mejor_reporte == None or es_mejor(reporte_actual, mejor_reporte, a.equipo):
            #             mejor_reporte = reporte_actual
            #             mejor_valor = valor_actual

            #     a.estrategia.variables[v] = mejor_valor
            
            mejor_conj_valores = {}
            mejor_reporte = None
            for _ in range(1):
                conj_actual_valores = copy.deepcopy(a.estrategia.variables)
                for v in diccionario_variables[a].keys():
                    conj_actual_valores[v] = diccionario_variables[a][v].get_value()
                    a.estrategia.variables[v] = conj_actual_valores[v]
                reporte_actual= copy.deepcopy(self.partido).simular(True)
                if mejor_reporte == None or es_mejor(reporte_actual, mejor_reporte, a.equipo):
                    mejor_reporte = reporte_actual
                    mejor_conj_valores = conj_actual_valores

                a.estrategia.variables = copy.deepcopy(mejor_conj_valores)

    def _optimizar_agente(self, a):
        variables = dict()
        mejores_variables = dict()
        for v in a.estrategia.variables.keys():
            if isinstance(a.estrategia.variables[v], Range):
                variables[v] = a.estrategia.variables[v]
                a.estrategia.variables[v] = a.estrategia.variables[v].get_value()
            
        for v in variables.keys():
            mejor_valor = None
            mejor_reporte = None
            for i in range(1):
                valor_actual = variables[v].get_value()
                a.estrategia.variables[v] = valor_actual
                reporte_actual= copy.deepcopy(self.partido).simular(True)
                if mejor_reporte == None or es_mejor(reporte_actual, mejor_reporte):
                    mejor_reporte = reporte_actual
                    mejor_valor = valor_actual
            a.estrategia.variables[v] = mejor_valor 
        
        print("#"*50)
        return mejores_variables
            
    




    
    