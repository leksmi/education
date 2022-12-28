# функций (объект 1го класса) может быть использована как любой другой объект
# функция внутри функции может использовать объект вне себя
#

from pprint import pprint as pp


def example(some_func, a: int = 0) -> None:
    print(f'{some_func.__name__=}')

    def inner(b) -> None:
        print(a + b)

    inner(45)


def summ(a: int, b: int) -> int:
    """
    складывает два числа
    :param a: int
    :param b: int
    :return: int
    """
    return a + b


def logger(func):
    def wrapper(a, b):
        print(f'{func.__name__} has Started ..')
        result = func(a, b)
        print(f'{func.__name__} has Finished.')
        return result

    return wrapper


if __name__ == '__main__':
    function = summ
    print(summ)
    print(function)
    example(summ, 45)
    # example()
    function = logger(summ)
    print(function)
