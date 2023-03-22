#
#

from rich import print, inspect


class SomeDemo:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'


class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self) -> str:  # для программистов
        """
        __repr__ показывает вид объекта. Является строкой. Используется функцией repr()
        :return:
        """
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self) -> str:  # для людей. Его использует функция print()
        """
        __str__ возвращает произвольную строку. Используется функцией str()
        Если нет __str__() текстовое представление берется из __repr__()
        :return:
        """
        return f'Банкнота номиналом {self.value} рублей'

    def __eq__(self, other) -> bool:
        """
        Разработчик определяет, что именно будем сравнивать (обычно все атрибуты)
        :param other: экземпляр данного Класса
        :return:
        """
        if other is None or not isinstance(other, self.__class__):
            raise TypeError('Data type error')
        else:
            return self.value == other.value  # other ожидаем экземпляр нашего Класса.

    # методы ниже так же нужно делать с проверкой:
    # if other is None or not isinstance(other, self.__class__):
    def __lt__(self, other) -> bool:
        """
        Определение меньше чем
        :param other: экземпляр данного Класса
        :return: bool
        """
        if other is None or not isinstance(other, self.__class__):
            raise TypeError('Data type error')
        else:
            return self.value < other.value

    def __gt__(self, other) -> bool:
        """
        Определение больше чем
        :param other: экземпляр данного Класса
        :return: bool
        """
        if other is None or not isinstance(other, self.__class__):
            raise TypeError('Data type error')
        else:
            return self.value > other.value

    def __le__(self, other) -> bool:
        """
        Определение меньше или равно чем
        :param other: экземпляр данного Класса
        :return: bool
        """
        if other is None or not isinstance(other, self.__class__):
            raise TypeError('Data type error')
        else:
            return self.value <= other.value

    def __ge__(self, other) -> bool:
        """
        Определение больше или равно чем
        :param other: экземпляр данного Класса
        :return: bool
        """
        if other is None or not isinstance(other, self.__class__):
            raise TypeError('Data type error')
        else:
            return self.value >= other.value


if __name__ == '__main__':
    bn10 = Banknote(10)
    bn50 = Banknote(50)
    bn100 = Banknote(100)
    print(bn10, '\n', bn50)
    print('\n', f'{bn10!r}', '\n', f'{bn50!r}')  # !r - возвращает результат __repr__()
    rebuilt_bn10 = eval(repr(bn10))  # восстанавливает объект
    print('\nОтображение rebuilt_bn10:', rebuilt_bn10)
    bn50_2 = Banknote(50)
    print(bn50 == bn50_2)  # по умолчанию сравнит объекты (ячейки в памяти). Нужно добавить __eq__()
    print(bn50 == bn100)
    print(bn50 > bn100)  # требует методы __lt__, __gt__, __le__, __ge__
    ed100 = SomeDemo(100)
    print(ed100)
    print(bn100 >= ed100)  # TypeError: Data type error
