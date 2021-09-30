from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_pencil():
        pass


    @abstractmethod
    def create_pen():
        pass


class Pen(ABC):
    def write(self):
        print(f"I'm writting permanently with - {self.brand}")


class Pencil(ABC):
    def write(self):
        print(f"I'm writting with - {self.brand}")


class FactoryFaberCastle(Factory):
    def create_pen(self):
        return PenFaberCastle("Faber Castle")
    
    def create_pencil(self):
        return PencilFaberCastle("Faber Castle")


class FactoryBic(Factory):
    def create_pen(self):
        return PenBic("Bic")

    def create_pencil(self):
        return PencilBic("Bic")


class PencilFaberCastle(Pencil):
    def __init__(self, brand: str) -> None:
        self.brand = brand
        

class PenFaberCastle(Pen):
    def __init__(self, brand: str) -> None:
        self.brand = brand
        

class PencilBic(Pencil):
    def __init__(self, brand: str) -> None:
        self.brand = brand
        

class PenBic(Pen):
    def __init__(self, brand: str) -> None:
        self.brand = brand


def client(factory: Factory):
    pen = factory.create_pen()
    pencil = factory.create_pencil()
    pen.write()
    pencil.write()


# Aqui o código cliente não conhece a classe concreta, apenas a classe factory
if __name__ == "__main__":
    client(FactoryFaberCastle())
    print('----')
    client(FactoryBic())
