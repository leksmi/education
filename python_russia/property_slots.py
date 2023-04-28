from pympler import asizeof


class Cat:
    # FIELDS = ('name', 'age')  # список допустимых свойств экземпляра
    # Python не экономичен с памятью, нужно использовать:
    __slots__ = ('_name', '_age')  # уменьшает занимаемую память

    def __init__(self, name: str, age: int):
        # if not name.strip():
        #     raise AttributeError('Name is required')
        # if age < 1 or age > 15:
        #     raise AttributeError('Age should be in 1 to 15 years')
        self.name = name
        # self._name = name
        self.age = age
        # self._age = age

    def __repr__(self):
        return f'Cat(name={self.name}, age={self.age})'

    # def __setattr__(self, key, value):
    #     """
    #     Вызывается при манипуляциях с атрибутами,
    #     в т.ч. через __init__
    #     :param key:
    #     :param value:
    #     :return:
    #     """
    #     # проверка на допустимость атрибута:
    #     if key not in self.FIELDS:
    #         raise AttributeError(f'Allowed only: {self.FIELDS}')
    #     if key == 'name' and not value.strip():
    #         raise AttributeError('Name is required')
    #     if key == 'age' and (value < 1 or value > 15):
    #         raise AttributeError('Age should be in 1 to 15 years')
    #     self.__dict__[key] = value

    # @property приоритетнее __setattr__
    # формирование атрибутов через @property:
    @property
    # это геттер, название метода соответствует имени атрибута:
    def name(self):  # название соответствует атрибуту !
        # чтобы название не совпадало с геттером, добавить "_"
        return self._name

    # декоратор сеттера пишется как: имя_атрибута.setter
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise AttributeError('Name can not be empty')
        self._name = value

    @property
    # это геттер, название метода соответствует имени атрибута:
    def age(self):  # название соответствует атрибуту !
        # чтобы название не совпадало с геттером, добавить "_"
        return self._age

    # сеттер для age:
    @age.setter
    def age(self, value: int):
        if value < 1 or value > 15:
            raise AttributeError('Age should be in 1 to 15 years')
        self._age = value


if __name__ == '__main__':
    tom = Cat(name='Tom', age=2)
    push = Cat('Pushok', 3)
    print(tom)
    tom.name = 'Barsik'
    print(tom)
    # print(tom.__dict__)  # при использовании __slots__ то __dict__ отсутствует - не создается
    # т.е. не создается словарь атрибутов
    # tom.name_2 = 'Secondary name' # отсутствует в __slots__
    print(asizeof.asizeof(tom))
    print(asizeof.asizeof(push))