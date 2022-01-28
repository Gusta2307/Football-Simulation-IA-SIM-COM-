import random
from classes.arbitro import Arbitro
from classes.manager import Manager
from IA.optimizador import Optimizador
from classes.reporte import Reporte
from utiles import analisis_acciones_list, elimina_tipo
from config import Config
config = Config()


class Partido:
    def __init__(self, eq1, eq2, arbitros) -> None:
        self.eq1 = eq1
        self.eq2 = eq2
        self.arbitros = arbitros
        self.marcador = [0,0]

        self.reporte = Reporte(self.eq1.nombre, self.eq2.nombre)

        self.cambios_por_equipo = {
            eq1.nombre: [config.PARTIDO.CONFIG.VENTANAS_DE_CAMBIOS, config.PARTIDO.CONFIG.TOTAL_DE_CAMBIOS],
            eq2.nombre: [config.PARTIDO.CONFIG.VENTANAS_DE_CAMBIOS, config.PARTIDO.CONFIG.TOTAL_DE_CAMBIOS]
        }

        self.cambios_pendiente = {
            eq1.nombre: [],
            eq2.nombre: []
        }

        self.__tiempo = None

        self.estado = config.PARTIDO.ESTADO.INICIAR_PARTIDO
        
        self.eq1.manager.acciones['ESCOGER_ALINEACION'][0].ejecutar(self)
        self.eq2.manager.acciones['ESCOGER_ALINEACION'][0].ejecutar(self)

        self.ultima_accion = None #ultima accion q realizo el jugador que tenia el balon

        self.pos_balon = None #jugador con la pocesion de balon

        self.op = Optimizador(self)
        self.op.optimizar()
    

    def __empezar_tiempo(self):
        self.__tiempo = float(0)

    def obtener_tiempo(self):
        return f'{int(self.__tiempo)}\''

    def __iniciar_partido(self):
        print('Inicia el partido...')
        self.__empezar_tiempo()
        equipo = random.randint(1, 2)
        eq = self.eq1 if equipo == 1 else self.eq2
        temp_jugador_list = []

        #este for seria por el once inicial y no por todos los del equipo
        for jugador in eq.jugadores_en_campo: 
            if jugador.posicion == 'DEL':
                temp_jugador_list.append(jugador)
        self.pos_balon = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]
        
        return self.pos_balon.escoger_accion_base(self)

    def __reanudar_partido_pos_gol(self):
        eq = self.eq1 if self.ultima_accion.agente.equipo == self.eq2 else self.eq2
        temp_jugador_list = []
        for jugador in eq.jugadores_en_campo:
            if jugador.posicion == 'DEL':
                temp_jugador_list.append(jugador)

        self.pos_balon = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]
        print("Se reanuda el partido")
        
    
    def simular(self, opt = False):
        iter = 20
        act = self.__iniciar_partido()
        act.ejecutar(self)
        while int(self.__tiempo) < 45:
            acciones_actual = []
            for j in self.arbitros + self.eq1.jugadores_en_campo + self.eq2.jugadores_en_campo + [self.eq1.manager, self.eq2.manager]:
                if isinstance(j, Arbitro) or isinstance(j, Manager):
                    accion = j.escoger_accion_base(self)
                else:
                    accion = j.escoger_accion_estrategia(self)
                acciones_actual.append(accion)
            acciones_actual = analisis_acciones_list(acciones_actual, self.ultima_accion, self.estado)

           
            acciones_actual = elimina_tipo(acciones_actual, config.ACCIONES.JUGADOR.ACT_DEFAULT)
           
            for item in acciones_actual:
                if item.precondicion(self):
                    item.ejecutar(self)
                    self.__tiempo += item.tiempo

            if self.estado == config.PARTIDO.ESTADO.REANUDAR_PARTIDO:
                self.__reanudar_partido_pos_gol()

            if self.estado == config.PARTIDO.ESTADO.DETENIDO:
                eq = [self.eq1.nombre, self.eq2.nombre]
                for e in eq:
                    while self.cambios_pendiente[e]:
                        self.cambios_pendiente[e].pop().poscondicion(self, opt)
                        
            if len(acciones_actual) != 0:
                iter -= 1
        self.restablecer_variables() #retorna un reporte y antes restablecer todas las variables
        return self.reporte

    def eq_dic(self, eq1, eq2):
        return {1:eq1, 2: eq2}

    def restablecer_variables(self):
        pass