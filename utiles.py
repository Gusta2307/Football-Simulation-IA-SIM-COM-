import random
import copy
# from compilacion.analisis_semantico.Ast.instructions.functionNode import FunctionNode
#from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode

from config import Config

config = Config()


def actualizar_scope(scope1, scope2):
    for k in scope1.defineVar.keys():
        if k in scope2.defineVar.keys():
            scope2.defineVar[k] = copy.deepcopy(scope1.defineVar[k])

    for k in scope1.defineFun.keys():
        if k in scope2.defineFun.keys():
            scope2.defineFun[k] = copy.deepcopy(scope1.defineFun[k])


def filter(funct, iterable):
    result_f = []
    result = []
    for item in iterable:
        if funct(item):
            result_f.append(item)
        else:
            result.append(item)
    return result_f, result


def analisis_acciones_list(acciones_actual, ultima_accion, estado):
    if ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_PASE:
        acciones_actual = escoge_una(
            acciones_actual, config.ACCIONES.JUGADOR.ACT_INTERCEPTAR_BALON)
        intercepcion, _ = filter(
            lambda x: x.tipo == config.ACCIONES.JUGADOR.ACT_INTERCEPTAR_BALON, iterable=acciones_actual)

        if len(intercepcion) > 0:
            acciones_actual = elimina_tipo(
                acciones_actual, config.ACCIONES.JUGADOR.ACT_RECIBIR_BALON)

    if estado == config.PARTIDO.ESTADO.REANUDAR_PARTIDO:  # cuando se marca un gol
        acciones_actual = escoge_una(
            acciones_actual, config.ACCIONES.JUGADOR.ACT_PASE)

    acciones_actual = escoge_una(
        acciones_actual, config.ACCIONES.JUGADOR.ACT_HACER_FALTA)

    acciones_actual = escoge_una(
        acciones_actual, config.ACCIONES.JUGADOR.ACT_SAQUE_BANDA)

    return acciones_actual


def escoge_una(acciones_actual, tipo):
    conjunto, acciones_actual = filter(
        lambda x: x.tipo == tipo, iterable=acciones_actual)
    if len(conjunto) >= 1:
        index = random.randint(0, len(conjunto) - 1)
        acciones_actual.append(conjunto[index])

    return acciones_actual


def elimina_tipo(acciones_actual, tipo):
    result = []
    for i in acciones_actual:
        if i.tipo != tipo:
            result.append(i)

    return result


def clasificar_jugadores(jugadores) -> dict:
    clasificacion = {}
    clasificacion['DEL'] = []
    clasificacion['MC'] = []
    clasificacion['DEF'] = []
    clasificacion['GK'] = []

    for jugador in jugadores:
        clasificacion[jugador.posicion].append(jugador)

    return clasificacion


def print_alineacion(esquema: list, jugadores):
    esquema.pop(len(esquema) - 1)
    esquema.reverse()
    result = f'Esquema de Juego: {esquema[0]}-{esquema[1]}-{esquema[2]} \n'

    for j in jugadores:
        result += f'{j.nombre}\n'

    # print(result)


# Devuelve si el reporte r1 es mejor que el reporte r2
def es_mejor(r1, r2, equipo):
    return r1._goles[equipo.nombre] > r2._goles[equipo.nombre]


def create_dict(args, scope):
    dic = {}
    for i in args:
        try:
            dic[i.name] = i.value.evaluate(scope)
        except:
            dic[i.identifier] = i.execute(scope)

    return dic

def create_dict_decl(args, scope):
    dic = {}
    for i in args:
        for args_aux in i.args:
            dic[i.identifier] = args_aux.value.evaluate(scope)
        # except:
        #     dic[i.identifier] = i.execute(scope)
        #     print(i.identifier)

    return dic


