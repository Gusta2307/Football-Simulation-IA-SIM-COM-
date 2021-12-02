import random
import numpy
import time


class Partido:
    def __init__(self, eq1, eq2, arbitros) -> None:
        self.eq1 = eq1
        self.eq2 = eq2
        self.arbitros = arbitros
        self.marcador = [0,0]
        
        self.__pos_balon = -1 
        self.__eq_dic = self.eq_dic(self.eq1, self.eq2)
        self.__pos_jugador = None #jugador con la posecion de balon



    def __iniciar_partido(self):
        self.__pos_balon = random.randint(1, 2)
        temp_jugador_list = []
        #este for seria por el once inicial y no por todos los del equipo
        for player in self.__eq_dic[self.__pos_balon].jugadores: 
            if player.posicion == 'DEL':
                temp_jugador_list.append(player)
        j1 = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]
        self.__pos_jugador = j1.seleccionar_jugador_pase(self.__eq_dic[self.__pos_balon], True)
        print('Inicia el partido...')
        print(f"{j1.nombre} le paso el balon a {self.__pos_jugador.nombre}")

    def __reanudar_partido_pos_gol(self):
        sec = random.uniform(1, 3)
        time.sleep(sec) #espera sec tiempo para reanuadar el partido
        pos_balon = 1 if self.__pos_balon == 2 else 2
        temp_player_list = []
        for player in self.__eq_dic[self.__pos_balon].jugadores:
            if player.posicion == 'DEL':
                temp_player_list.append(player)
        j1 = temp_player_list[random.randint(0, len(temp_player_list) - 1)]
        j2 = j1.seleccionar_jugador_pase(self.__eq_dic[self.__pos_balon], True)
        print(f"{j1.nombre} saca luego del gol y le pasa el balon a {j2.nombre}")
        return pos_balon, j2

    def __realiza_un_pase(self, j1, eq):
        pase_efect = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.__pos_jugador.pase_efectivo_p, self.__pos_jugador.pase_efectivo_p])
        pase_intercep = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.__pos_jugador.pase_intercep_p, self.__pos_jugador.pase_intercep_p])
        pase_largo = numpy.random.choice(numpy.arange(0, 2), p=[1 - self.__pos_jugador.pase_largo_p, self.__pos_jugador.pase_largo_p])    
        jugador_inter = None

        if pase_efect > pase_intercep:
            if pase_efect > pase_largo:
                print(f"{self.__pos_jugador.nombre} le paso el balon a {j1.nombre}")
                return "RECIBIDO", jugador_inter
            else: 
                print(f"{self.__pos_jugador.nombre} le paso el balon a {j1.nombre}, pero se fue de largo")
                jugador_inter = self.__pos_jugador.elegir_jugador_para_sacar(eq) #jugador para sacar de banda
                print(f"{jugador_inter.nombre} va a sacar desde la banda")
                return "LARGO", jugador_inter
        else:
            jugador_comete_falta = numpy.random.choice(numpy.arange(0, 4), p=[self.__pos_jugador.no_falta, self.__pos_jugador.falta_leve, self.__pos_jugador.falta_amarilla, self.__pos_jugador.falta_roja])
            jugador_inter = self.__pos_jugador.interceptar_pase(eq)
            
            if jugador_comete_falta == 0: # no cometio falta
                print(f"{self.__pos_jugador.nombre} le paso el balon a {j1.nombre}, pero fue interceptado por {jugador_inter.nombre}")
                return "INTERCEPTADO", jugador_inter 

            else: #cometio falta
                arbitro_principal = self.arbitros[0]
                return jugador_inter.cometer_falta(self.__pos_jugador, j1, arbitro_principal), None


    def __analizar_result_pase(self, resultado, j1, jugador_pase_inter):
        #equipo = t1 if pos_balon == 1 else t2
        largo = True if resultado == "LARGO" or resultado == "FALTA" else False
        pos_balon = self.__pos_balon
        jugador1 = self.__pos_jugador

        if resultado == "RECIBIDO": #si jugador2 recibio, entonces ahora el es el que tiene la opcion de pasar el balon o tirar a porteria
            jugador1 = j1
            # jugador2 = None
        
        elif resultado == "LARGO" or resultado == "INTERCEPTADO":
            jugador1 = jugador_pase_inter
            pos_balon = 1 if self.__pos_balon == 2 else 2

        elif resultado == "FALTA":
            jugador1 = self.__pos_jugador.elegir_jugador_para_sacar(self.__eq_dic[self.__pos_balon])
            print(f"{jugador1.nombre} saca luego de la falta")

        return jugador1, pos_balon, largo

    def __analizar_result_tiro_a_porteria(self, resultado, jugador_a_sacar):
        #equipo = t1 if pos_balon == 1 else t2
        largo = False if resultado == 'O' else True
        pos_balon = self.__pos_balon

        if resultado == 'O':
            print(f"{self.__pos_jugador.nombre} marco GOOOOOOOOOOLLL")
            if self.__pos_balon == 1: 
                self.marcador[0] += 1
            else: 
                self.marcador[1] += 1
            
            print(f"Marcador: {self.eq1.nombre}: {self.marcador[0]} {self.eq2.nombre}: {self.marcador[1]}")
            pos_balon, jugador1 = self.__reanudar_partido_pos_gol()

        else:
            jugador1 = jugador_a_sacar

            if resultado == "NO_REBOTE" or resultado == "REBOTE_JUGADOR_CONTRARIO":
                pos_balon = 1 if self.__pos_balon == 2 else 2

            elif resultado == "TIRO_ESQUINA":
                pass

        return jugador1, pos_balon, largo


    def simular(self):
        iter = 20
        largo = False
        self.__iniciar_partido()

        while iter:
            d = numpy.random.choice(numpy.arange(0, 2), p=[0.95, 0.05]) if not largo else 0 

            if self.__pos_jugador.posicion == 'GK':
                j1 = self.__pos_jugador.seleccionar_jugador_pase(self.__eq_dic[self.__pos_balon])
                resultado, jugador_pase_inter = self.__realiza_un_pase(j1, self.eq2 if self.__pos_balon == 1 else self.eq1)
                self.__pos_jugador, self.__pos_balon, largo = self.__analizar_result_pase(resultado, j1, jugador_pase_inter)
                continue
            
            if d == 0: #el jugador del equipo que posee el balon realiza un pase
                j1 = self.__pos_jugador.seleccionar_jugador_pase(self.__eq_dic[self.__pos_balon])
                if self.__pos_jugador == j1:
                    print(f"{self.__pos_jugador.nombre} se mantiene con el balon")
                    continue

                resultado, jugador_pase_inter = self.__realiza_un_pase(j1, self.eq2 if self.__pos_balon == 1 else self.eq1) #jugador1 le pasa el balon al jugador2
                self.__pos_jugador, self.__pos_balon, largo = self.__analizar_result_pase(resultado, j1, jugador_pase_inter)
            
            else: #el jugador del equipo que posee el balon tira a porteria
                portero = self.eq2.jugadores[-1] if self.__pos_balon == 1 else self.eq1.jugadores[-1]
                resultado, jugador_a_sacar = self.__pos_jugador.tiro_a_porteria_en_partido(portero, self.__eq_dic[self.__pos_balon], self.eq2 if self.__pos_balon == 1 else self.eq1)
                self.__pos_jugador, self.__pos_balon, largo = self.__analizar_result_tiro_a_porteria(resultado, jugador_a_sacar)
                
            iter -= 1


    def eq_dic(self, eq1, eq2):
        return {1:eq1, 2: eq2}


