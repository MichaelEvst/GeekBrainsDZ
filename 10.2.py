from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption_calculator(self):
        pass


class Coat(Clothes):
    def __init__(self,v):
        self.v = v

    @property
    def fabric_consumption_calculator(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self,h):
        self.h = h

    @property
    def fabric_consumption_calculator(self):
        return self.h * 2 + 0.3


if __name__ == '__main__':
    c = Coat(60)
    print(c.fabric_consumption_calculator)

    s = Suit(370)
    print(s.fabric_consumption_calculator)
