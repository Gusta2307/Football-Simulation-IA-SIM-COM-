import random
import numpy
import time
from classes.player import Player


def simulacion_penales(t1, t2):
    result = []
    index = 0
    win = 0

    while index < 5:
        r1 = tiro_a_porteria(t1[index], t2[-1])
        win += 1 if r1 == 'O' else 0
        r2 = tiro_a_porteria(t2[index], t1[-1])
        win -= 1 if r2 == 'O' else 0
        index += 1
        result.append((r1, r2))
    # print_sol(result)
    return win

def tiro_a_porteria(lanzador, portero):
    #j = random.random()
    #p = random.random()

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

def simulacion_pase_porteria(t1, t2):
    largo = False
    pos_balon = random.randint(1, 2)
    
    equipo = t1

    if pos_balon == 2:
        equipo = t2
    
    iter = 20
    pos_jugador1 = random.randint(0, len(equipo) - 2) #jugador q posee el balon al iniciar el partido
    jugador1 = equipo[pos_jugador1]

    while iter >= 0:
        if not largo:
            d = random.randint(0, 1)
        else:
            d = 0

        if jugador1.posicion == 'GK':
            #pos_jugador2 = random.randint(0, len(equipo) - 2) #jugador q debe recibir el pase
            largo = False
            jugador2 = seleccionar_jugador_pase(jugador1, t1 if pos_balon == 1 else t2)
            result, jugador_pase_inter = realiza_un_pase(jugador1, jugador2, t2 if pos_balon == 1 else t1)
            
            if result == "RECIBIDO": #si jugador2 recibio, entonces ahora el es el que tiene la opcion de pasar el balon o tirar a porteria
                jugador1 = jugador2
                jugador2 = None
                continue

            elif result == "LARGO": 
                pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                jugador1 = jugador_pase_inter
                largo = True

            elif result == "INTERCEPTADO": #pasa el balon al equipo contrario
                pos_balon = 1 if pos_balon == 2 else 2
                jugador1 = jugador_pase_inter
                equipo = t1 if pos_balon == 1 else t2
        else:
            largo = False
            if d == 0: #el jugador del equipo que posee el balon realiza un pase
                # pos_jugador2 = random.randint(0, len(equipo) - 2) #jugador q debe recibir el pase
                # jugador2 = equipo[pos_jugador2]
                jugador2 = seleccionar_jugador_pase(jugador1, t1 if pos_balon == 1 else t2)
                if jugador1.nombre == jugador2.nombre: #si es el propio jugador, significa q esta conduciendo el balon
                    print(f"{jugador1.nombre} se mantiene con el balon")
                    continue

                result, jugador_pase_inter = realiza_un_pase(jugador1, jugador2, t2 if pos_balon == 1 else t1) #jugador1 le pasa el balon al jugador2

                if result == "RECIBIDO": #si jugador2 recibio, entonces ahora el es el que tiene la opcion de pasar el balon o tirar a porteria
                    jugador1 = jugador2
                    jugador2 = None
                    continue

                elif result == "LARGO":
                    pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                    jugador1 = jugador_pase_inter
                    largo = True

                elif result == "INTERCEPTADO": #pasa el balon al equipo contrario
                    pos_balon = 1 if pos_balon == 2 else 2
                    jugador1 = jugador_pase_inter
                    equipo = t1 if pos_balon == 1 else t2

            else: #el jugador del equipo que posee el balon tira a porteria
                portero = t2[-1] if pos_balon == 1 else t1[-1]
                result = tiro_a_porteria(jugador1, portero)

                if result == 'O':
                    pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                    pos_jugador1 = random.randint(0, len(equipo) - 2) #jugador q intercepto el balon
                    jugador1 = equipo[pos_jugador1]
        iter -= 1

def realiza_un_pase(lanzador, receptor, t):
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
            jugador_inter = sacar_de_banda(t)
            print(f"{jugador_inter.nombre} va a sacar desde la banda")
            return "LARGO", jugador_inter
    else:
        #Aqui va lo de definir que jugador tiene mas probabilidad de interceptar el pase
        jugador_inter = interceptar_pase(lanzador.posicion, t)
        print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}, pero fue interceptado por {jugador_inter.nombre}")
        return "INTERCEPTADO", jugador_inter 

posicion = ['DEL', 'MC', 'DEF', 'GK']

def seleccionar_jugador_pase(jugador1, t):
    index = -1
    if jugador1.posicion == 'DEL':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.45,   0.3,   0.2,  0.05])
    elif jugador1.posicion == 'MC':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.3,   0.3,   0.3,  0.1])
    elif jugador1.posicion == 'DEF':
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.1,   0.3,   0.3,  0.3])
    elif jugador1.posicion == 'GK':
        index = numpy.random.choice(numpy.arange(0, 3), p=[0.3,   0.3,   0.4])

    return obtener_jugador(posicion[index], t)

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

    return obtener_jugador(posicion[index], t)

def sacar_de_banda(t):
    index = numpy.random.choice(numpy.arange(0, 4), p=[0.1,   0.35,   0.5,  0.05])
    return obtener_jugador(posicion[index], t)

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


def print_sol(result):
    l1 = []
    l2 = []
    for i, j in result:
        l1.append(i)
        l2.append(j)
    print(l1)
    print(l2)


def main():
    posiciones = ['DEL', 'MC', 'DEF', 'GK']

    t1_name = ['messi', 'fati', 'depay', 'de jong', 'neymar', 'ter stegen']
    t1_pos = [posiciones[0], posiciones[0], posiciones[0], posiciones[1], posiciones[2], posiciones[3]]
    t1_prob = [(0.75, 0.1, 0.8, 0.1, 0.1), (0.6, 0.1, 0.7, 0.1, 0.2), (0.7, 0.1, 0.75, 0.2, 0.05), (0.58, 0.1, 0.7, 0.2, 0.1), (0.73, 0.1, 0.81, 0.1, 0.09), (0.1, 0.6, 0.8, 0.1, 0.1)]

    t2_name = ['ronaldo', 'mbappe', 'ramos', 'benzema', 'alaba', 'courtoi']
    t2_pos = [posiciones[0], posiciones[0], posiciones[2], posiciones[1], posiciones[2], posiciones[3]]
    t2_prob = [(0.8, 0.1, 0.85, 0.1, 0.05), (0.62, 0.1, 0.7, 0.2, 0.1), (0.6, 0.1, 0.65, 0.2, 0.15), (0.6, 0.1, 0.76, 0.11, 0.13), (0.57, 0.1, 0.9, 0.5, 0.5), (0.1, 0.6, 0.8, 0.1, 0.1)]

    t1 = []
    t2 = []

    for i in range(len(t1_name)):
        t1.append(Player(t1_name[i], t1_pos[i], t1_prob[i][0], t1_prob[i][1], t1_prob[i][2], t1_prob[i][3], t1_prob[i][4]))
        t2.append(Player(t2_name[i], t2_pos[i], t2_prob[i][0], t2_prob[i][1], t2_prob[i][2], t2_prob[i][3], t2_prob[i][4]))


    simulacion_pase_porteria(t1, t2) #pasar balon
    # n = 10000
    # win_t1, win_t2, empate = 0, 0, 0
    # while n != 0:
    #     r = simulacion_penales(t1, t2)
    #     if r == 0:
    #         empate += 1
    #     elif r > 0:
    #         win_t1 += 1
    #     else:
    #         win_t2 += 1

    #     n -= 1

    # print("Victorias t1", win_t1)
    # print("Victorias t2", win_t2)
    # print("Empates", empate)


if '__main__' == __name__:
    main()
