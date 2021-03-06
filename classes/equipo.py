#from collections import defaultdict
#from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration


class Equipo(): #(Declaration):
    def __init__(self, name, country, coach, players) -> None:
        self.nombre = name
        self.manager = coach
        self.jugadores = players
        self.pais = country

        self._jugadores_en_campo = None
        self._jugadores_en_banca = None

        for j in self.jugadores:
            j.equipo = self

        self.manager.equipo = self

    #@property
    def jugadores_en_campo(self):
        return self._jugadores_en_campo

    #@jugadores_en_campo.setter
    def jugadores_en_campo(self, jugadores):
        self._jugadores_en_campo = jugadores

    #@property
    def jugadores_en_banca(self):
        return self._jugadores_en_banca

    #@jugadores_en_banca.setter
    def jugadores_en_banca(self, jugadores):
        self._jugadores_en_banca = jugadores
