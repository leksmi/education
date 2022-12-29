class Person:
    name = 'Adam'

    def breath(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')


class Doctor(Person):
    def breath(self):
        print('Доктор дышит')


d1 = Doctor()
p1 = Person()
d1.walk()
p1.walk()
d1.breath()
p1.breath()
print(f'{p1.name=}\n{d1.name=}')


class Person_2:
    def __init__(self, name):
        print('Вызван __init__ Person_2')
        self.name = name

    def breath(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')


class Architect(Person_2):
    name = 'Ivan'

    def breath(self):
        print('Архитектор дышит')

    def __str__(self):
        return f'Architect {self.name}'


p2 = Person_2('Adam')
a1 = Architect('John')  # Architect не имеет своего __init__, поэтому возьмет родительский
print(f'{p2.name=}\n{a1.name=}')
print(p2, a1, sep='\n')
