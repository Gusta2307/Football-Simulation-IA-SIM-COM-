
class Player:
    def __init__(self, nombre, pos, list_prob):#  gol_p, atajar_p, pase_efectivo_p, pase_largo_p, pase_intercep_p, gol_partido, atajar_partido, no_falta, falta_leve, falta_amarilla, falta_roja, pos_array) -> None:
        self.nombre = nombre
        self.posicion = pos

        self.gol_p = list_prob[0]
        self.atajar_p = list_prob[1]
        
        self.pase_efectivo_p = list_prob[2]
        self.pase_largo_p = list_prob[3]
        self.pase_intercep_p = list_prob[4]
        self.gol_partido = list_prob[5]
        self.atajar_partido = list_prob[6]

        #a lo mejor no hace falta
        self.no_falta = list_prob[7]
        self.falta_leve = list_prob[8]
        self.falta_amarilla = list_prob[9]
        self.falta_roja = list_prob[10]

        self.cantidad_tarjetas = 0
        #self.pos_array = pos_array
        self.fuera_del_partido = False