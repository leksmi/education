# Перегрузка - создание в подКлассах свойств и методов с теми же именами,
# что и в родительском Классе.
# * скорее всего это известно как Overwriting
# Расширение - добавление новых свойств и методов, которых нет в родительском Классе


class CPU:
    """
    Base Class
    """

    chip_type = "CPU core chip"


class IntelCPU(CPU):
    """
    Sub Class
    """

    cpu_socket = 1151
    name = "Intel"

    def hello(self):
        """
        Метод, имя которого используем и в подКлассах
        """
        print(f"\nHello from {self.__class__.__name__} Class !")


class I7(IntelCPU):
    """
    Sub Class
    """

    def hello(self):
        print(f"\nHello from {self.__class__.__name__} Class !")


class I5(IntelCPU):
    """
    Sub Class
    """

    def hello(self):
        print(f"\nHello from {self.__class__.__name__} Class !")


i5 = I5()
i7 = I7()
print(f"\nПроверка принадлежности объекта:\t{isinstance(i5, IntelCPU)=}")
print(f"\nПроверка на подКласс:\t\t\t{issubclass(I5, CPU)=}")
print(f"\nПроверка принадлежности экземпляра Классу:\t{type(i5)=}")
print(f"\nПроверка, что два объекта от одного Класса:\t{isinstance(i7, type(i5))=}")
print("\n" * 3)
i = IntelCPU()
i.hello()
i5.hello()
i7.hello()


class Person:
    def __init__(self, name) -> None:
        self.name = name
    def hello(self):
        print(f'\nHello from: {self.name}')

class Student(Person):
    pass

s = Student('Semen')
# подКласс Student не имеет свой __init__, поэтому он взят из Person,
# Но, свойства и методы связываются с экземпляром s от Student:
s.hello()
print(s.__dict__)