def check_type(tipo, argumentos, scope):
    from compilacion.comp_config import Config_C
    from compilacion.analisis_semantico.predefined import types
    config_C = Config_C()

    if tipo == "player":
        # nombre, pos, edad, list_prob, estrategia = None)
        if type(argumentos['name']) == config_C.Player.args["name"] and type(argumentos['country']) == config_C.Player.args["country"] and type(argumentos['pos']) == config_C.Player.args["pos"] and type(argumentos['age']) == config_C.Player.args['age'] and type(argumentos['list_prob']) == config_C.Player.args['list_prob']:
            if "st" in argumentos.keys():
                return type(argumentos['st']) == config_C.Player.args['st'] and len(argumentos.keys()) == 6
            else:
                return len(argumentos.keys()) == 5

    elif tipo == "manager":
        if type(argumentos['name']) == config_C.Manager_.args["name"] and type(argumentos['country']) == config_C.Manager_.args["country"] and type(argumentos['age']) == config_C.Manager_.args['age'] and type(argumentos['experience']) == config_C.Manager_.args['experience']:
            # if "st" in argumentos.keys():
            #     return type(argumentos['st']) == config_C.Manager_.args['st'] and len(argumentos.keys()) == 6
            # else:
            return len(argumentos.keys()) == 4

    elif tipo == "referee":
        if type(argumentos['name']) == config_C.Referee.args["name"] and type(argumentos['country']) == config_C.Referee.args["country"] and type(argumentos['age']) == config_C.Referee.args['age'] and type(argumentos['experience']) == config_C.Referee.args['experience'] and type(argumentos['list_prob']) == config_C.Referee.args['list_prob']:
            # if "st" in argumentos.keys():
            #     return type([argumentos['st'].type]) == config_C.Referee.args['st'] and len(argumentos.keys()) == 6
            # else:
            return len(argumentos.keys()) == 5

    elif tipo == "goalkeeper":
        if type(argumentos['name']) == config_C.Goalkeeper.args["name"] and type(argumentos['country']) == config_C.Goalkeeper.args["country"] and type(argumentos['age']) == config_C.Goalkeeper.args['age'] and type(argumentos['list_prob']) == config_C.Goalkeeper.args['list_prob'] and type(argumentos['goalkeeper_prob']) == config_C.Goalkeeper.args['goalkeeper_prob']:
            if "st" in argumentos.keys():
                return type(argumentos['st']) == config_C.Goalkeeper.args['st'] and len(argumentos.keys()) == 7
            else:
                return len(argumentos.keys()) == 6

    elif tipo == "team":
        if type(argumentos['name']) == config_C.Team.args["name"] and type(argumentos['country']) == config_C.Team.args["country"] and type(argumentos['coach']) == config_C.Team.args['manager'] and type(argumentos['players']) == config_C.Team.args['players']:
            return len(argumentos.keys()) == 4

    elif tipo == "game":
        if type(argumentos['eq1']) == config_C.Game.args["eq1"] and type(argumentos['eq2']) == config_C.Game.args["eq2"] and type(argumentos['referees']) == config_C.Game.args['referees']:
            return len(argumentos.keys()) == 3

    elif tipo == "rangeint":
        if type(argumentos['li']) == config_C.RangeInt.args['li'] and type(argumentos['ls']) == config_C.RangeInt.args["ls"]:
            if "distribution" in argumentos.keys():
                return scope.check_fun(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 3
            else:
                return len(argumentos.keys()) == 2

    elif tipo == "rangefloat":
        if type(argumentos['li']) == config_C.RangeFloat.args['li'] and type(argumentos['ls']) == config_C.RangeFloat.args["ls"]:
            if "distribution" in argumentos.keys():
                return scope.check_fun(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 3
            else:
                return len(argumentos.keys()) == 2

    elif tipo == "rangechoice":
        if type(argumentos['valores']) == config_C.RangeChoice.args["valores"]:
            if "distribution" in argumentos.keys():
                return scope.check_fun(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 2
            else:
                return len(argumentos.keys()) == 1

    elif tipo == "rangebool":
        if "distribution" in argumentos.keys():
            return scope.check_fun(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 1
        else:
            return len(argumentos.keys()) == 0


def mejor_equipo(partido):
    s = partido.simular(True, 45)
    jugadores = []
    from classes.equipo import Equipo
    for j in range(len(partido.eq1.jugadores)):
        jugadores.append(mejor_rendimiento(partido.eq1.jugadores[j], partido.eq2.jugadores[j]))
    
    eq_name = partido.eq1.nombre[:len(partido.eq1.nombre) - 2]
    return Equipo(eq_name, partido.eq1.pais, partido.eq1.manager, jugadores)
            
def mejor_rendimiento(j1, j2):
    count_j1, count_j2 = 0, 0
    for prop in config.RENDIMIENTO.ASPECTOS.keys():
        count_j1 += getattr(j1.reporte, '_'+prop)*config.RENDIMIENTO.ASPECTOS[prop]
        count_j2 += getattr(j2.reporte, '_'+prop)*config.RENDIMIENTO.ASPECTOS[prop]
    
    return j1 if count_j1 >= count_j2 else j2
