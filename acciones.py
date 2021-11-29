import numpy
import random
import time

marcador = [0, 0]
posiciones = ['DEL', 'MC', 'DEF', 'GK']



def iniciar_partido(t):
    temp_player_list = []
    for player in t:
        if player.posicion == 'DEL':
            temp_player_list.append(player)
    j1 = temp_player_list[random.randint(0, len(temp_player_list) - 1)]
    j2 = seleccionar_jugador_pase(j1, t, True)
    print('Inicia el partido...')
    print(f"{j1.nombre} le paso el balon a {j2.nombre}")
    return j2

def reanudar_partido_pos_gol(pos_balon, t1, t2):
    sec = random.uniform(1, 3)
    time.sleep(sec) #espera sec tiempo para reanuadar el partido
    pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
    temp_player_list = []
    for player in equipo:
        if player.posicion == 'DEL':
            temp_player_list.append(player)
    j1 = temp_player_list[random.randint(0, len(temp_player_list) - 1)]
    j2 = seleccionar_jugador_pase(j1, equipo, True)
    print(f"{j1.nombre} saca luego del gol y le pasa el balon a {j2.nombre}")
    return pos_balon, equipo, j2


def realiza_un_pase(lanzador, receptor, arbitros, t):
    pase_efect = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.pase_efectivo_p, lanzador.pase_efectivo_p])
    pase_intercep = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.pase_intercep_p, lanzador.pase_intercep_p])
    pase_largo = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.pase_largo_p, lanzador.pase_largo_p])    
    jugador_inter = None

    if pase_efect > pase_intercep:
        if pase_efect > pase_largo:
            print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}")
            return "RECIBIDO", jugador_inter
        else: 
            print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}, pero se fue de largo")
            jugador_inter = elegir_jugador_para_sacar(t) #jugador para sacar de banda
            print(f"{jugador_inter.nombre} va a sacar desde la banda")
            return "LARGO", jugador_inter
    else:
        jugador_comete_falta = numpy.random.choice(numpy.arange(0, 4), p=[lanzador.no_falta, lanzador.falta_leve, lanzador.falta_amarilla, lanzador.falta_roja])
        jugador_inter = interceptar_pase(lanzador.posicion, t)
        
        if jugador_comete_falta == 0: # no cometio falta
            print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}, pero fue interceptado por {jugador_inter.nombre}")
            return "INTERCEPTADO", jugador_inter 

        else: #cometio falta
            arbitro_principal = arbitros[0]
            return cometer_falta(lanzador, receptor, jugador_inter, arbitro_principal, t), None

def tiro_a_porteria_en_partido(lanzador, portero):
    j = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.gol_partido , lanzador.gol_partido])
    p = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.atajar_partido, portero.atajar_partido])

    if j > p:
        # print(f"{lanzador.nombre} marco")
        return 'O'
    elif j == p:
        j = random.randint(0, 2)
        if j == 0:
            print(f"{lanzador.nombre} fallo")
            return 'X' 
        else:
            # print(f"{lanzador.nombre} marco")
            return 'O'
    else:
        print(f"{lanzador.nombre} fallo")
        return 'X'

def seleccionar_jugador_pase(jugador1, t, reanudar_juego=False):
    index = -1
    if jugador1.posicion == 'DEL':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.5,   0.35,   0.1,  0.05])
    elif jugador1.posicion == 'MC':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.4,   0.3,   0.2,  0.1])
    elif jugador1.posicion == 'DEF':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.05,   0.4,   0.25,  0.3])
    elif jugador1.posicion == 'GK':
        index = numpy.random.choice(numpy.arange(0, 3), p=[0.3,   0.3,   0.4])

    jugador2 = obtener_jugador(posiciones[index], t)
    if jugador2 == jugador1 and reanudar_juego:
        seleccionar_jugador_pase(jugador1, t, reanudar_juego)
    
    return jugador2      

