
class Player:
    def __init__(self, nombre, pos, gol_p, atajar_p, pase_efectivo_p, pase_largo_p, pase_intercep_p, gol_partido, atajar_partido, no_falta, falta_leve, falta_amarilla, falta_roja, pos_array) -> None:
        self.nombre = nombre
        self.posicion = pos

        self.gol_p = gol_p
        self.atajar_p = atajar_p
        
        self.pase_efectivo_p = pase_efectivo_p
        self.pase_largo_p = pase_largo_p
        self.pase_intercep_p = pase_intercep_p
        self.gol_partido = gol_partido
        self.atajar_partido = atajar_partido

        #a lo mejor no hace falta
        self.no_falta = no_falta
        self.falta_leve = falta_leve
        self.falta_amarilla = falta_amarilla
        self.falta_roja = falta_roja

        self.cantidad_tarjetas = 0
        self.pos_array = pos_array
        self.fuera_del_partido = False