
class Reporte:
    def __init__(self, nombre_eq1, nombre_eq2) -> None:
        self.__eq1 = nombre_eq1
        self.__eq2 = nombre_eq2
        self.__goles = {self.__eq1: 0, self.__eq2: 0}
        self.__remates = {self.__eq1: 0, self.__eq2: 0}
        self.__tiros_de_esquina = {self.__eq1: 0, self.__eq2: 0}
        self.__fuera_de_juego = {self.__eq1: 0, self.__eq2: 0}
        self.__pases = {self.__eq1: 0, self.__eq2: 0}
        self.__balones_perdidos = {self.__eq1: 0, self.__eq2: 0}
        self.__balones_recuperados = {self.__eq1: 0, self.__eq2: 0}
        self.__paradas_portero = {self.__eq1: 0, self.__eq2: 0}
        self.__faltas = {self.__eq1: 0, self.__eq2: 0}
        self.__tarjetas_amarillas = {self.__eq1: 0, self.__eq2: 0}
        self.__tarjetas_rojas = {self.__eq1: 0, self.__eq2: 0}

    def annadir_gol(self, eq):
        self.__goles[eq] += 1

    def annadir_remate(self, eq):
        self.__remates[eq] += 1

    def annadir_tiro_esquina(self, eq):
        self.__tiros_de_esquina[eq] += 1

    def annadir_fuera_juego(self, eq):
        self.__fuera_de_juego[eq] += 1

    def annadir_pase(self, eq):
        self.__pases[eq] += 1

    def annadir_balon_perdido(self, eq):
        self.__balones_perdidos[eq] += 1

    def annadir_balon_recuperado(self, eq):
        self.__balones_recuperados[eq] += 1

    def annadir_parada_portero(self, eq):
        self.__paradas_portero[eq] += 1

    def annadir_falta(self, eq):
        self.__faltas[eq] += 1

    def annadir_tarjeta_amarilla(self, eq):
        self.__tarjetas_amarillas[eq] += 1

    def annadir_tarjeta_roja(self, eq):
        self.__tarjetas_rojas[eq] += 1


    def __str__(self):
        prop = vars(self)
        underscores = 40    
        str_result = '\n' +'_'*underscores + '\n'+ 'Estadisticas del Partido'.center(underscores) + '\n' +'_'*underscores   
        for i in range(2, len(prop)):
            est = list(prop.keys())[i].replace('_Reporte__','').split('_')
            if i == 2: #Marcador
                g_eq1 = f'\n  {list(prop[list(prop.keys())[i]].keys())[0]}'
                g_eq2 = f'{list(prop[list(prop.keys())[i]].keys())[1]}  '
                marcador = f'{list(prop[list(prop.keys())[i]].values())[0]} - {list(prop[list(prop.keys())[i]].values())[1]}'.center(underscores - len(g_eq1) - len(g_eq2))
                str_result += g_eq1 + marcador + g_eq2
            else:
                est_eq1 = f'\n  {list(prop[list(prop.keys())[i]].values())[0]}'
                est_eq2 = f'{list(prop[list(prop.keys())[i]].values())[1]}  '
                est = f'{" ".join(est).upper()}'.center(underscores - len(est_eq1) - len(est_eq2))
                str_result += est_eq1 + est + est_eq2
            str_result += '\n' + '_'*underscores
        return str_result
