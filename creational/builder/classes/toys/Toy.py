from abc import ABC


class Toy(ABC):
    def __init__(self, name, price, heigth, width) -> None:
        self._name = name
        self._price = price
        self._heigth = heigth
        self._width = width
    
    def getPrice(self) -> float:
        return self._price


class Barbie(Toy):
    pass


class Ken(Toy):
    pass


class Polly(Toy):
    pass


class HotWheels(Toy):
    pass
