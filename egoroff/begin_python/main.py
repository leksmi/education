import sys
import pprint
import package1
# import package1.file1
# import package1.file2
from package1.file1 import c
# from package1.file1 import aaa
# from package1.file2 import show_data
#
print('При импорте выполняется поиск в каталогах:')
pprint.pprint(sys.path)
# print(f'\nДоступ к переменной из модуля:\n{package1.file1}: {package1.file1.b}')
# print(f'\n{package1.file2.h}')
#
print(f'c импортирована в текущую область видимости, можно обратиться напрямую: {c}')
# print(aaa)
# show_data('some text')
print(package1.h)
