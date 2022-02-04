
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
        self._resumen = []

    # @property
    # def goles(self):
    #     return {self._eqi1 : a.goles[self._eq1] + b.goles[self._eq1], ........}

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

    def annadir_a_resumen(self, string):
        self._resumen.append(string)
        
    def __str__(self):
        prop = vars(self)
        underscores = 40    
        str_result = '\n' +'_'*underscores + '\n'+ 'Estadisticas del Partido'.center(underscores) + '\n' +'_'*underscores   
        for i in range(2, len(prop)-3):
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
        

        temp_resumen = "resume"
        str_result+= f'\n{" ".join(temp_resumen).upper()}'.center(underscores - len(temp_resumen))
        # str_result += '\n' + '_'*underscores
        for s in self._resumen:
            str_result+= '\n' + s
        str_result += '\n' + '_'*underscores
        return str_result
 



class Reporte_General(Reporte):
    def __init__(self, nombre_eq1, nombre_eq2):
        super().__init__(nombre_eq1,nombre_eq2)
        self.reporte1 = Reporte(nombre_eq1, nombre_eq2)
        self.reporte2 = Reporte(nombre_eq1, nombre_eq2)


    @property
    def goles(self):
        return {
            self._eq1: self.reporte1._goles[self.eq1] + self.reporte2._goles[self.eq1], 
            self._eq2: self.reporte1._goles[self.eq2] + self.reporte2._goles[self.eq2]
        }



    @property
    def remates(self):
        return {
            self._eq1: self.reporte1._remates[self._eq1] + self.reporte2._remates[self._eq1],
            self._eq2: self.reporte1._remates[self._eq2] + self.reporte2._remates[self._eq2],
        }


    @property
    def tiros_de_esquina(self):
        return {
            self._eq1: self.reporte1._tiros_de_esquina[self._eq1] + self.reporte2._tiros_de_esquina[self._eq1],
            self._eq2: self.reporte1._tiros_de_esquina[self._eq2] + self.reporte2._tiros_de_esquina[self._eq2],
        } 


    @property
    def fuera_de_juego(self):
        return {
            self._eq1: self.reporte1._fuera_de_juego[self._eq1] + self.reporte2._fuera_de_juego[self._eq1],
            self._eq2: self.reporte1._fuera_de_juego[self._eq2] + self.reporte2._fuera_de_juego[self._eq2],
        }
    
    @property
    def pase(self):
        return {
            self._eq1: self.reporte1._pases[self._eq1] + self.reporte2._pases[self._eq1],
            self._eq2: self.reporte1._pases[self._eq2] + self.reporte2._pases[self._eq2],
        }
        

    
    @property
    def balones_perdidos(self):
        return {
            self._eq1: self.reporte1._balones_perdidos[self._eq1] + self.reporte2._balones_perdidos[self._eq1],
            self._eq2: self.reporte1._balones_perdidos[self._eq2] + self.reporte2._balones_perdidos[self._eq2],
        }

    
    @property
    def balones_perdidos(self):
        return {
            self._eq1: self.reporte1._balones_recuperados[self._eq1] + self.reporte2._balones_recuperados[self._eq1],
            self._eq2: self.reporte1._balones_recuperados[self._eq2] + self.reporte2._balones_recuperados[self._eq2],
        }


    @property
    def paradas_portero(self):
        return {
            self._eq1: self.reporte1._paradas_portero[self._eq1] + self.reporte2._paradas_portero[self._eq1],
            self._eq2: self.reporte1._paradas_portero[self._eq2] + self.reporte2._paradas_portero[self._eq2],
        }

    
    @property
    def faltas(self):
        return {
            self._eq1: self.reporte1._faltas[self._eq1] + self.reporte2._faltas[self._eq1],
            self._eq2: self.reporte1._faltas[self._eq2] + self.reporte2._faltas[self._eq2],
        }


    @property
    def tarjetas_amarillas(self):
        return {
            self._eq1: self.reporte1._tarjetas_amarillas[self._eq1] + self.reporte2._tarjetas_amarillas[self._eq1],
            self._eq2: self.reporte1._tarjetas_amarillas[self._eq2] + self.reporte2._tarjetas_amarillas[self._eq2],
        }

    @property
    def tarjetas_rojas(self):
        return {
            self._eq1: self.reporte1._tarjetas_rojas[self._eq1] + self.reporte2._tarjetas_rojas[self._eq1],
            self._eq2: self.reporte1._tarjetas_rojas[self._eq2] + self.reporte2._tarjetas_rojas[self._eq2],
        }

    @property
    def resumen(self):
        return self.reporte1._resumen + self.reporte2._resumen



    def annadir_gol(self, eq, t):
        if t == 1:
            self.reporte1._goles[eq] += 1
        else:
            self.reporte2._goles[eq] += 1

        self._goles[eq] += 1

    def annadir_remate(self, eq, t):
        if t == 1:
            self.reporte1._remates[eq] += 1
        else:
            self.reporte2._remates[eq] += 1

        self._remates[eq] += 1

    def annadir_tiro_esquina(self, eq, t):
        if t == 1:
            self.reporte1._tiros_de_esquina[eq] += 1
        else:
            self.reporte2._tiros_de_esquina[eq] += 1

        self._tiros_de_esquina[eq] += 1

    def annadir_fuera_juego(self, eq, t):
        if t == 1:
            self.reporte1._fuera_de_juego[eq] += 1
        else:
            self.reporte2._fuera_de_juego[eq] += 1

        self._fuera_de_juego[eq] += 1

    def annadir_pase(self, eq, t):
        if t == 1:
            self.reporte1._pases[eq] += 1
        else:
            self.reporte2._pases[eq] += 1

        self._pases[eq] += 1

    def annadir_balon_perdido(self, eq, t):
        if t == 1:
            self.reporte1._balones_perdidos[eq] += 1
        else:
            self.reporte2._balones_perdidos[eq] += 1
        
        self._balones_perdidos[eq] += 1

    def annadir_balon_recuperado(self, eq, t):
        if t == 1:
            self.reporte1._balones_recuperados[eq] += 1
        else:
            self.reporte2._balones_recuperados[eq] += 1

        self._balones_recuperados[eq] += 1

    def annadir_parada_portero(self, eq, t):
        if t == 1:
            self.reporte1._paradas_portero[eq] += 1
        else:
            self.reporte2._paradas_portero[eq] += 1

        self._paradas_portero[eq] += 1

    def annadir_falta(self, eq, t):
        if t == 1:
            self.reporte1._faltas[eq] += 1
        else:
            self.reporte2._faltas[eq] += 1
            
        self._faltas[eq] += 1

    def annadir_tarjeta_amarilla(self, eq, t):
        if t == 1:
            self.reporte1._tarjetas_amarillas[eq] += 1
        else:
            self.reporte2._tarjetas_amarillas[eq] += 1
        
        self._tarjetas_amarillas[eq] += 1

    def annadir_tarjeta_roja(self, eq, t):
        if t == 1:
            self.reporte1._tarjetas_rojas[eq] += 1
        else:
            self.reporte2._tarjetas_rojas[eq] += 1
        
        self._tarjetas_rojas[eq] += 1


    def annadir_a_resumen(self, string, t):
        if t == 1:
            self.reporte1._resumen.append(string)
        else:
            self.reporte2._resumen.append(string)
            
        self._resumen.append(string)


