import random
import numpy
from classes.arbitro import arbitro
from classes.player import Player
from acciones import *

# marcador = [0, 0]
# posiciones = ['DEL', 'MC', 'DEF', 'GK']

def simulacion_partido(t1, t2, arbitros):
    iter = 10
    largo = False
    pos_balon = random.randint(1, 2)

    equipo = t1 if pos_balon == 1 else t2

    jugador1 = iniciar_partido(equipo)

    while iter:
        d = numpy.random.choice(numpy.arange(0, 2), p=[0.85, 0.15]) if not largo else 0 
        if jugador1.posicion == 'GK':
            largo = False
            jugador2 = seleccionar_jugador_pase(jugador1, t1 if pos_balon == 1 else t2)
            result, jugador_pase_inter = realiza_un_pase(jugador1, jugador2, arbitros, t2 if pos_balon == 1 else t1)
            
            if result == "RECIBIDO": #si jugador2 recibio, entonces ahora el es el que tiene la opcion de pasar el balon o tirar a porteria
                jugador1 = jugador2
                jugador2 = None
                continue

            elif result == "LARGO": 
                jugador1 = jugador_pase_inter
                pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                largo = True

            elif result == "INTERCEPTADO": #pasa el balon al equipo contrario
                jugador1 = jugador_pase_inter
                pos_balon = 1 if pos_balon == 2 else 2
                equipo = t1 if pos_balon == 1 else t2
            
            elif result == "FALTA":
                # pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                jugador1 = elegir_jugador_para_sacar(equipo)
                print(f"{jugador1.nombre} saca luego de la falta")
                largo = True
        else:
            largo = False
            if d == 0: #el jugador del equipo que posee el balon realiza un pase
                jugador2 = seleccionar_jugador_pase(jugador1, t1 if pos_balon == 1 else t2)

                if jugador1.nombre == jugador2.nombre: #si es el propio jugador, significa q esta conduciendo el balon
                    print(f"{jugador1.nombre} se mantiene con el balon")
                    continue

                result, jugador_pase_inter = realiza_un_pase(jugador1, jugador2, arbitros, t2 if pos_balon == 1 else t1) #jugador1 le pasa el balon al jugador2

                if result == "RECIBIDO": #si jugador2 recibio, entonces ahora el es el que tiene la opcion de pasar el balon o tirar a porteria
                    jugador1 = jugador2
                    jugador2 = None
                    continue

                elif result == "LARGO":
                    jugador1 = jugador_pase_inter
                    pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                    largo = True

                elif result == "INTERCEPTADO": #pasa el balon al equipo contrario
                    jugador1 = jugador_pase_inter
                    pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                
                elif result == "FALTA":
                    # pos_balon, equipo = cambiar_equipo(pos_balon, t1, t2)
                    jugador1 = elegir_jugador_para_sacar(equipo)
                    print(f"{jugador1.nombre} saca luego de la falta")
                    largo = True

            else: #el jugador del equipo que posee el balon tira a porteria
                portero = t2[-1] if pos_balon == 1 else t1[-1]
                result = tiro_a_porteria_en_partido(jugador1, portero)

                if result == 'O':
                    print(f"{jugador1.nombre} marco GOOOOOOOOOOLLL")
                    if pos_balon == 1: marcador[0] += 1
                    else: marcador[1] += 1
                    
                    print(f"Marcado: equipo1: {marcador[0]} equipo2: {marcador[1]}")

                    pos_balon, equipo, jugador1 = reanudar_partido_pos_gol(pos_balon, t1, t2)
        iter -= 1


def print_sol(result):
    l1 = []
    l2 = []
    for i, j in result:
        l1.append(i)
        l2.append(j)
    print(l1)
    print(l2)

def main():
    arbitros = [arbitro('Arbitro Oscar', None, (0.2, 0.6, 0.15, 0.05))]

    t1_name = ['messi', 'fati', 'depay', 'de jong', 'neymar', 'ter stegen']
    t1_pos = [posiciones[0], posiciones[0], posiciones[0], posiciones[1], posiciones[2], posiciones[3]]
    t1_prob = [(0.75, 0.1, 0.8, 0.1, 0.1, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.7, 0.1, 0.75, 0.2, 0.05, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.58, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7,  0.69, 0.2, 0.1, 0.01), (0.73, 0.1, 0.81, 0.1, 0.09, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01)]

    t2_name = ['ronaldo', 'mbappe', 'ramos', 'benzema', 'alaba', 'courtoi']
    t2_pos = [posiciones[0], posiciones[0], posiciones[2], posiciones[1], posiciones[2], posiciones[3]]
    t2_prob = [(0.8, 0.1, 0.85, 0.1, 0.05, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.62, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.65, 0.2, 0.15, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.76, 0.11, 0.13, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.57, 0.1, 0.9, 0.5, 0.5, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01)]

    t1 = []
    t2 = []

    for i in range(len(t1_name)):
        t1.append(Player(t1_name[i], t1_pos[i], t1_prob[i]))
        t2.append(Player(t2_name[i], t2_pos[i], t2_prob[i]))

    simulacion_partido(t1, t2, arbitros)


if '__main__' == __name__:
    main()
