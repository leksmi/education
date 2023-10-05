#
#
#


class Person:
    """
    1-й вариант:
    Использование Класса property
    """

    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        """
        Для реализации геттера
        """
        print(f"Getter shows: {self._name}")
        return self._name

    def set_name(self, new_name: str) -> None:
        """
        Для реализации сеттера
        """
        print(f"Setter changing: {self._name}")
        self._name = new_name
        print(f"to: {self._name}")

    # создаем объект Класса property, с передачей ранее созданных функций
    # которым управляем одноименным атрибутом
    name = property(fget=get_name, fset=set_name)


class Person2:
    """
    2-й вариант:
    Использование декоратора property
    """

    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        """
        Для реализации геттера
        """
        print(f"Getter shows: {self._name}")
        return self._name

    def set_name(self, new_name: str) -> None:
        """
        Для реализации сеттера
        """
        print(f"Setter changing: {self._name}")
        self._name = new_name
        print(f"to: {self._name}")

    # создаем объект Класса property
    name = property()
    # переопределяем его с выполнением метода getter:
    name = name.getter(get_name)
    # повторно переопределяем его с выполнением setter:
    name = name.setter(set_name)


class Person3:
    """
    3-й вариант:
    Использование декоратора property
    """

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        """
        Реализация геттера
        """
        return self._name
    # в результате работы предыдущего декоратора,
    # name становится экземпляром Класса property
    # у которого в следующем декораторе вызываем метод .setter
    # и декорируем им функцию с одноименным названием
    @name.setter
    def name(self, new_name: str):
        """
        Реализация сеттера с помощью вызова метода у ранее
        созданного name, который является экземпляром Класса property
        """
        self._name = new_name


p3 = Person3('Fedora')
print(f'{p3.name=}')
p3.name = 'Astra'
print(f'{p3.name=}')
