# Пространство имен - это словарь, где записаны ссылки на объекты в памяти
# Область видимости - это путь для поиска имени в пространстве имен,
# фактически перечень словарей. Тут работает правило LEGB:
# Local
# Enclosed
# Global
# Builtin
# Есть 3 исключения, одно из них это определение Класов:
# Unbound local variables (несвязанные локальные переменные) разрешаются (ищутся) из Глобального пространства !
# Это следствие того, что у Класса свое пространство имен, у экземпляра свое, они изолированы друг от друга
# Иначе говоря, пространство имен Класса не является Enclosed областью для его функций,
# т.е. находятся наодном уровне.

from rich import print, inspect

name = "Ivan"


class Person:
    """
    Класс имеет свое пространство, тут есть name
    """

    name = "Dima"

    def print_name(self) -> None:
        """
        Метод имеет свое пространство, и name отсутствует !
        тут name это Unbound local variable, так как на момент вызова она не создана
        """
        print(f"{name=}")

    def print_name_self(self) -> None:
        """
        Прочитать переменную Класса можно через self
        Но только прочитать. При записи через self создается своя локальная переменная экземпляра
        """
        print(f"{self.name=}")

    @classmethod
    def change_class_attrib(cls, new_name) -> None:
        """
        Полноценное взаимодействие с переменными Класса возможно декорированием функции как @classmethod
        Данный декоратор связывает функцию с Классом, но не с экземпляром,
        после чего эта функция становится методом Класса.
        Метод Класса видит пространство имен только Класса, и не видит экземпляры.
        Предназначен для работы со свойствами Класса.
        """
        cls.name = new_name
        print(f"{cls.name=}")  # вывод измененного атрибута Класса


p = Person()
p.print_name()
p.print_name_self()
print(f"\n{Person.__dict__=}\n{p.__dict__=}\n")
p.change_class_attrib(new_name="Sasha")
print(f"\n{Person.__dict__=}\n{p.__dict__=}")


class Person2:
    def __init__(self, name) -> None:
        self.name = name

    @classmethod
    def from_file(cls, path):
        """
        Получаем name из файла
        Возвращаем Класс с этим атрибутом
        """
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_obj(cls, obj):
        """
        Получаем name из другого объекта
        Если нужный атрибут найден, возвращаем Класс с этим атрибутом
        Иначе, возвращаем просто Класс
        """
        if hasattr(obj, "name"):
            name = getattr(obj, "name")
            return cls(name=name)
        return cls


class Config:  # сторонний Класс для извлечения атрибута
    name = 'Alena'

pa = Person2.from_obj(Config)
print(f'{pa.__dict__=}')