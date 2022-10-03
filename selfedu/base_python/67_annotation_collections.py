# Для указания типов для python3.8 и ранее, нужен модуль typing:
from typing import List, Tuple, Dict, Set, Union, Callable

# Callable - аннотация вызываемых объектов

# list, tuple, dict, set - основные типы коллекций
# Базовый способ:
lst_1: list = [1, 'One', True, None]  # работает, но непонятно, что внутри списка
#  Расширяем указание, (следующие записи эквивалентны):
lst_2: list[int] = [3, 5, 'Five', True]  # для python3.9 и новее
lst_3: List[int] = [11, 33, 77]  # для python3.8 и ранее

# у кортежей указать тип каждого элемента:
addr: tuple[int, str] = (9, 'some_string')
book_1: Tuple[str, str, int]
book_1 = ('Алдошина', 'Акустические системы и излучатели', 1995)
elems: Tuple[float, ...]  # многоточие указывает, что все элементы float
elems = (1.1,)
elems = (2.3, 4.2, 1001.05)

# словари: указать тип для ключей и значений (по аналогии со строками)
dic_1: Dict[str, int]  # для python3.8 и ранее
dic_1 = {'one': 1, 'four': 4, 'nine': 9}
dic_2: dict[int, int] = {3: 11, 5: 59, 144: 44444}  # для python3.9 и новее

# множества: по аналогии со строками
first_names: Set[str] = {'Polina', 'Svetlana', 'Oksana'}
ages: set[int] = {6, 26, 36}


def get_positives(digits: list[int]) -> list[int]:
    """
    возвращает только положительные числа
    :param digits: list[int]
    :return: list[int]
    """
    return list(filter(lambda x: x > 0, digits))


print(get_positives([10, -1, 0, 3, 99, 182, -90]))


def get_positive_2(digits: List[Union[int, float]]) -> List[Union[int, float]]:
    return [x for x in digits if x > 0]


print(get_positive_2([1.1, -30.03, 5.5, 10.01, 11]))


# Callable:
# часто это функции передаваемые как параметр
def get_digits(flt: Callable[[int], bool], lst: List[int] = None) -> List[int]:
    if lst is None:
        return []
    else:
        return list(filter(flt, lst))


print(get_digits(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


def even(x: int):
    return bool(x % 2 == 0)


print(get_digits(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
