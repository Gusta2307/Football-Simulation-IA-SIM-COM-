import random
from IA.optimizador import Optimizador
from classes.reporte import Reporte_General
from utiles import analisis_acciones_list, elimina_tipo
from config import Config
config = Config()


class Partido:
    def __init__(self, eq1, eq2, arbitros) -> None:
        self.eq1 = eq1
        self.eq2 = eq2
        self.arbitros = arbitros

        self.eq1.manager.acciones['ESCOGER_ALINEACION'][0].ejecutar(self)
        self.eq2.manager.acciones['ESCOGER_ALINEACION'][0].ejecutar(self)

        self.__inicializar()

        self.op = Optimizador(self)
        self.op.optimizar()


    def __inicializar(self):
        self.marcador = [0,0]

        self.pt = None # Parte del partido (1ra parte, 2da parte)

        self.reporte = Reporte_General(self.eq1.nombre, self.eq2.nombre)

        self.cambios_por_equipo = {
            self.eq1.nombre: [config.PARTIDO.CONFIG.VENTANAS_DE_CAMBIOS, config.PARTIDO.CONFIG.TOTAL_DE_CAMBIOS],
            self.eq2.nombre: [config.PARTIDO.CONFIG.VENTANAS_DE_CAMBIOS, config.PARTIDO.CONFIG.TOTAL_DE_CAMBIOS]
        }

        self.cambios_pendiente = {
            self.eq1.nombre: [],
            self.eq2.nombre: []
        }

        self.__tiempo = None #Tiempo en minutos

        self.estado = config.PARTIDO.ESTADO.INICIAR_PARTIDO

        self.ultima_accion = None #ultima accion q realizo el jugador que tenia el balon

        self.pos_balon = None #jugador con la posesion de balon

        self.pos_balon_1er_tiempo = None


    def __empezar_tiempo(self):
        self.__tiempo = float(0)
        

    def obtener_tiempo(self):
        return f'{int(self.__tiempo)}\''

    def __iniciar_partido(self):
        self.reporte.annadir_a_resumen('Inicia el partido...', self.pt)
        self.pt = 1
        self.__empezar_tiempo()
        equipo = random.randint(1, 2)
        eq = self.eq1 if equipo == 1 else self.eq2
        temp_jugador_list = []

        self.pos_balon_1er_tiempo = eq

        #este for seria por el once inicial y no por todos los del equipo
        for jugador in eq.jugadores_en_campo:
            if jugador.posicion == 'DEL':
                temp_jugador_list.append(jugador)
        self.pos_balon = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]

        return self.pos_balon.escoger_accion_base(self)

    def __reanudar_partido(self, is_goal=False):
        if is_goal:
            eq = self.eq1 if self.ultima_accion.agente.equipo == self.eq2 else self.eq2
        else:
            eq = self.eq1 if self.pos_balon_1er_tiempo == self.eq2 else self.eq2
        temp_jugador_list = []
        for jugador in eq.jugadores_en_campo:
            if jugador.posicion == 'DEL':
                temp_jugador_list.append(jugador)

        self.pos_balon = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]
        self.reporte.annadir_a_resumen("Se reanuda el partido", self.pt)


    # def __reanudar_partido(self):
    #     eq = self.eq1 if self.pos_balon_1er_tiempo == self.eq2 else self.eq2
    #     temp_jugador_list = []
    #     for jugador in eq.jugadores_en_campo:
    #         if jugador.posicion == 'DEL':
    #             temp_jugador_list.append(jugador)

    #     self.pos_balon = temp_jugador_list[random.randint(0, len(temp_jugador_list) - 1)]
    #     self.reporte.annadir_a_resumen("Se reanuda el partido", self.pt)

    def simular(self, opt = False, tiempo = 90):
        act = self.__iniciar_partido()
        act.ejecutar(self)
        while int(self.__tiempo) < tiempo:
            acciones_actual = []
            for j in self.arbitros + self.eq1.jugadores_en_campo + self.eq2.jugadores_en_campo + [self.eq1.manager, self.eq2.manager]:
                accion = j.escoger_accion_estrategia(self)
                acciones_actual.append(accion)
            acciones_actual = analisis_acciones_list(acciones_actual, self.ultima_accion, self.estado)


            acciones_actual = elimina_tipo(acciones_actual, config.ACCIONES.JUGADOR.ACT_DEFAULT)

            mayor_tiempo = 0
            for item in acciones_actual:
                if item.precondicion(self):
                    item.ejecutar(self)
                    if mayor_tiempo < item.tiempo:
                        mayor_tiempo = item.tiempo

            self.__tiempo += mayor_tiempo


            if self.estado == config.PARTIDO.ESTADO.REANUDAR_PARTIDO:
                self.__reanudar_partido(is_goal=True)

            if self.estado == config.PARTIDO.ESTADO.DETENIDO:
                eq = [self.eq1.nombre, self.eq2.nombre]
                for e in eq:
                    while self.cambios_pendiente[e]:
                        self.cambios_pendiente[e].pop().poscondicion(self, opt)

            if self.pt == 1 and self.__tiempo > 45:
                self.pt = 2
                self.estado = config.PARTIDO.ESTADO.REANUDAR_PARTIDO
                self.__reanudar_partido()

            #if len(acciones_actual) != 0:
            #    iter -= 1

        result = self.reporte
        self.__inicializar() #retorna un reporte y antes restablecer todas las variables
        return result


    def eq_dic(self, eq1, eq2):
        return {1:eq1, 2: eq2}
