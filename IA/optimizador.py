from IA.range import *
import copy
# from classes.partido import Partido
from utiles import es_mejor, mejor_equipo
from IA.estrategia import Estrategia


class Optimizador:
    def __init__(self, partido):
        self.partido = partido

    # def optimizar(self):
    #     mejores_variables = []  # aqui es donde se va a guardar por cada agente el diccionario de variables con los mejores valores y despues es lo que se va a devolver
    #     diccionario_variables = dict()
    #     for a in self.partido.eq1.jugadores_en_campo + self.partido.eq2.jugadores_en_campo + [self.partido.eq1.manager] + [self.partido.eq2.manager]:
    #         # guardamos las variables originales, o sea, los rangos, pues las vamos a ir modificando
    #         variables = dict()
    #         if a.estrategia != None:
    #             for v in a.estrategia.variables.keys():
    #                 if isinstance(a.estrategia.variables[v], Range):
    #                     variables[v] = copy.deepcopy(a.estrategia.variables[v])
    #                     a.estrategia.variables[v] = a.estrategia.variables[v].get_value(
    #                     )
    #             diccionario_variables[a] = copy.deepcopy(variables)

    #     for a in self.partido.eq1.jugadores_en_campo + self.partido.eq2.jugadores_en_campo + [self.partido.eq1.manager] + [self.partido.eq2.manager]:
    #         if a.estrategia != None:
    #             mejor_conj_valores = {}
    #             mejor_reporte = None
    #             for _ in range(1):
    #                 conj_actual_valores = copy.deepcopy(a.estrategia.variables)
    #                 for v in diccionario_variables[a].keys():
    #                     conj_actual_valores[v] = diccionario_variables[a][v].get_value(
    #                     )
    #                     a.estrategia.variables[v] = conj_actual_valores[v]
    #                 reporte_actual = copy.deepcopy(
    #                     self.partido).simular(True, 45)
    #                 if mejor_reporte == None or es_mejor(reporte_actual, mejor_reporte, a.equipo):
    #                     mejor_reporte = reporte_actual
    #                     mejor_conj_valores = conj_actual_valores

    #                 a.estrategia.variables = copy.deepcopy(mejor_conj_valores)
    #        # mejores_variables.append((a, a.estrategia.variables))
    #     # return mejores_variables

    # def _optimizar_agente(self, a):
    #     variables = dict()
    #     mejores_variables = dict()
    #     for v in a.estrategia.variables.keys():
    #         if isinstance(a.estrategia.variables[v], Range):
    #             variables[v] = a.estrategia.variables[v]
    #             a.estrategia.variables[v] = a.estrategia.variables[v].get_value(
    #             )

    #     for v in variables.keys():
    #         mejor_valor = None
    #         mejor_reporte = None
    #         for i in range(1):
    #             valor_actual = variables[v].get_value()
    #             a.estrategia.variables[v] = valor_actual
    #             reporte_actual = copy.deepcopy(self.partido).simular(True, 45)
    #             if mejor_reporte == None or es_mejor(reporte_actual, mejor_reporte):
    #                 mejor_reporte = reporte_actual
    #                 mejor_valor = valor_actual
    #         a.estrategia.variables[v] = mejor_valor

    #     return mejores_variables

    def torneo(self, eq, arbitros, n=2):
        if n < 0:
            raise Exception("El valor de n tiene que ser mayor que 0.")

        from classes.partido import Partido

        tournament = []
        for _ in range(2**n):
            eq1 = copy.deepcopy(eq)
            eq2 = copy.deepcopy(eq)

            eq1.nombre += "_1"
            eq2.nombre += "_2"

            self.asignar_valores(eq1)
            self.asignar_valores(eq2)

            tournament.append(Partido(eq1, eq2, arbitros, False))

        best = None
        while tournament:
            if len(tournament) == 1:
                best = mejor_equipo(tournament[0])
                break

            tournament_temp = []
            for i in range(0, len(tournament), 2):
                eq1 = copy.deepcopy(mejor_equipo(tournament[i]))
                eq2 = copy.deepcopy(mejor_equipo(tournament[i+1]))

                eq1.nombre += "_1"
                eq2.nombre += "_2"


                tournament_temp.append(
                    Partido(
                        eq1,     
                        eq2,
                        arbitros,
                        False
                    )
                )

            tournament = tournament_temp

        return best

    def asignar_valores(self, eq1):
        for a in eq1.jugadores + [eq1.manager]:
            # guardamos las variables originales, o sea, los rangos, pues las vamos a ir modificando
            variables = dict()
            if a.estrategia != None:
                for v in a.estrategia.variables.keys():
                    if isinstance(a.estrategia.variables[v], Range):
                        variables[v] = copy.deepcopy(a.estrategia.variables[v])
                        a.estrategia.variables[v] = a.estrategia.variables[v].get_value()
