from compilacion.analisis_semantico.type import MyType


class Attribute:
    def __init__(self, name: str, attr_type: MyType) -> None:
        self.name = name
        self.type = attr_type