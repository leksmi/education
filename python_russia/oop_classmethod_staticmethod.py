# LEGB-rule работает и внутри классов, если self НЕ указан:
max = lambda x: x[-1]  # redefine built-in function "max" !


# изменение Неизменяемых атрибутов Класса создает локальный атрибут Объекта
# изменение Изменяемых атрибутов Класса модифицирует атрибут Класса (список, словарь ..)
# для изменения атрибута класса нужно использовать имя класса: Class.attrib = значение
# или декоратор @classmethod - для работы со свойствами Класса
#
# @staticmethod - не получает ссылок (cls или self). Это функция контекстом связанная с Классом.

class BlueCat:
    breed = 'Russian Blue'  # задает общий атрибут для всех объектов
    names = []  # изменяемый атрибут класса, общий для всех объектов
    count = 0  # статическое свойство Класса

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.names.append(name)  # при каждом создании объекта добавляется аргумент name
        self.increment_count()

    def meow(self):
        print(f'{self.name}`s breed is {self.breed} and he says Meow !')

    def get_maximum(self):
        print(max([1, 3, 7, 4]))

    @classmethod
    def increment_count(cls, cnt=1):  # cls указывает на ссылку класса
        cls.count += cnt  # изменение статического поля Класса

    @classmethod
    def make_cat(cls, name):
        if name == 'Tom':
            print(f'{cls.__name__=}')
            return cls('Tom', 2)
        elif name == 'Funtik':
            print(f'{cls.__name__=}')
            return cls('Funtik', 1)
        return cls('SomeCat', 1)

    @staticmethod
    def get_human_age(age):  # нет ссылки ни на класс (cls) ни на объект (self)
        return age * 8

    def get_name(self, name):  # это тоже статик метод, так как self не задействован
        print(f'{name=}')


if __name__ == '__main__':
    # tom = BlueCat(name='Tom', age=2)
    tom = BlueCat.make_cat('Tom')
    tom.breed = 'Perse'  # создаст локальное свойство объекта "том"
    tom.meow()
    # funtik = BlueCat(name='Funtik', age=1)
    funtik = BlueCat.make_cat('Funtik')
    funtik.meow()
    print(f'\n{id(tom.names)=}\n{id(funtik.names)=}\n')
    print(f'{BlueCat.count=}')  # количество созданных объектов класса
    human_age = BlueCat.get_human_age(funtik.age)  # вызов через класс
    print(f'{human_age=}')
    human_age2 = tom.get_human_age(tom.age)  # вызов через объект
    print(f'{human_age2=}')
