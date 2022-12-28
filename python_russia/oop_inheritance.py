from pprint import pprint as pp


# Наследование: механизм получения доступа к данным и поведению своего предка
# Если классы имеют много общего, тогда общий код выводим в базовый класс
# IS-A является
# HAS-A содержит (композиция)

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calc_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'{self.__class__.__name__}\t{self.name:<20}\tsalary={self.salary}, bonus={self.bonus}%, ' \
               f'total bonus={self.calc_total_bonus()} rub'


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, salary=15000, bonus=1)
        print(self.salary)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, salary=45000, bonus=15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, salary=105000, bonus=100)

    def calc_total_bonus(self):  # переопределили родительский метод
        return 200_000


class MyList(list):  # наследуем от встроенного класса "list" и все его атрибуты
    def __str__(self):  # замена штатного метода __str__
        return super().__str__().replace(',', ',\n')


# по умолчанию все классы наследуются от "object": class Empty(object):
# и наследуют всё окружение от object
class Empty:
    """
    Пустой класс.
    Получает все свойства от базового класса Питона "object"
    """
    pass


class Engine:
    pass


class Wheel:
    pass


class Car:
    def __int__(self):
        self.engine = Engine()
        self.wheels = [Wheel()] * 4


# демонстрация сохранения атрибутов __private при наследовании:
class First:
    def __init__(self):
        self._login = 'First_login'
        self.__password = 'First_password_text'


class Second(First):
    def __init__(self):
        super().__init__()
        self._login = 'Second_login'
        self.__password = 'Second_password_text'


if __name__ == '__main__':
    masha = Cleaner('Maria Ivanova')
    print(masha)
    grisha = Manager('Grigory Petrovich')
    print(grisha)
    vanya = CEO('Ivan Palych')
    print(vanya)
    print([1, 2, 3])
    my_list = MyList([1, 2, 3])
    print(my_list)
    my_list.extend([4, 5])  # метод унаследован от родительского "list"
    print(my_list)
    pp(dir(Empty()))  # пустой класс получит все свойства от "object"
    print(Empty.__doc__)
    first = First()
    second = Second()
    pp(dir(second))
    print(second._login)
    print(second._First__password)
    print(second._Second__password)


