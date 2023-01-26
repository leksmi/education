# @staticmethod не имеет ссылок ни на Класс ни на объект
# по сути статикметод это обычная функция работающая с указанными параметрами
from pprint import pprint


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x: int = 0, y: int = 0):
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        else:
            raise ValueError('Координаты вне диапазона')
        # статикметод можно использовать внутри класса в любом месте:
        print(f'{self.norm2(self.x, self.y)=}')

    @classmethod
    def validate(cls, arg) -> bool:
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x: int, y: int) -> int:  # просто вспомогательная функция
        return x * x + y * y

    def get_coord(self) -> tuple:
        return self.x, self.y


v = Vector(11, 22)
res = v.get_coord()
print(f'{type(res)=}; {res=}')
print(f'{v.validate(10)=}')
print(f'{v.validate(101)=}')
pprint(dir(v))
print(f'{type(v.validate)=}\n{type(v.get_coord)=}')
print(f'{v.norm2(v.x, v.y)=}')

