#from pickle import FALSE, NONE
import abc
import random
class Range (abc.ABC):
    @abc.abstractclassmethod
    def get_value(self): 
        raise NotImplementedError


class RangeInt(Range):
    def __init__(self, li, ls, distribution = None) -> None:
        self.l_i = li
        self.l_s = ls
        self.distribucion = distribution
    
    def get_value(self):
        return random.randint(self.l_i, self.l_s) if self.distribucion == None else self.distribucion(random.randint(self.l_i, self.l_s))


class RangeFloat(Range):
    def __init__(self, li, ls, distribution = None) -> None:
        self.l_i = li
        self.l_s = ls
        self.distribucion = distribution

    def get_value(self):
        return random.uniform(self.l_i, self.l_s) if self.distribucion == None else self.distribucion(random.uniform(self.l_i, self.l_s))

       
class RangeBool(Range):
    def __init__(self, distribution = None) -> None:
        self.distribucion = distribution

    def get_value(self):
        return random.choice([True, False]) if self.distribucion == None else self.distribucion(random.choice([True, False]))


class RangeChoice(Range):
    def __init__(self, values, distribution = None) -> None:
        self.valores = values
        self.distribucion = distribution

    def get_value(self):
        return random.choice(self.valores) if self.distribucion == None else self.distribucion(random.choice(self.valores))


