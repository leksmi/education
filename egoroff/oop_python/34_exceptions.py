try:
    print(int('12345'))
    print(int('hello'))
except ValueError:
    print('\nОшибка преобразования')

t = IndexError()
print(isinstance(t, IndexError))
print(isinstance(t, LookupError))
print(isinstance(t, TypeError))
print(isinstance(t, BaseException))

tstList = [11, True, 'Ok', None]
# print(tstList[5])
try:
    print(tstList[5])
except IndexError:  # это дочерний класс от LookupError
    print('\nНеправильный индекс')
    exit(1)

try:
    print(tstList[5])
except LookupError:
    # LookupError это родительский класс для IndexError, поэтому он сработает.
    # Но, тогда будут обрабатываться исключения KeyError (дочерний от LookupError)
    print('\nНеправильный индекс')
    exit(1)
