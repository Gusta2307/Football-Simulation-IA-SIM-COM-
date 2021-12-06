from classes.equipo import Equipo
from classes.arbitro import arbitro
from classes.jugador import Jugador
from classes.partido import Partido
from classes.portero import Portero
from config import Config
config = Config()

def main():
    arbitros = [arbitro('Oscar', None, (0.7, 0.6, 0.7, 0.05))]

    t1_name = ['messi', 'fati', 'depay', 'de jong', 'neymar', 'ter stegen']
    t1_pos = [config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[3]]
    t1_prob = [(0.75, 0.1, 0.8, 0.1, 0.1, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.7, 0.1, 0.75, 0.2, 0.05, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.58, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7,  0.69, 0.2, 0.1, 0.01), (0.73, 0.1, 0.81, 0.1, 0.09, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3)]
    t1_act_prob = [[0.8, 0.9, 0.7, 0.8, 0.75, 0.6, 0.0001]]*6

    t2_name = ['ronaldo', 'mbappe', 'ramos', 'benzema', 'alaba', 'courtoi']
    t2_pos = [config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[2], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[3]]
    t2_prob = [(0.8, 0.1, 0.85, 0.1, 0.05, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.62, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.65, 0.2, 0.15, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.76, 0.11, 0.13, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.57, 0.1, 0.9, 0.5, 0.5, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3)]
    t2_act_prob = [[0.8, 0.9, 0.7, 0.8, 0.75, 0.6, 0.0001]]*6

    t1 = []
    t2 = []
    length = len(t1_name)

    for i in range(length - 1):
        t1.append(Jugador(t1_name[i], t1_pos[i], t1_prob[i], t1_act_prob[i]))
        t2.append(Jugador(t2_name[i], t2_pos[i], t2_prob[i], t2_act_prob[i]))
    
    t1_portero_prob = [0.8, 0.4, 0.1, 0.2, 0.3]
    t2_portero_prob = [0.7, 0.4, 0.1, 0.3, 0.2]
    t1.append(Portero(t1_name[length - 1], t1_pos[length - 1], t1_prob[length - 1], t1_act_prob[length - 1], t1_portero_prob))
    t2.append(Portero(t2_name[length - 1], t2_pos[length - 1], t2_prob[length - 1], t2_act_prob[length - 1], t2_portero_prob))


    eq1 = Equipo("Barca", "PEPE1", t1)
    eq2 = Equipo("Madrid", "PEPE2", t2)

    p1 = Partido(eq1,eq2, arbitros)

    p1.simular()


if '__main__' == __name__:
    main()
