from compilacion.grammars.sentence import Sentence


class Epsilon(Sentence):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    
    def __str__(self) -> str:
        return "€"