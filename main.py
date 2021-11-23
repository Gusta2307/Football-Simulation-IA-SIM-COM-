import random
import numpy
import time
from classes.player import Player


def simulacion(t1, t2):
    result = []
    index = 0
    win = 0
    while index < 5:
        r1 = check(t1[index], t2[-1])
        win += 1 if r1 == 'O' else 0
        r2 = check(t2[index], t1[-1])
        win -= 1 if r2 == 'O' else 0
        index += 1
        result.append((r1, r2))
    # print_sol(result)
    return win

def check(lanzador, portero):
    #j = random.random()
    #p = random.random()

    j = numpy.random.choice(numpy.arange(0, 2), p=[1 - lanzador.gol_p, lanzador.gol_p])
    p = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.atajar_p, portero.atajar_p])


    #if lanzador.gol_p + j > 1:
    #    if portero.atajar_p + p > 1:
    #        # print(f"{portero.nombre} atajo")
    #        return 'X'
    #    else:
    #        # print(f"{lanzador.nombre} marco")
    #        return 'O'
    #else:
    #    # print(f"{lanzador.nombre} fallo")
    #    return 'X'

    if j > p:
        # print(f"{lanzador.nombre} marco")
        return 'O'
    elif j == p:
        j = random.randint(0, 2)
        if j == 0:
            # print(f"{lanzador.nombre} fallo")
            return 'X' 
        else:
            # print(f"{lanzador.nombre} marco")
            return 'O'
    else:
        # print(f"{lanzador.nombre} fallo")
        return 'X'

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
    t1_prob = [(0.75, 0.1), (0.6, 0.1), (0.7, 0.1), (0.58, 0.1), (0.73, 0.1), (0.1, 0.6)]

    t2_name = ['ronaldo', 'mbappe', 'ramos', 'benzema', 'alaba', 'coutua']
    t2_prob = [(0.8, 0.1), (0.62, 0.1), (0.6, 0.1), (0.6, 0.1), (0.57, 0.1), (0.1, 0.6)]

    t1 = []
    t2 = []

    for i in range(len(t1_name)):
        t1.append(Player(t1_name[i], "ALGO", t1_prob[i][0], t1_prob[i][1]))
        t2.append(Player(t2_name[i], "ALGO", t2_prob[i][0], t2_prob[i][1]))

    n = 10000
    win_t1, win_t2, empate = 0, 0, 0
    while n != 0:
        r = simulacion(t1, t2)
        if r == 0:
            empate += 1
        elif r > 0:
            win_t1 += 1
        else:
            win_t2 += 1

        n -= 1

    print("Victorias t1", win_t1)
    print("Victorias t2", win_t2)
    print("Empates", empate)


if '__main__' == __name__:
    main()
