from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)  # запуск декорируемой функции
        print(f'\nВремя выполнения для {func} {datetime.now() - start}\n')
        return result

    return wrapper


# @timeit
def one(n):
    l: list = []
    for i in range(10 ** n):
        if not i % 2:
            l.append(i)
    return l


# @timeit
def two(n):
    l = [i for i in range(10 ** n) if not i % 2]
    return l


# l1 = one(8)
# l2 = two(8)

# print(l1)
# print(l2)

l1 = timeit(one)
l1 = timeit(one)(8)


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
def one(n):
    l: list = []
    for i in range(10 ** n):
        if not i % 2:
            l.append(i)
    return l


@timeit
def two(n):
    l = [i for i in range(10 ** n) if not i % 2]
    return l


one(8)
