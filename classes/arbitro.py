
class arbitro:
    def __init__(self, nombre, experiencia, list_prob):# no_canta_falta, declare_falta_leve, tarjeta_amarilla, tarjeta_roja) -> None:
        self.nombre = nombre
        self.experiencia = experiencia

        self.no_canta_falta = list_prob[0]
        self.declare_falta_leve = list_prob[1]
        self.tarjeta_amarilla = list_prob[2]
        self.tarjeta_roja = list_prob[3]