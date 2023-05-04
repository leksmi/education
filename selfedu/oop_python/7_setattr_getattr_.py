import logging

logging.basicConfig(level=logging.DEBUG,
                    datefmt='%(asctime)s %(levelno)s %(message)s'
                    )


class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        # автоматически вызывается при считывании атрибута экземпляра Класса
        # переопределяем через базовый object:
        logging.info(msg='Вызов метода __getattribute__')
        if item == 'x':
            raise ValueError('Attribute access denied')
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        # срабатывает при обращении к несуществующему атрибуту
        logging.info(msg='Вызов метода __getattr__')
        # возвращаем то, что нам удобно, например False
        # return False
        return 'There is no attribute'

    def __setattr__(self, key, value):
        # автоматически вызывается при назначении атрибута экземпляра Класса
        # можно запретить установку определенных атрибутов
        logging.info(msg='Вызов метода __setattr__')
        if key == 'j':
            raise AttributeError('Not allowed attribute name')
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        # автоматически вызывается при назначении атрибута экземпляра Класса
        logging.info(msg='Вызов метода __delattr__')
        object.__delattr__(self, item)

    def set_coord(self, new_x, new_y):
        if self.MIN_COORD <= new_x <= self.MAX_COORD:
            self.x = new_x
        else:
            raise ValueError(f'Should be in {self.MIN_COORD} to {self.MAX_COORD}')
        if self.MIN_COORD <= new_y <= self.MAX_COORD:
            self.y = new_y
        else:
            raise ValueError(f'Should be in {self.MIN_COORD} to {self.MAX_COORD}')

    @classmethod
    def set_bound(cls, new_min):
        cls.MIN_COORD = new_min


pt = Point(11, 22)
print(pt.__dict__)
pt.set_bound(new_min=20)
print(pt.__dict__)
# pt.set_coord(15, 17)
print(pt.__dict__)
# print(pt.x)  # raise ValueError('Attribute access denied')
print(pt.y)  # сработает
print(pt.f)
del pt.y
