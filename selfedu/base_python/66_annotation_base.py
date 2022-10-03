from typing import Union, Optional, Any, Final  # для гибкого указания типов

# Union - список типов допустимых данных
# Optional - возможность указать None
# Any - любой тип данных
# Final - для указания объектов не подлежащих изменению:
MAX_VALUE: Final = 1000

# аннотация переменных:
cnt: int = 10  # указываем, что ожидаем тип int
cnt_2: float = 10.5

# cnt = 0
msg: str = 'hello'
lst = [1, 2, 3]

print(type(cnt))
print(type(lst[0]), id(lst[0]))
print(type(lst[1]), id(lst[1]))
print(type(lst[2]), id(lst[2]))

cnt = 5.3  # ранее указали как int, сейчас объявили как float => IDE ругается
print(type(cnt))


# аннотация функций:
def mul2(x):
    # x может быть разным типом данных (примеры ниже)
    # но, можно конкретизировать, что именно передавать аргументом
    return x * 2


n: int = 5
s1: str = 'some string'
l1: lst = [2, 5, 9]
print(f'Result mul2 for {n} (type: {type(n)}) is: {mul2(n):>26}')
print(f'Result mul2 for {s1} (type: {type(s1)}) is: {mul2(s1):>{len(s1)}}')
print(f'Result mul2 for {l1} (type: {type(l1)}) is: {mul2(l1)}')


def mul2_new(x: Union[int, float], y: float = 2.2, mess: str = 'Result') -> str:
    # аргументом ожидаем целое или вещественное число
    # аннотация позволяет получить подсказки от IDE по атрибутам данных
    return f'{mess} : {x * 2 + y}'


# Вместо указания Union в теле блока кода, его можно вынести через алиас:
Digit = Union[int, float]
# Вариант с None:
StrType = Union[str, None]  # данная конструкция заменяется на Optional:


def multiple(x: int | float, y: Union[int, float] = 0, mess: Optional[str] = None) -> Union[int, float]:
    if mess:
        print(mess)
        res = x * 2 + y
        if res < MAX_VALUE:
            return res
        else:
            print('Overloaded !')
            return res
    else:
        return x * 2 + y


# атрибут __annotations__ :
print(mul2.__annotations__)  # выведет пустой словарь
print(mul2_new.__annotations__)  # выведет словарь вида параметр:класс_данных

print(multiple(5))
print(multiple(501, mess='Умножаем на 2:'))
