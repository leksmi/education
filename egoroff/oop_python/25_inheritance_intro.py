class Person:  # parent class
    def can_breathe(self):
        print(f'Я {self.__class__.__name__} и могу дышать')

    def can_walk(self):
        print(f'Я {self.__class__.__name__} и могу ходить')


class Doctor(Person):  # subclass
    def can_cure(self):
        return f'Я {self.__class__.__name__} и могу лечить'


class Ortoped(Doctor):  # унаследует Doctor -> Person -> object
    pass


class Architect(Person):  # subclass
    def can_build(self):
        return f'Я {self.__class__.__name__} и могу строить'


doc = Doctor()
print(f'{doc.__dict__=}')
print(dir(doc))
print(doc.can_cure())
#
arch = Architect()
print(f'{arch.__dict__=}')
print(dir(arch))
arch.can_walk()
#  Проверка на сабкласс (вернет bool):
print(issubclass(Doctor, Person))
print(issubclass(Person, Doctor))
print(issubclass(Architect, Person))
# Проверка на принадлежности объекта классу (вернет bool):
print(isinstance(doc, Doctor))
print(isinstance(arch, Architect))
print(isinstance(arch, Person))  # рекурсивно через Architect найдет принадлежность к Person
#
ort = Ortoped()
print(ort.can_cure())
ort.can_walk()
