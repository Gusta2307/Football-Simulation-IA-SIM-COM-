class Equipo:
    def __init__(self, nombre, manager, jugadores) -> None:
        self.nombre = nombre
        self.manager = manager
        self.jugadores = jugadores
        for i in range(len(self.jugadores)):
            self.jugadores[i].equipo = self
