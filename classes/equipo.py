from collections import defaultdict


class Equipo:
    def __init__(self, nombre, manager, jugadores) -> None:
        self.nombre = nombre
        self.manager = manager
        self.jugadores = jugadores

        self._jugadores_en_campo = None
        self._jugadores_en_banca = None

        for j in jugadores:
            j.equipo = self

        self.manager.equipo = self

    @property
    def jugadores_en_campo(self):
        return self._jugadores_en_campo

    @jugadores_en_campo.setter
    def jugadores_en_campo(self, jugadores):
        self._jugadores_en_campo = jugadores

    @property
    def jugadores_en_banca(self):
        return self._jugadores_en_banca

    @jugadores_en_banca.setter
    def jugadores_en_banca(self, jugadores):
        self._jugadores_en_banca = jugadores
