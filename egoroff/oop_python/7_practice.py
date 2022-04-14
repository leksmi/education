class Point:
    def __init__(self, coord_x=0, coord_y=0):  # отрабатывает при создании объекта (запуске класса)
        # self.x = coord_x
        # self.y = coord_y
        # вместо присвоений выше, можно вызвать объявленный метод:
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        # self.x = 0
        # self.y = 0
        # вместо присвоений выше, можно вызвать объявленный метод:
        self.move_to(0, 0)


pt1 = Point()
pt2 = Point(5, 9)
pt2.go_home()


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.sound = ''

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound: str):
        self.sound = sound
        return f"{self.name} says {self.sound}"


#
# Декораторы
#
def my_decorator(some_func):  # внешняя функция, принимающая аргументом другую функцию
    # затем функция-обертка которая выполняет свои действия, затем вызывает
    # на исполнение декорируемую функцию
    def wrapper():
        print('Hello user !')
        some_func()  # запускаем на выполнение декорируемую функцию
        print('Goodby user !')

    # далее возвращаем функцию-обертку
    # так как обертка возвращается как объект, далее ее потребуется запускать через ()
    return wrapper

@my_decorator # за этой строкой идет функция, которая будет автоматически подставлена на место some_func
def show_strings():  # функция, которую будем декорировать
    print('''
    the beginning !
    Some string ONE
    Some string TWO
    Somw string THREE
    the end !''')

# для возможности декорируемой функции принимать любые аргументы (позиционные и/или ключевые)
# используем *args **kwargs
def my_decorator2(some_func):  # внешняя функция, принимающая аргументом другую функцию
    # затем функция-обертка которая выполняет свои действия, затем вызывает
    # на исполнение декорируемую функцию
    def wrapper(*args, **kwargs): # указываем возможные параметры
        print('Hello user !')
        # запускаем на выполнение декорируемую функцию
        # и передаем возможные аргументы
        some_func(*args, **kwargs)
        print('Goodby user !')

    # далее возвращаем функцию-обертку
    # так как обертка возвращается как объект, далее ее потребуется запускать через ()
    return wrapper

@my_decorator2
def show_tth(model, eng, manuf):
    print(f'Auto data:\nModel: {model}\nEngine: {eng}\nManufacturer: {manuf}')
a = 10
from pprint import pprint
pprint('abc')
d1 = {'a': 10, 'b': 'C'}