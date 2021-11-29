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

def analizar_result_pase(resultado, jugador1, jugador2, jugador_pase_inter, pos_balon, t1, t2):
    equipo = t1 if pos_balon == 1 else t2
    largo = True if resultado == "LARGO" or resultado == "FALTA" else False

    if resultado == "RECIBIDO": #si jugador2 recibio, entonces ahora el es el que tiene la opcion de pasar el balon o tirar a porteria
        jugador1 = jugador2
        jugador2 = None
    
    elif resultado == "LARGO" or resultado == "INTERCEPTADO":
        jugador1 = jugador_pase_inter
        pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)

    elif resultado == "FALTA":
        jugador1 = elegir_jugador_para_sacar(equipo)
        print(f"{jugador1.nombre} saca luego de la falta")

    return jugador1, equipo, pos_balon, largo

def analizar_result_tiro_a_porteria(resultado, jugador1, jugador_a_sacar, pos_balon, t1, t2):
    equipo = t1 if pos_balon == 1 else t2
    largo = False if resultado == 'O' else True

    if resultado == 'O':
        print(f"{jugador1.nombre} marco GOOOOOOOOOOLLL")
        if pos_balon == 1: marcador[0] += 1
        else: marcador[1] += 1
        
        print(f"Marcado: equipo1: {marcador[0]} equipo2: {marcador[1]}")
        pos_balon, equipo, jugador1 = reanudar_partido_pos_gol(pos_balon, t1, t2)

    else:
        jugador1 = jugador_a_sacar

        if resultado == "NO_REBOTE" or resultado == "REBOTE_JUGADOR_CONTRARIO":
            pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)

        elif resultado == "TIRO_ESQUINA":
            pass

    return jugador1, equipo, pos_balon, largo


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

def tiro_a_porteria_en_partido(lanzador, portero, equipo, equipo_contrario):
    jugador_gol = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.gol_partido , lanzador.gol_partido])
    portero_ataja = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.atajar_partido, portero.atajar_partido])
    jugador_a_sacar = None

    if jugador_gol > portero_ataja:
        return 'O', jugador_a_sacar
    else:
        portero_rebote = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.rebote , portero.rebote])
        
        if portero_rebote == 0: #el portero atajo el balon y no hubo rebote
            print(f"{lanzador.nombre} tiro a porteria, pero el portero {portero.nombre} atajo el balon sin rebote")
            return "NO_REBOTE", portero
        else: #hubo rebote
            portero_tipo_rebote = numpy.random.choice(numpy.arange(0, 3), p=[portero.rebote_banda , portero.rebote_linea_final, portero.rebote_jugador])
            
            if portero_tipo_rebote == 0: #el rebote salio por la banda y hay saque de banda
                print(f"{lanzador.nombre} tiro a porteria, pero el portero {portero.nombre} saco el balon por la banda")
                jugador_a_sacar = elegir_jugador_para_sacar(equipo) #jugador para sacar de banda
                print(f"{jugador_a_sacar.nombre} va a sacar desde la banda")
                return "POR_BANDA", jugador_a_sacar

            elif portero_tipo_rebote == 1: #el rebote salio por la linea final y hay tiro de esquina
                #Implementar tiro de esquina
                jugador_a_sacar = portero
                print(f"{lanzador.nombre} tiro a porteria, pero el portero {portero.nombre} saco el balon por la linea final")
                return "TIRO_ESQUINA", jugador_a_sacar

            elif portero_tipo_rebote == 2: #el rebote le cayo a un jugador, ya sea el portero mismo, un jugador de t1 o de t2
                recibir_rebote = numpy.random.choice(numpy.arange(0, 3), p=[0.3, 0.4 , 0.3])
                
                if recibir_rebote == 0: #el rebote le cae al propio portero
                    print(f"{lanzador.nombre} tiro a porteria, pero el portero {portero.nombre} recibio el rebote")
                    jugador_a_sacar = portero

                elif recibir_rebote == 1: #el rebote le cae a un jugador del mismo equipo q el portero
                    jugador_a_sacar = elegir_jugador_para_sacar(equipo)
                    print(f"{lanzador.nombre} tiro a porteria, pero el portero rechazo y {jugador_a_sacar.nombre} recibio el rebote")

                elif recibir_rebote == 2: #el rebote le cae a un jugador del equipo contrario al del portero
                    jugador_a_sacar = elegir_jugador_para_sacar(equipo_contrario)
                    print(f"{lanzador.nombre} tiro a porteria, pero el portero rechazo y {jugador_a_sacar.nombre} (del equipo contrario) recibio el rebote")
                    return "REBOTE_JUGADOR_CONTRARIO", jugador_a_sacar

                return "REBOTE_JUGADOR", jugador_a_sacar


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
        return seleccionar_jugador_pase(jugador1, t, reanudar_juego)
    
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

        if arbitro_tarjeta == 3: #saca tarjeta roja
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
    jugador_gol = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.gol_p, lanzador.gol_p])
    p = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.atajar_p, portero.atajar_p])

    if jugador_gol > p:
        print(f"{lanzador.nombre} marco")
        return 'O'
    elif jugador_gol == p:
        jugador_gol = random.randint(0, 2)
        if jugador_gol == 0:
            print(f"{lanzador.nombre} fallo")
            return 'X' 
        else:
            print(f"{lanzador.nombre} marco")
            return 'O'
    else:
        print(f"{lanzador.nombre} fallo")
        return 'X'

