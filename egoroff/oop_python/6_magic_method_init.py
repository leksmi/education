class Cat:
    breed = 'pers'

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self):  # выполняется автоматически каждый раз при вызове класса
        print(f'Method __init__ has worked for: {self}')


Cat()  # вызов класса на исполнение. Но, так как результат работы не присвоен переменной,
# он сразу удаляется сборщиком мусора

kitty = Cat()  # при создании экземпляра класса, сам класс вызывается на выполнение скобками - ()
print(kitty)
print(kitty.__dict__)
tom = Cat()  # при создании экземпляра класса, сам класс вызывается на выполнение скобками - ()
print(tom)
print(tom.__dict__)


# __init__ для определения переменных при запуске класса
class Cat:

    def __init__(self, name, breed='pers', age=1,
                 color='white'):  # выполняется автоматически каждый раз при вызове класса
        print(f'Method __init__ has worked for: {self}')
        print(f'New Cat object with: name={name} breed={breed} age={age} color={color}')
        # определяем переменные:
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color


kitty = Cat('Kitty')
print('\n' * 2)
walt = Cat('Walt')


class Laptop:
    def __init__(self, manufac, model_name, price_val):
        self.brand = manufac
        self.model = model_name
        self.price = price_val
        self.laptop_name = f'{manufac} {model_name}'


class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


class Zebra:
    def __init__(self):
        self.count = 0

    def which_stripe(self):
        if self.count % 2 == 0:
            print("Полоска белая")
        else:
            print("Полоска черная")
        self.count += 1


class Person:
    def __init__(self, f_name: str, l_name: str, years: int):
        self.first_name = f_name
        self.last_name = l_name
        self.age = years

    def full_name(self) -> str:  # подсказка типа - typing
        return f'{self.last_name} {self.first_name}'

    def is_adult(self) -> bool: # return boolean-type
        return self.age >= 18


