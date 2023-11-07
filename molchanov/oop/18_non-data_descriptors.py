# Класс Person содержит избыточный код, с целью устранения
# создаем новый Класс для генерации атрибутов.
# Тогда, атрибуты класса Person становятся экземплярами того Класса.
# Это дескрипторы:
# non-data - get method only, не хранит состояние
# data - get, set

from time import time
from random import choice


class Person:
    """
    Person base Class
    Создание свойств имеет избыточный код: меняются только переменные.
    Можно заменить дескрипторами.
    """

    def __init__(self, name, surname) -> None:
        self._name = name
        self._surname = surname
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self._full_name = None


class Epoch:
    def __get__(self, instance, owner_class):
        return int(time())


class MyTime:
    epoch = Epoch()


mt = MyTime()
print(mt.epoch)


class Dice:
    """
    Игральный кубик
    """

    @property
    def number(self):
        return choice(range(1, 7))


dc = Dice()
print(dc.number)


# Класс с избыточным кодом:
class Games:
    @property
    def rock_paper_scissors(self):
        return choice(["Rock", "Paper", "Scissors"])

    @property
    def flip(self):
        return choice(["Head", "Tails"])

    @property
    def dice(self):
        return choice(range(1, 7))


gm = Games()
print(gm.flip)


class Choice:
    def __init__(self, *choice) -> None:
        self._choice = choice

    def __get__(self, obj, owner):
        return choice(self._choice)


class GamesChoice:
    """
    Non-data descriptors:
    """
    dice = Choice(1, 2, 3, 4, 5, 6)
    flip = Choice("Head", "Tails")
    rock_paper_scissors = Choice("Rock", "Paper", "Scissors")

gc = GamesChoice()
print(gc.flip)
print(gc.rock_paper_scissors)
