from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def measures(self):
        pass


class Circle(Shape):
    def area(self):
        return 3.14 * (7 ** 2)

    def measures(self):
        return f"Raio: 7cm"


class Rectangle(Shape):
    def area(self):
        return 7 * 9

    def measures(self):
        return f"Altura: 7cm e Largura: 9cm"


class Square(Shape):
    def area(self):
        return 7 * 7

    def measures(self):
        return f"Altura: 7cm e Largura: 7cm"


def factory_function(ShapeType: str):
    if ShapeType == "circle":
        return Circle()
    if ShapeType == "rectangle":
        return Rectangle()
    if ShapeType == "square":
        return Square()


if __name__ == "__main__":
    shape = input("Qual tipo de shape você quer?\n")
    area = factory_function(shape).area()
    measures = factory_function(shape).measures()
    print(f"{area}cm²")
    print(measures)
