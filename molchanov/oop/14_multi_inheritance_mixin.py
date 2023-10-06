# Diamond shape problem - проблема ромбовидной формы наследования
# Разрешение свойств и методов происходит слева на право
# в порядке перечисления наследования: class MyClass(Class1, Class2, .. ClassN):
# obj.__class__.__mro__ выведет порядок наследования
# Mixin - небольшой Класс, для расширения функционала других Классов
# как правило, не имеет своих экземпляров


class Person:
    """
    Base Class
    """

    def hello(self):
        print("\nHello from Person !\n")


class FavoriteFood:
    """
    Mixin Класс
    Добавляет функционал
    """

    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError("Food should be set")
        print(f"I like {self.food}")


class Student(FavoriteFood, Person):
    food = "Pizza"

    def hello(self):
        print("\nHello from Student !\n")


class Prof(Person):
    def hello(self):
        print("\nHello from Prof !\n")


class SomeOne(Student, Prof):
    pass


s = SomeOne()
s.hello()
print(s.__class__.__mro__)
s.get_food()
