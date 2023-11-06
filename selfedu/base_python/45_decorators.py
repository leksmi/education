# Декораторы функций
import time


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- Decorator starts working ---")
        result = func(*args, **kwargs)
        print("--- Decorator has finished working ---")
        return result

    return wrapper


def some_func(title: str, tag: str) -> str:
    print(f"Some_func with {title} working, {tag=}")
    return f"The title is: {title}; {tag=}"


# some_func = func_decorator(some_func)
# print("\n", some_func, some_func.__name__, sep="\n")
# some_func("Title", "HEADER")


def timer_decorator(func):
    """
    Декоратор для измерения времени работы функций
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"\nВремя выполнения функции: {stop - start}")
        return result

    return wrapper


def get_nod(a, b):
    """
    Нахождение Наибольший общий делитель
    Медленный алгоритм Евклида
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def get_fast_nod(a, b):
    """
    Быстрый алгоритм Евклида
    """
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


print(f'\nGlobal scope:\n{dir()}')
get_nod = timer_decorator(get_nod)
print(f'\nget_nod scope:\n{dir(get_nod)=}')
# print(get_nod(8, 800000000))
#
get_fast_nod = timer_decorator(get_fast_nod)
# print(get_fast_nod(50, 500000000))
