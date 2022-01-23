
class Reporte:
    def __init__(self, nombre_eq1, nombre_eq2) -> None:
        self._eq2 = nombre_eq2
        self._eq1 = nombre_eq1
        self._goles = {self._eq1: 0, self._eq2: 0}
        self._remates = {self._eq1: 0, self._eq2: 0}
        self._tiros_de_esquina = {self._eq1: 0, self._eq2: 0}
        self._fuera_de_juego = {self._eq1: 0, self._eq2: 0}
        self._pases = {self._eq1: 0, self._eq2: 0}
        self._balones_perdidos = {self._eq1: 0, self._eq2: 0}
        self._balones_recuperados = {self._eq1: 0, self._eq2: 0}
        self._paradas_portero = {self._eq1: 0, self._eq2: 0}
        self._faltas = {self._eq1: 0, self._eq2: 0}
        self._tarjetas_amarillas = {self._eq1: 0, self._eq2: 0}
        self._tarjetas_rojas = {self._eq1: 0, self._eq2: 0}

    def annadir_gol(self, eq):
        self._goles[eq] += 1

    def annadir_remate(self, eq):
        self._remates[eq] += 1

    def annadir_tiro_esquina(self, eq):
        self._tiros_de_esquina[eq] += 1

    def annadir_fuera_juego(self, eq):
        self._fuera_de_juego[eq] += 1

    def annadir_pase(self, eq):
        self._pases[eq] += 1

    def annadir_balon_perdido(self, eq):
        self._balones_perdidos[eq] += 1

    def annadir_balon_recuperado(self, eq):
        self._balones_recuperados[eq] += 1

    def annadir_parada_portero(self, eq):
        self._paradas_portero[eq] += 1

    def annadir_falta(self, eq):
        self._faltas[eq] += 1

    def annadir_tarjeta_amarilla(self, eq):
        self._tarjetas_amarillas[eq] += 1

    def annadir_tarjeta_roja(self, eq):
        self._tarjetas_rojas[eq] += 1


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
 