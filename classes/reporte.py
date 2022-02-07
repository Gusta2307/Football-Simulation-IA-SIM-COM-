
class Reporte:
    def __init__(self, nombre_eq1, nombre_eq2) -> None:
        self._eq2 = nombre_eq2
        self._eq1 = nombre_eq1
        self._goles = {self._eq1: 0, self._eq2: 0}
        self._remates = {self._eq1: 0, self._eq2: 0}
        self._tiros_de_esquina = {self._eq1: 0, self._eq2: 0}
        self._pases = {self._eq1: 0, self._eq2: 0}
        self._balones_perdidos = {self._eq1: 0, self._eq2: 0}
        self._balones_recuperados = {self._eq1: 0, self._eq2: 0}
        self._paradas_portero = {self._eq1: 0, self._eq2: 0}
        self._faltas = {self._eq1: 0, self._eq2: 0}
        self._tarjetas_amarillas = {self._eq1: 0, self._eq2: 0}
        self._tarjetas_rojas = {self._eq1: 0, self._eq2: 0}
        self._resumen = []

    def annadir_gol(self, eq):
        self._goles[eq] += 1

    def annadir_remate(self, eq):
        self._remates[eq] += 1

    def annadir_tiro_esquina(self, eq):
        self._tiros_de_esquina[eq] += 1

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



class Reporte_Jugador:
    def __init__(self, jugador) -> None:
        self._jugador = jugador
        self._goles = 0
        self._remates = 0
        self._pases = 0
        self._balones_perdidos = 0
        self._balones_recuperados = 0
        self._paradas_portero = 0
        self._faltas = 0
        self._tarjetas_amarillas = 0
        self._tarjetas_rojas = 0


    def annadir_gol(self):
        self._goles += 1

    def annadir_remate(self):
        self._remates += 1

    def annadir_pase(self):
        self._pases += 1

    def annadir_balon_perdido(self):
        self._balones_perdidos += 1

    def annadir_balon_recuperado(self):
        self._balones_recuperados += 1

    def annadir_parada_portero(self):
        self._paradas_portero += 1

    def annadir_falta(self):
        self._faltas += 1

    def annadir_tarjeta_amarilla(self):
        self._tarjetas_amarillas += 1

    def annadir_tarjeta_roja(self):
        self._tarjetas_rojas += 1
        

    def __str__(self) -> str:
        prop = vars(self)
        underscores = 40
        str_result = '_'*underscores + '\n'+ f'Datos del Jugador'.center(underscores) + '\n' +'_'*underscores 
        nombre=self._jugador.nombre
        pos=self._jugador.posicion  
        edad=self._jugador.edad
        pais=self._jugador.pais
        equipo=self._jugador.equipo
        str_result += '\n' + str("".join(" Nombre") + "".join(nombre).rjust(underscores - len("nombre") - 2)).center(underscores)
        str_result += '\n' + str("".join(" Posicion") + "".join(pos).rjust(underscores - len('Posicion') - 2)).center(underscores)
        str_result += '\n' + str("".join(" Edad") + "".join(str(edad)).rjust(underscores - len('Edad') - 2)).center(underscores)
        str_result += '\n' + str("".join(" Pais") + "".join(str(pais)).rjust(underscores - len('pais') - 2)).center(underscores)
        str_result += '\n' + str("".join(" Equipo") + "".join(str(equipo)).rjust(underscores - len('Equipo') - 2)).center(underscores)
        str_result += '\n' +'_'*underscores + '\n'+ f'Estadisticas del Jugador'.center(underscores) + '\n' +'_'*underscores 

        for i in range(1, len(prop)):
            prop_name = str(list(prop.keys())[i]).replace('_', '', 1).replace('_', ' ').upper()
            prop_value = str(list(prop.values())[i])
            str_result += '\n' + str("".join(f"{prop_name}") + "".join(prop_value).rjust(underscores - len(prop_name) - 2)).center(underscores)

        str_result += '\n' +'_'*underscores

        return str_result
