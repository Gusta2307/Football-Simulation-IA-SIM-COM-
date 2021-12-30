from typing import List
from compilacion.analisis_semantico.attribute import Attribute


class Method:
    def __init__(self, name: str, return_type, args: List[Attribute]) -> None:
        self.name = name
        self.return_type = return_type # es de tipo MyType
        self.args = args