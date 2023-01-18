from pprint import pprint as pp


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(fget=get_old, fset=set_old)


p = Person('Sergei', 20)
p.__dict__['old'] = 'old in object <p>'
a = p.old  # property выше приоритетом чем локальные свойства объекта ! Поэтому обращение к сеттеру get_old !
p.old = 35  # property выше приоритетом чем локальные свойства объекта ! Поэтому обращение к сеттеру set_old !
print(f'{p.old=}', f'\nСвойства объекта: {p.__dict__}')


#  Реализация через декораторы property:
class DataBase:
    def __init__(self, value_1, value_2):
        self.__val1 = value_1
        self.__val2 = value_2

    @property  # высегда пишется перед геттером ("точка входа")
    def val1(self):
        """
        get value 1
        :return:
        """
        return self.__val1

    @val1.setter  # реализация сеттера
    def val1(self, number):
        """
        set value 1
        :param number:
        :return:
        """
        self.__val1 = number

    @val1.deleter  # реализация делиттера
    def val1(self):
        del self.__val1


d1 = DataBase(33, 55)
print(d1.val1)  #  вызов геттера
d1.val1 = 44  #  вызов сеттера
print(f'{d1.val1=}')
print(d1.__dict__)
del d1.val1  #  вызов делиттера
print(d1.__dict__)
