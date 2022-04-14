class Cat:
    def hello():
        print('Hello world from cat !')


bob = Cat()

print(Cat.hello)
print(bob.hello)


class Cat:
    def hello(*args):
        print(f'Hello world from cat !  {args}')


jim = Cat()
jim.hello()
print(jim)


class Cat:
    breed = 'pers'

    def hello(*args):
        print(f'Hello world from cat !  {args}')

    def sh_breed(instance):
        print(f'My breed is {instance.breed}')

    def sh_name(instance):
        if hasattr(instance, 'name'):
            print(f'My name is {instance.name}')
        else:
            print('No name !')

    def set_value(object_name, value, age=0):
        object_name.name = value
        object_name.age = age


walt = Cat()
walt.breed = 'siam'
walt.sh_breed()
bob = Cat()
bob.sh_breed()

tom = Cat()
tom.sh_name()  # no name !
tom.set_value('TOM')  # make name
tom.sh_name()
print(tom.name)

jerry = Cat()
# print(jerry.age) # error because of set_value did not work !
jerry.set_value('JERRY')
jerry.sh_name()
print(jerry.age)


class myCat:
    breed = 'pers'

    def hello(self):
        print(f'Hello world from cat !  {self}')

    def sh_breed(self):
        print(f'My breed is {self.breed}')

    def sh_name(self):
        if hasattr(self, 'name'):
            print(f'My name is {self.name}')
        else:
            print('No name !')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def sh_name_age(self):
        print(f'My name is {self.name} and my age is {self.age}')


kitty = myCat()
kitty.set_value('KITTY', age=3)
kitty.sh_name_age()


class Counter:
    n = 0

    def start_from(self, i=0):
        self.n = i

    def increment(self):
        self.n += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.n}")

    def reset(self):
        self.n = 0


class Point:
    def set_coordinates(self, a=0, b=0):
        self.x = a
        self.y = b

    def get_summ(self, obj):
        if hasattr(obj, 'x'):  # проверка на True/False
            print(self.x + self.y + obj.x + obj.y)
        else:
            print("Передана не точка")

