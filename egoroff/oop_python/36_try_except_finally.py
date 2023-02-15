try:
    a + b
    19 / 0
    int('hello')
    1 / 0

except ValueError:
    print(f'\nError: Value error')
except ZeroDivisionError:
    print(f'\nError: division by zero')
except NameError:
    print(f'\nError: name is not defined')

s = 'hello'
d = {}
try:
    i = 101
    # print(d['one'])

except KeyError:
    print(f'\nError: KeyError')
except LookupError:
    print(f'\nError: LookupError')
except Exception:  # отреагирует на любое (почти) исключение
    print(f'\nSome error occurred')
finally:  # блок finally только один
    print(f'\nfinally: Блок finally выполняется всегда\n\n')


my_list = [None, False, 'Ok', 'text']
try:
    # print(my_list[7])
    print(my_list[2])
except (IndexError, KeyError):
    print(f'\nОшибка в индексе или ключе (LookupError error)')
else:  # else только один
    print(f'\nЭтот блок выполняется если исключения Не было ! Требует наличия except.')
finally:  # блок finally только один
    print(f'\nfinally: Блок finally выполняется всегда. Не требует наличия except.')


