from abc import ABC, abstractmethod



class QuadriLateral:
    """
    Base class
    """

    def __init__(self, a, b, c, d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def perimeter(self):
        p = self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=", p)


class Rectangle(QuadriLateral):
    """
    Child class
    """

    def __init__(self, a, b):
        super().__init__(a, b, a, b)

    def area(self):
        a = self.side1 * self.side2
        print("area of rectangle=", a)


class Square(Rectangle):
    """
    Another child class.
    """

    def __init__(self, a):
        super().__init__(a, a)

    def area(self):
        a = pow(self.side1, 2)
        print("area of Square=", a)


s1 = Square(10)
s1.area()
print(s1.__class__.__mro__)


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def __init__(self, n) -> None:
        self.number = n
    
    def noofsides(self):
        print(f'I have {self.number} sides')

class Pentagon(Polygon):
    def __init__(self, n) -> None:
        self.number = n

    def noofsides(self):
        print(f'I have {self.number} sides')


tr = Triangle(3)
tr.noofsides()
pt = Pentagon(5)
pt.noofsides()

