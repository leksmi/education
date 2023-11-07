# super() предоставляет доступ к свойствам и методам родительского Класса
# при вызове метода через super, он связывается с экземпляром дочернего Класса


class Person:
    """
    Base human Class
    """

    def __init__(self, name) -> None:
        self.name = name


class Student(Person):
    """
    SubClass to make students
    """

    def __init__(self, name, surname):  # нужно передать все аргументы, в том числе для методов родительского Класса
        # super возвращает proxy_obj родительского Класса:
        super().__init__(name)
        # инициализация свойств собственно дочернего Класса:
        self.surname = surname


st = Student("Ivan", "Ivanov")
print(st)
print(st.__dict__)
print("Resolution order:\n", st.__class__.__mro__)


class Person2:
    var_p2 = "I am Person2 var"

    def hello(self):
        print(f"Bound with: {self}")


class SomeOne(Person2):
    def hello(self):
        print(f"SomeOne obj.hello() has called")
        # обращение к методу родительского Класса
        super().hello()
        # обращение к свойству
        print(f"Свойство родительского Класса:\n{super().var_p2}")


st2 = SomeOne()
st2.hello()
print(f"\nst2 is: {hex(id(st2))}")
