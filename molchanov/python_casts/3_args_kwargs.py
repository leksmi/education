def add(a, b):  # Ограничение количества аргументов
    s = a + b
    return s


print(add(5, 7))


def add(*args):  # * пакует все аргументы в Кортеж
    print(args, type(args))
    s = sum(args)  # sum принимает Кортеж как один аргумент
    return s


print(add(3, 7, 12, 22))  # передаем любое количество чисел
