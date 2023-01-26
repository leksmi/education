from pprint import pprint as pp
from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, old: int, ps: str, weight: int):
        self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_ps(ps)
        # self.verify_weight(weight)

        self.__fio = fio.split()
        # self.__old = old
        # self.__passport = ps
        # self.__weight = weight
        # вместо прямого обращения к приватным атрибутам и проверки ранее, используем сеттеры со встроенной проверкой:
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio: str):
        if type(fio) != str:
            raise TypeError('Ошибка: ФИО нужно указать строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('ФИО должен быть 1 и более символов')
            if len(s.strip(letters)) != 0:
                raise TypeError('ФИО может содержать только буквы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or not 14 < old < 120:
            raise TypeError('Возраст должен быть целым числом в диапазоне 14-120')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != int or w < 20:
            raise TypeError('Вес должен быть целым числом от 20 и выше')

    @classmethod
    def verify_ps(cls, ps: str):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')

        ps_lst = ps.split()
        if len(ps_lst) != 2 or len(ps_lst[0]) != 4 or len(ps_lst[1]) != 6:
            raise TypeError('Неверный формат паспорта')

        for p in ps_lst:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old: int):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps: str):
        self.verify_ps(ps)
        self.__passport = ps


p = Person('Семенов Семен Семенович', 33, '4233 456789', 88)
print(p.__dict__)
p.old = 45
p.passport = '4567 123456'
p.weight = 91
print(p.__dict__)  # после изменений сеттерами
print(f'{p.old=}')
