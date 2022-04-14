import os
import pprint
import calendar
from math import e, pi, factorial as fact


def say_hello(name):
    print(f'Hello {name} !')


def summa(*args):
    print(f'The summ of {print(args)} is {sum(args)}')
    return sum(args)


def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


my_str = 'Some important string !'
my_val1 = 101
my_val2 = 777

print(os.getcwd())
pprint.pprint(locals())
# print(calendar.TextCalendar().formatyear(2021))
# print(math.e)
# print(math.pi)
# print(math.tau)
# pprint.pprint(dir(math))
print(f'E: {e} PI: {pi}')
print(f'Factorial: {factorial(5)}')
