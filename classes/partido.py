import random

from utiles import analisis_acciones_list, elimina_tipo
from config import Config
config = Config()


class Partido:
    def __init__(self, eq1, eq2, arbitros) -> None:
        self.eq1 = eq1
        self.eq2 = eq2
        self.arbitros = arbitros
        self.marcador = [0,0]

        self.estado = config.INICIAR_PARTIDO
        self.ultima_accion = None #ultima accion q realizo el jugador que tenia el balon

        self.pos_balon = None #jugador con la posecion de balon

    def __iniciar_partido(self):
        print('Inicia el partido...')
        equipo = random.randint(1, 2)
        eq = self.eq1 if equipo == 1 else self.eq2
        temp_jugador_list = []

        #este for seria por el once inicial y no por todos los del equipo
        for jugador in eq.jugadores: 
            if jugador.posicion == 'DEL':
                temp_jugador_list.append(jugador)
        self.pos_balon = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]
        
        return self.pos_balon.escoger_accion(self)

    def __reanudar_partido_pos_gol(self):
        eq = self.eq1 if self.ultima_accion.agente.equipo == self.eq2 else self.eq2
        temp_jugador_list = []
        for jugador in eq.jugadores:
            if jugador.posicion == 'DEL':
                temp_jugador_list.append(jugador)

        self.pos_balon = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]
        print("Se reanuda el partido")
        
    
    def simular(self):
        iter = 20
        act = self.__iniciar_partido()
        act.ejecutar(self)
        while iter:
            acciones_actual = []
            for j in self.eq1.jugadores + self.eq2.jugadores + self.arbitros:
                accion = j.escoger_accion(self)
                acciones_actual.append(accion)
            acciones_actual = analisis_acciones_list(acciones_actual, self.ultima_accion, self.estado)

           
            acciones_actual = elimina_tipo(acciones_actual, config.ACT_DEFAULT)
           
            for item in acciones_actual:
                if item.precondicion(self):
                    item.ejecutar(self)

            if self.estado == config.REANUDAR_PARTIDO:
                self.__reanudar_partido_pos_gol()
             
            if len(acciones_actual) != 0:
                iter -= 1


    def eq_dic(self, eq1, eq2):
        return {1:eq1, 2: eq2}
