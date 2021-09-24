from abc import ABC, abstractmethod

class Pen(ABC):
    def write(self) -> None:
        print(f"I'm writting permanently with - {self.brand}")


class Pencil(ABC):
    def write(self) -> None:
        print(f"I'm writting with - {self.brand}")


class PenFaber(Pen):
    def __init__(self) -> None:
        self.brand = "Faber Castle"


class PencilFaber(Pencil):
    def __init__(self) -> None:
        self.brand = "Faber Castle"


class PenBic(Pen):
    def __init__(self) -> None:
        self.brand = "Bic"


class PencilBic(Pencil):
    def __init__(self) -> None:
        self.brand = "Bic"


def client(someClass):
    someClass.write()

# Aqui o código cliente conhece a classe concreta
if __name__ == "__main__":
    client(PencilFaber())
    client(PenFaber())
    print("---")
    client(PencilBic())
    client(PenBic())

    print("\nRevert\n")

    client(PencilFaber())
    client(PenBic())
    print("---")
    client(PencilBic())
    client(PenFaber())
