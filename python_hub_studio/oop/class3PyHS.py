from datetime import datetime


class Player:
    __LVL = 1
    __HEALTH = 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()

    @property
    def lvl(self):  # getter
        return self.__lvl, f'{datetime.now() - self.__born}'

    @lvl.setter
    def lvl(self, num):  # setter
        self.__lvl = num
        if self.__lvl >= 100:
            self.__lvl = 100

    @classmethod
    def set_cls_fields(cls, lvl=1, health=100):
        cls.__LVL = cls.__typeTest(lvl)
        cls.__HEALTH = cls.__typeTest(health)

    @classmethod
    def show_cls_fields(cls):
        print(f'Level: {cls.__LVL}\nHealth: {cls.__HEALTH}')

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise ValueError('Must be integer')


if __name__ == '__main__':
    p1 = Player()
    print(p1.lvl)
    p1.lvl = 107
    print(p1.lvl)
    p1.set_cls_fields()