def interceptar_pase(pos, t):
    index = -1
    if pos == 'DEL':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.1,   0.3,   0.4,  0.2])
    elif pos == 'MC':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.2,   0.3,   0.3,  0.2])
    elif pos == 'DEF':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.3,   0.3,   0.2,  0.2])
    elif pos == 'GK':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.4,   0.3,   0.2,  0.1])
    else:
        print("POSICION NO REGISTRADA")

    return obtener_jugador(posiciones[index], t)

def elegir_jugador_para_sacar(t):
    index = numpy.random.choice(numpy.arange(0, 4), p=[0.1,   0.35,   0.5,  0.05])
    return obtener_jugador(posiciones[index], t)

def cometer_falta(lanzador, receptor, jugador_inter, arbitro, t):
    arbitro_tarjeta = numpy.random.choice(numpy.arange(0, 4), p=[arbitro.no_canta_falta, arbitro.declare_falta_leve, arbitro.tarjeta_amarilla, arbitro.tarjeta_roja])
            
    if arbitro_tarjeta == 0: # el arbitro decide no cantar la falta
        print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}, pero fue interceptado por {jugador_inter.nombre} (el arbitro decidio no cantar la falta)")
        return "INTERCEPTADO", jugador_inter
    else:
        print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}, pero {jugador_inter.nombre} trato de interceptarlo y cometio falta")

        if arbitro_tarjeta == 2: #saca tarjeta amarilla
            jugador_inter.cantidad_tarjetas += 1

            if jugador_inter.cantidad_tarjetas == 2:
                jugador_inter.cantidad_tarjetas = 0
                jugador_inter.fuera_del_partido = True
                # t.pop(jugador_inter.pos_array) da error el metodo obtener_jugador
                print(f"{jugador_inter.nombre} le sacaron tarjeta amarilla por segunda vez y lo expulsaron")
            else:
                print(f"{jugador_inter.nombre} le sacaron tarjeta amarilla")

        elif arbitro_tarjeta == 3: #saca tarjeta roja
            jugador_inter.cantidad_tarjetas = 0
            jugador_inter.fuera_del_partido = True
            # t.pop(jugador_inter.pos_array) da error el metodo obtener_jugador
            print(f"{jugador_inter.nombre} le sacaron tarjeta roja y lo expulsaron")
    
    return "FALTA"

def cambiar_equipo(pos_balon, t1, t2):
    if pos_balon == 1: #si el balon lo tiene t1, entonces pasa a t2
        equipo = t2
        pos_balon = 2
    else:
        equipo = t1
        pos_balon = 1
    
    return pos_balon, equipo

def obtener_jugador(pos_jugador, t):
    temp_list = []
    for item in t:
        if item.posicion == pos_jugador:
            temp_list.append(item)
    jugador_inter = temp_list[int(random.randint(0, len(temp_list)- 1))]
    return jugador_inter


def simulacion_penales(t1, t2):
    result = []
    index = 0
    win = 0

    while index < 5:
        r1 = tiro_a_porteria_en_penales(t1[index], t2[-1])
        win += 1 if r1 == 'O' else 0
        r2 = tiro_a_porteria_en_penales(t2[index], t1[-1])
        win -= 1 if r2 == 'O' else 0
        index += 1
        result.append((r1, r2))
    # print_sol(result)
    return win

def tiro_a_porteria_en_penales(lanzador, portero):
    j = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.gol_p, lanzador.gol_p])
    p = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.atajar_p, portero.atajar_p])

    if j > p:
        print(f"{lanzador.nombre} marco")
        return 'O'
    elif j == p:
        j = random.randint(0, 2)
        if j == 0:
            print(f"{lanzador.nombre} fallo")
            return 'X' 
        else:
            print(f"{lanzador.nombre} marco")
            return 'O'
    else:
        print(f"{lanzador.nombre} fallo")
        return 'X'

