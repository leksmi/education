def main_func(name):
    def inner_func():
        print(f'Hello {name} !')

    return inner_func


s = main_func('Sveta')
print(s())
v = main_func('Violetta')
print(v())


def adder(value):
    def inner(a):
        return value + a

    return inner


a2 = adder(2)
print(a2(10))


def counter(count=0):
    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def average_number():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa
        nonlocal count
        summa = summa + number
        count += 1
        return summa / count

    return inner

def multiply(n):
    def inner(k):
        return n * k
    return inner