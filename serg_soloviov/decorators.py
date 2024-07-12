import functools
import time
from typing import Any


# Декораторы без параметров:
def deco(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('I am deco decorator, start')
        result = func(*args, **kwargs)
        print('I am deco decorator, finished')
        return result
    return wrapper


def deco2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('I am Deco2 decorator, start')
        result = func(*args, **kwargs)
        print('I am Deco2 decorator, finished')
        return result
    return wrapper


@deco
def my_func():
    return 1


# Стекирование декораторов: выполняются в порядке написания стека.
@deco2
@deco
def summator(a: int, b: int) -> int:
    """
    My summator. To get summ with two integers.
    :param a: int
    :param b: int
    :return: int
    """
    print('I am getting summary with a and b now')
    return a + b


@deco
def square(a: int) -> int:
    """
    My square calculator.
    :param a: int
    :return:
    """
    return a * a


# Запуск функции со стеком декораторов:
print(summator(a=100, b=105))

# Декоратор с параметрами
def logger(name: str):
    def inner(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            print(f'{name}: {time.perf_counter() - start_time}')
            return result
        return wrapper
    return inner


@logger(name='HeLLo')
def say_hello(message: str):
    print('I am making the greeting message')
    time.sleep(3)
    return f'Hello {message}'


say_hello('my friend')
say_hello('to your respect')