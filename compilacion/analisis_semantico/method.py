from typing import List
from compilacion.analisis_semantico.type import MyType
from compilacion.analisis_semantico.attribute import Attribute


class Method:
    def __init__(self, name: str, return_type: MyType, args: List[Attribute]) -> None:
        self.name = name
        self.return_type = return_type
        self.args = args