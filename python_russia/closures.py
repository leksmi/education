# замыкание это внутренняя функция которая возвращается из внешней, и использует внешние переменные
#
#
# каждое замыкание хранит свое состояние

def names():
    all_names = []  # свободная переменная

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def average():
    vals = []

    def inner(val: int) -> float:
        vals.append(val)
        return sum(vals) / len(vals)

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


def pow_(base):
    def inner(val):
        return val ** base # используем base (параметр) объявленныйво внешней функции

    return inner


if __name__ == '__main__':
    students = names()  # момент выполнения функции names
    # по завершении работы names ее локальные переменные (all_names) должны удалиться сборщиком мусора
    # но, в переменную students присвоена функция inner как ОБЪЕКТ,
    # а inner использует переменную all_names и "держит" ее,
    # тогда получается students "удерживает" переменную all_names
    # получается, что из глобальной видимости можем работать с переменной внутри функции (!)
    print(students('Nina'))
    print(students('Olya'))
    print(students('Vika'))
    print(id(students))
    autos = names()
    print(autos('Lada'))
    print(autos('i320'))
    print(autos('Atlas'))
    print(id(autos))
    print(autos.__closure__[0].cell_contents) # извлечение внутренней переменной через "magic method"
