import random
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
    if ultima_accion.tipo == config.ACT_PASE:
        acciones_actual = escoge_una(acciones_actual, config.ACT_INTERCEPTAR_BALON)
        intercepcion, _ = filter(lambda x: x.tipo == config.ACT_INTERCEPTAR_BALON, iterable=acciones_actual)

        if len(intercepcion) > 0:
            acciones_actual = elimina_tipo(acciones_actual, config.ACT_RECIBIR_BALON)         
            
    if estado == config.REANUDAR_PARTIDO: #cuando se marca un gol
        acciones_actual = escoge_una(acciones_actual, config.ACT_PASE)

    acciones_actual = escoge_una(acciones_actual, config.ACT_HACER_FALTA)

    acciones_actual = escoge_una(acciones_actual, config.ACT_SAQUE_BANDA)

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