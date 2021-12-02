import random
import numpy

from config import Config
config = Config()


class Player:
    def __init__(self, nombre, pos, list_prob):#  gol_p, atajar_p, pase_efectivo_p, pase_largo_p, pase_intercep_p, gol_partido, atajar_partido, no_falta, falta_leve, falta_amarilla, falta_roja, pos_array) -> None:
        self.nombre = nombre
        self.posicion = pos

        self.gol_p = list_prob[0]
        self.atajar_p = list_prob[1]
        
        self.pase_efectivo_p = list_prob[2]
        self.pase_largo_p = list_prob[3]
        self.pase_intercep_p = list_prob[4]
        self.gol_partido = list_prob[5]
        self.atajar_partido = list_prob[6]

        #a lo mejor no hace falta
        self.no_falta = list_prob[7]
        self.falta_leve = list_prob[8]
        self.falta_amarilla = list_prob[9]
        self.falta_roja = list_prob[10]

        self.cantidad_tarjetas = 0
        #self.pos_array = pos_array
        self.fuera_del_partido = False

        #solo para el portero
        if len(list_prob) > 11:
            self.rebote = list_prob[11]
            self.rebote_banda = list_prob[12]
            self.rebote_linea_final = list_prob[13]
            self.rebote_jugador = list_prob[14]
    

    def seleccionar_jugador_pase(self, eq, reanudar_partido=False):
        index = -1
        if self.posicion == 'DEL':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.5,   0.35,   0.1,  0.05])
        elif self.posicion == 'MC':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.4,   0.3,   0.2,  0.1])
        elif self.posicion == 'DEF':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.05,   0.4,   0.25,  0.3])
        elif self.posicion == 'GK':
            index = numpy.random.choice(numpy.arange(0, 3), p=[0.3,   0.3,   0.4])

        jugador2 = self.obtener_jugador(config.POSICIONES[index], eq)
        if jugador2 == self and reanudar_partido:
            return self.seleccionar_jugador_pase(eq, reanudar_partido)
        
        return jugador2

    #no se si poner este metodo aqui seria lo ideal
    def obtener_jugador(self, posicion, eq):
        temp_list = []
        for item in eq.jugadores:
            if item.posicion == posicion:
                temp_list.append(item)
        j1 = temp_list[int(random.randint(0, len(temp_list)- 1))]
        return j1

    def interceptar_pase(self, eq):
        index = -1
        if self.posicion == 'DEL':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.1,   0.3,   0.4,  0.2])
        elif self.posicion == 'MC':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.2,   0.3,   0.3,  0.2])
        elif self.posicion == 'DEF':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.3,   0.3,   0.2,  0.2])
        elif self.posicion == 'GK':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.4,   0.3,   0.2,  0.1])
        else:
            print("POSICION NO REGISTRADA")

        return self.obtener_jugador(config.POSICIONES[index], eq)

    def elegir_jugador_para_sacar(self, eq):
        index = numpy.random.choice(numpy.arange(0, 4), p=[0.1,   0.35,   0.5,  0.05])
        return self.obtener_jugador(config.POSICIONES[index], eq)

    def cometer_falta(self, lanzador, receptor, arbitro):
        arbitro_tarjeta = numpy.random.choice(numpy.arange(0, 4), p=[arbitro.no_canta_falta, arbitro.declare_falta_leve, arbitro.tarjeta_amarilla, arbitro.tarjeta_roja])
                
        if arbitro_tarjeta == 0: # el arbitro decide no cantar la falta
            print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}, pero fue interceptado por {self.nombre} (el arbitro decidio no cantar la falta)")
            return "INTERCEPTADO", self
        else:
            print(f"{lanzador.nombre} le paso el balon a {receptor.nombre}, pero {self.nombre} trato de interceptarlo y cometio falta")

            if arbitro_tarjeta == 2: #saca tarjeta amarilla
                self.cantidad_tarjetas += 1

                if self.cantidad_tarjetas == 2:
                    self.cantidad_tarjetas = 0
                    self.fuera_del_partido = True
                    # t.pop(self.pos_array) da error el metodo obtener_jugador
                    print(f"{self.nombre} le sacaron tarjeta amarilla por segunda vez y lo expulsaron")
                else:
                    print(f"{self.nombre} le sacaron tarjeta amarilla")

            if arbitro_tarjeta == 3: #saca tarjeta roja
                self.cantidad_tarjetas = 0
                self.fuera_del_partido = True
                # t.pop(self.pos_array) da error el metodo obtener_jugador
                print(f"{self.nombre} le sacaron tarjeta roja y lo expulsaron")
        
        return "FALTA"

    def tiro_a_porteria_en_partido(self, portero, equipo, equipo_contrario):
        jugador_gol = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.gol_partido , self.gol_partido])
        portero_ataja = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.atajar_partido, portero.atajar_partido])
        jugador_a_sacar = None

        if jugador_gol > portero_ataja:
            return 'O', jugador_a_sacar
        else:
            portero_rebote = numpy.random.choice(numpy.arange(0, 2), p=[1 - portero.rebote , portero.rebote])
            
            if portero_rebote == 0: #el portero atajo el balon y no hubo rebote
                print(f"{self.nombre} tiro a porteria, pero el portero {portero.nombre} atajo el balon sin rebote")
                return "NO_REBOTE", portero
            else: #hubo rebote
                portero_tipo_rebote = numpy.random.choice(numpy.arange(0, 3), p=[portero.rebote_banda , portero.rebote_linea_final, portero.rebote_jugador])
                
                if portero_tipo_rebote == 0: #el rebote salio por la banda y hay saque de banda
                    print(f"{self.nombre} tiro a porteria, pero el portero {portero.nombre} saco el balon por la banda")
                    jugador_a_sacar = self.elegir_jugador_para_sacar(equipo) #jugador para sacar de banda
                    print(f"{jugador_a_sacar.nombre} va a sacar desde la banda")
                    return "POR_BANDA", jugador_a_sacar

                elif portero_tipo_rebote == 1: #el rebote salio por la linea final y hay tiro de esquina
                    #Implementar tiro de esquina
                    jugador_a_sacar = portero
                    print(f"{self.nombre} tiro a porteria, pero el portero {portero.nombre} saco el balon por la linea final")
                    return "TIRO_ESQUINA", jugador_a_sacar

                elif portero_tipo_rebote == 2: #el rebote le cayo a un jugador, ya sea el portero mismo, un jugador de t1 o de t2
                    recibir_rebote = numpy.random.choice(numpy.arange(0, 3), p=[0.3, 0.4 , 0.3])
                    
                    if recibir_rebote == 0: #el rebote le cae al propio portero
                        print(f"{self.nombre} tiro a porteria, pero el portero {portero.nombre} recibio el rebote")
                        jugador_a_sacar = portero

                    elif recibir_rebote == 1: #el rebote le cae a un jugador del mismo equipo q el portero
                        jugador_a_sacar = self.elegir_jugador_para_sacar(equipo)
                        print(f"{self.nombre} tiro a porteria, pero el portero rechazo y {jugador_a_sacar.nombre} recibio el rebote")

                    elif recibir_rebote == 2: #el rebote le cae a un jugador del equipo contrario al del portero
                        jugador_a_sacar = self.elegir_jugador_para_sacar(equipo_contrario)
                        print(f"{self.nombre} tiro a porteria, pero el portero rechazo y {jugador_a_sacar.nombre} (del equipo contrario) recibio el rebote")
                        return "REBOTE_JUGADOR_CONTRARIO", jugador_a_sacar

                    return "REBOTE_JUGADOR", jugador_a_sacar


    def __eq__(self, jugador) -> bool:
        return (self.nombre == jugador.nombre and self.posicion == jugador.posicion)