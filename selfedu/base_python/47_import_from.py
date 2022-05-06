# При импорте модуля он полностью выполняется !
import os
import time
import pprint
import math as mt # подмена имени модуля
from math import ceil, pi
from scrapli.driver.core import IOSXEDriver

print(f'\nТекущий каталог: {os.getcwd()}')
pprint.pprint(locals())

print(f'{mt.pi=}')
print(f'{pi=}')
math = 'Математика' # сломали имя стандартного модуля
print(math)
print(f'{ceil(1.8)=}')
print(f'{ceil(1.4)=}')

print(f'{ceil=}')

def ceil(n):
    print('\nСделали свою функцию ceil, и ..\nсломали импортированную !\nВызовем ее:')
    return n

print(f'{ceil(1.5)=} (просто возврат аргумента)')
print(f'{ceil=}')

# Решение: импорт функции с подменой имени:
# from math import ceil as mc, pi

# Импорт всех функций и переменных:
from math import *  # Крайне не рекомендуется
pprint.pprint(locals())


