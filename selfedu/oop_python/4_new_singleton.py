from pprint import pprint as pp


class Point:  # неявно наследуется от Класса object
    __instance = None  # ссылка на экземпляр Класса, для проверки есть ли уже экземпляр

    def __new__(cls, *args, **kwargs):
        '''
        __new__ всегда должен вернуть адрес созданнного объекта
        *args **kwargs - для передачи аргументов при создании экземпляров Класса
        :param args:
        :param kwargs:
        '''
        print(f'Вызов __new__ для: {cls=}')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # cls - ссылка на текущий Класс Point
        # вызовем __new__ у базового Класса object, на него укажет super():
        return cls.__instance

    def __del__(self):
        self.__instance = None

    def __init__(self, x=1, y=1):
        print(f'Вызов __init__ для {self=}')
        self.x = x
        self.y = y


pt1 = Point(3, 5)  # 3, 5 - сработают за счет наличия *args, **kwargs в методе __new__
print(pt1)
print(f'{pt1.x=}\n{pt1.y=}')
print(f'{id(pt1)=}')
print(pt1.__dict__)
pt2 = Point()
print(f'{id(pt2)=}')
del pt1
print(f'{id(pt2)=}')
del pt2
pt3 = Point(3, 3)
pt4 = Point(4, 4)  # атрибуты при создании последнего экземпляра перезапишут предыдущие !
print(f'{id(pt3)=}, {id(pt4)=}')
print(f'{pt3.__dict__=}, {pt4.__dict__=}')