from typing import List
from compilacion.analisis_semantico.method import *


class MyType:
    def __init__(self, name, attributes: List[Attribute], methods: List[Method]) -> None:
        self.name = name
        self.attributes = attributes
        self.methods = methods
    
    def get_attribute(self, name: str) -> Attribute:
        for attr in self.attributes:
            if attr.name == name:
                return attr
        return None

    def get_method(self, name: str) -> Method:
        for method in self.methods:
            if method.name == name:
                return method
        return None
    
    def define_attribute(self, name: str, attr_type) -> bool:
        if not self.contains_attribute(name):
            attr = Attribute(name, attr_type)
            self.attributes.append(attr)
            return True
        return False

    def define_method(self, name: str, return_type, args: List[Attribute]) -> bool:
        if not self.contains_method(name):
            method = Method(name, return_type, args)
            self.methods.append(method)
            return True
        return False

    def contains_attribute(self, name):
        for attr in self.attributes:
            if attr.name == name:
                return True
        return False
    
    def contains_method(self, name, count_args):
        for method in self.methods:
            if method.name == name and count_args == len(method.args):
                return True
        return False