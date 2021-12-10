import random
from config import Config

config = Config()

class Equipo:
    def __init__(self, nombre, manager, jugadores) -> None:
        self.nombre = nombre
        self.manager = manager
        self.jugadores_en_campo, self.jugadores_en_banda, self.jugadores_restantes = self.seleccionar_jugadores(jugadores)

        for i in range(len(self.jugadores_en_campo)):
            self.jugadores_en_campo[i].equipo = self

        for i in range(len(self.jugadores_en_banda)):
            self.jugadores_en_banda[i].equipo = self


    def clasificar_jugadores(self, jugadores)->dict:
        clasificacion = {}
        clasificacion['DEL'] = []
        clasificacion['MC'] = []
        clasificacion['DEF'] = []
        clasificacion['GK'] = []

        for jugador in jugadores:
            clasificacion[jugador.posicion].append(jugador)

        return clasificacion


    def seleccionar_jugadores(self, jugadores):
        i = 0
        cantidades = [3, 3, 4, 1]
        jugadores_en_campo = []
        jugadores_en_banca = []
        jugadores_restantes = []
        clasificacion = self.clasificar_jugadores(jugadores)

        for pos in config.POSICIONES:
            self.seleccionar_jugadores_por_posicion(clasificacion[pos], cantidades[i], jugadores_en_campo)
            self.seleccionar_jugadores_por_posicion(clasificacion[pos], 7, jugadores_en_banca)
            self.seleccionar_jugadores_por_posicion(clasificacion[pos], len(clasificacion[pos]), jugadores_restantes)
            i += 1

        return jugadores_en_campo, jugadores_en_banca, jugadores_restantes
        

    def seleccionar_jugadores_por_posicion(self, jugadores, cantidad, jugadores_en_campo):
        cant = 0
        while(cant < cantidad and len(jugadores) != 0):
            i =  random.randint(0, len(jugadores) - 1)
            jugador = jugadores[i]
            jugadores_en_campo.append(jugador)
            jugadores.pop(i)
            cant += 1
