
class Player:
    def __init__(self, nombre, pos, gol_p, atajar_p, pase_efectivo_p, pase_largo_p, pase_intercep_p) -> None:
        self.nombre = nombre
        self.posicion = pos

        self.gol_p = gol_p
        self.atajar_p = atajar_p
        
        self.pase_efectivo_p = pase_efectivo_p
        self.pase_largo_p = pase_largo_p
        self.pase_intercep_p = pase_intercep_p