import random
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from config import Config


config = Config()


def filter(funct, iterable):
    result_f = []
    result = []
    for item in iterable:
        if funct(item):
            result_f.append(item)
        else:
            result.append(item)
    return result_f, result

def analisis_acciones_list(acciones_actual, ultima_accion,estado):
    if ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_PASE:
        acciones_actual = escoge_una(acciones_actual, config.ACCIONES.JUGADOR.ACT_INTERCEPTAR_BALON)
        intercepcion, _ = filter(lambda x: x.tipo == config.ACCIONES.JUGADOR.ACT_INTERCEPTAR_BALON, iterable=acciones_actual)

        if len(intercepcion) > 0:
            acciones_actual = elimina_tipo(acciones_actual, config.ACCIONES.JUGADOR.ACT_RECIBIR_BALON)         
            
    if estado == config.PARTIDO.ESTADO.REANUDAR_PARTIDO: #cuando se marca un gol
        acciones_actual = escoge_una(acciones_actual, config.ACCIONES.JUGADOR.ACT_PASE)

    acciones_actual = escoge_una(acciones_actual, config.ACCIONES.JUGADOR.ACT_HACER_FALTA)

    acciones_actual = escoge_una(acciones_actual, config.ACCIONES.JUGADOR.ACT_SAQUE_BANDA)

    return acciones_actual
    
def escoge_una(acciones_actual, tipo):
    conjunto, acciones_actual = filter(lambda x: x.tipo == tipo, iterable=acciones_actual)
    if len(conjunto) >= 1:
            index = random.randint(0, len(conjunto) - 1)
            acciones_actual.append(conjunto[index])
    
    return acciones_actual

def elimina_tipo (acciones_actual, tipo):
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

def print_alineacion(esquema:list, jugadores):
    esquema.pop(len(esquema) - 1)
    esquema.reverse()
    result = f'Esquema de Juego: {esquema[0]}-{esquema[1]}-{esquema[2]} \n'

    for j in jugadores:
        result += f'{j.nombre}\n'
    
    print(result)


#Devuelve si el reporte r1 es mejor que el reporte r2
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

def check_type(tipo, argumentos, scope):
    from compilacion.comp_config import Config_C
    config_C = Config_C()

    if tipo == "player":
        #nombre, pos, edad, list_prob, estrategia = None)
        if argumentos['name'].type == config_C.Player["name"].type and argumentos['country'].type == config_C.Player["country"].type and argumentos['pos'].type == config_C.Player["pos"] and argumentos['age'].type == config_C.Player['age'] and argumentos['list_prob'].type == config_C.Player['list_prob']:
            if "estrategy" in argumentos.keys():
                return argumentos['estrategy'].type == config_C.Player['estrategy'] and len(argumentos.keys()) == 5
            else:
                return len(argumentos.keys()) == 4

    elif tipo == "manager":
        if argumentos['name'].type == config_C.Manager_["name"].type and argumentos['country'].type == config_C.Manager_["country"] and argumentos['age'].type == config_C.Manager_['age'] and argumentos['experience'].type == config_C.Manager_['experience']:
            if "estrategy" in argumentos.keys():
                return argumentos['estrategy'].type == config_C.Manager_['estrategy'] and len(argumentos.keys()) == 5
            else:
                return len(argumentos.keys()) == 4

    elif tipo == "referee":
        if argumentos['name'].type == config_C.Referee["name"].type and argumentos['country'].type == config_C.Referee["country"] and argumentos['age'].type == config_C.Referee['age'] and argumentos['experience'].type == config_C.Referee['experience'] and argumentos['list_prob'].type == config_C.Referee['list_prob']:
            if "estrategy" in argumentos.keys():
                return argumentos['estrategy'].type == config_C.Referee['estrategy'] and len(argumentos.keys()) == 6
            else:
                return len(argumentos.keys()) == 5

    elif tipo == "goalkeeper":
        if argumentos['name'].type == config_C.Goalkeeper["name"].type and argumentos['country'].type == config_C.Goalkeeper["country"] and argumentos['age'].type == config_C.Goalkeeper['age'] and argumentos['list_prob'].type == config_C.Goalkeeper['list_prob'] and argumentos['goalkeeper_prob'].type == config_C.Goalkeeper['goalkeeper_prob']:
            if "estrategy" in argumentos.keys():
                return argumentos['estrategy'].type == config_C.Goalkeeper['estrategy'] and len(argumentos.keys()) == 7
            else:
                return len(argumentos.keys()) == 6

    elif tipo == "team":
        if argumentos['name'].type == config_C.Team["name"].type and argumentos['country'].type == config_C.Team["country"] and argumentos['age'].type == config_C.Team['age'] and argumentos['list_prob'].type == config_C.Team['list_prob'] and argumentos['goalkeeper_prob'].type == config_C.Team['goalkeeper_prob']:
            if "estrategy" in argumentos.keys():
                return argumentos['estrategy'].type == config_C.Team['estrategy'] and len(argumentos.keys()) == 7
            else:
                return len(argumentos.keys()) == 6


    elif tipo == "rangeint":
        if argumentos['li'].type == config_C.Team["li"].type and argumentos['ls'].type == config_C.Team["ls"]:
            if "distribution" in argumentos.keys() : 
                return scope.check_function(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 3
            else:
                return len(argumentos.keys()) == 2

    elif tipo == "rangefloat":
        if argumentos['li'].type == config_C.Team["li"].type and argumentos['ls'].type == config_C.Team["ls"]:
            if "distribution" in argumentos.keys() : 
                return scope.check_function(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 3
            else:
                return len(argumentos.keys()) == 2

    elif tipo == "rangechoice":
        if argumentos['valores'].type == config_C.Team["valores"].type:
            if "distribution" in argumentos.keys() :
                return scope.check_function(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 2
            else:
                return len(argumentos.keys()) == 1   

    elif tipo == "rangebool":
        if "distribution" in argumentos.keys() :
                return scope.check_function(argumentos["distribution"].value.identifier, 1) and len(argumentos.keys()) == 1
        else:
            return len(argumentos.keys()) == 0

