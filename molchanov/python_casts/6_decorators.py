from datetime import datetime


def timeit(func):
    """
    Функция - декоратор
    :param func:  декорируемая функция
    :return:
    """

    def wrapper(*args, **kwargs):
        """
        Блок кода, в котором декоратор выполняет свои действия,
        и возвращает результат работы декорируемой функции
        :param args:
        :param kwargs:
        :return:
        """
        start = datetime.now()
        result = func(*args, **kwargs)  # запуск декорируемой функции
        print(f'\nВремя выполнения для {func} {datetime.now() - start}\n')
        return result

    return wrapper


# @timeit
def list_one(n):
    l: list = []
    for i in range(10 ** n):
        if not i % 2:
            l.append(i)
    return l


# @timeit
def list_two(n):
    l = [i for i in range(10 ** n) if not i % 2]
    return l


one_1 = timeit(list_one)(7)


# timeit принимает аргументом list_one,
# возвращает wrapper, который вызывается с аргументом 7


# в результате вернет wrapper который в свою очередь вызывается с аргументом 8
# эта запись эквивалентна
# @decorator_name
# декорируемая функция

# параметры в декораторе: требует дополнительную функцию:
def timeit(arg):
    print(arg)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)  # запуск декорируемой функции
            print(f'\nВремя выполнения для {func} {datetime.now() - start}\n')
            return result

        return wrapper

    return outer


@timeit
def one(n: int) -> list:
    """
    Создает список в цикле
    :param n:
    :return:
    """
    l: list = []
    for i in range(10 ** n):
        if not i % 2:
            l.append(i)
    return l


@timeit
def two(n: int) -> list:
    """
    Создает список через list comprehension
    :param n:
    :return:
    """
    l = [i for i in range(10 ** n) if not i % 2]
    return l


one(8)
