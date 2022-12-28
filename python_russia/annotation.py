from typing import List, Union, Optional, Any


# Union - указанные в [] типы
# Optional - может быть None или указанные в [] типы
# Any - вернет любые данные

def example(*args) -> Any:
    return args


def calc(a: Optional, b: Union[int, float]) -> Union[int, float]:
    return a + b


def to_int(a_list: list[str]) -> List[int]:  # начиная с py3.9 mod. typing не обязателен: list[int]
    return [int(j) for j in a_list]


if __name__ == '__main__':
    print(example(2, 7, '101'))
    print(example([1, 2, 3, 4, 5], (7, 8, '888')))
    print(calc(1, 7))
    print(to_int(['10', '11', '33']))
