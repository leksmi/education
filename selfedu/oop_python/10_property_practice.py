from pprint import pprint as pp
from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, old: int, ps: str, weight):
        self.verify_fio(fio)
        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio: str):
        if type(fio) != str:
            raise TypeError('Ошибка: ФИО нужно указать строкой')
        f: list = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи ФИО')
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('ФИО должен быть 1 и более символов')
            if len(s.strip(letters)) != 0:
                raise TypeError('ФИО может содержать только буквы и дефис')

