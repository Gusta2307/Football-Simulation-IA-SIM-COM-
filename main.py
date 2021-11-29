import random
import numpy
from classes.arbitro import arbitro
from classes.player import Player
from acciones import *

# marcador = [0, 0]
# posiciones = ['DEL', 'MC', 'DEF', 'GK']

def simulacion_partido(t1, t2, arbitros):
    iter = 100
    largo = False
    pos_balon = random.randint(1, 2)
    equipo = t1 if pos_balon == 1 else t2

    jugador1 = iniciar_partido(equipo)

    while iter:
        d = numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05]) if not largo else 0 

        if jugador1.posicion == 'GK':
            jugador2 = seleccionar_jugador_pase(jugador1, equipo)
            resultado, jugador_pase_inter = realiza_un_pase(jugador1, jugador2, arbitros, t2 if pos_balon == 1 else t1)
            jugador1, equipo, pos_balon, largo = analizar_result_pase(resultado, jugador1, jugador2, jugador_pase_inter, pos_balon, t1, t2)
            continue
        
        if d == 0: #el jugador del equipo que posee el balon realiza un pase
            jugador2 = seleccionar_jugador_pase(jugador1, equipo)
            if jugador1 == jugador2:
                print(f"{jugador1.nombre} se mantiene con el balon")
                continue

            resultado, jugador_pase_inter = realiza_un_pase(jugador1, jugador2, arbitros, t2 if pos_balon == 1 else t1) #jugador1 le pasa el balon al jugador2
            jugador1, equipo, pos_balon, largo = analizar_result_pase(resultado, jugador1, jugador2, jugador_pase_inter, pos_balon, t1, t2)
        
        else: #el jugador del equipo que posee el balon tira a porteria
            portero = t2[-1] if pos_balon == 1 else t1[-1]
            resultado, jugador_a_sacar = tiro_a_porteria_en_partido(jugador1, portero, equipo, t2 if pos_balon == 1 else t1)
            jugador1, equipo, pos_balon, largo = analizar_result_tiro_a_porteria(resultado, jugador1, jugador_a_sacar, pos_balon, t1, t2)
            
        iter -= 1


def print_sol(resultado):
    l1 = []
    l2 = []
    for i, j in resultado:
        l1.append(i)
        l2.append(j)
    print(l1)
    print(l2)


def main():
    arbitros = [arbitro('Arbitro Oscar', None, (0.2, 0.6, 0.15, 0.05))]

    t1_name = ['messi', 'fati', 'depay', 'de jong', 'neymar', 'ter stegen']
    t1_pos = [posiciones[0], posiciones[0], posiciones[0], posiciones[1], posiciones[2], posiciones[3]]
    t1_prob = [(0.75, 0.1, 0.8, 0.1, 0.1, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.7, 0.1, 0.75, 0.2, 0.05, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.58, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7,  0.69, 0.2, 0.1, 0.01), (0.73, 0.1, 0.81, 0.1, 0.09, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3)]

    t2_name = ['ronaldo', 'mbappe', 'ramos', 'benzema', 'alaba', 'courtoi']
    t2_pos = [posiciones[0], posiciones[0], posiciones[2], posiciones[1], posiciones[2], posiciones[3]]
    t2_prob = [(0.8, 0.1, 0.85, 0.1, 0.05, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.62, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.65, 0.2, 0.15, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.76, 0.11, 0.13, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.57, 0.1, 0.9, 0.5, 0.5, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3)]

    t1 = []
    t2 = []
    length = len(t1_name)

    for i in range(length):
        t1.append(Player(t1_name[i], t1_pos[i], t1_prob[i]))
        t2.append(Player(t2_name[i], t2_pos[i], t2_prob[i]))

    simulacion_partido(t1, t2, arbitros)


if '__main__' == __name__:
    main()
