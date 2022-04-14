import sys
from pprint import pprint
sys.path.append('C:\\python\\reposit\\education\\egoroff\\begin_python\\dir')
pprint(sys.path)

# Импорт своего модуля,
# Если путь отличен от sys.path - указывать через точку:
# from egoroff.begin_python.dir import mymodule
# from egoroff.begin_python.dir.mymodule import my_str, my_val1
import mymodule
from mymodule import my_str, my_val1

# Вызов функции из импортированного модуля
print(mymodule.factorial(5))
print(my_str, my_val1, sep='\n')

# Так в модуле mymodule импортировано все из math через *
# При импорте mymodule получем прямой доступ ко всем именам math
print(mymodule.pi)  # константа из math
print(mymodule.tau)  # константа из math
print(mymodule.exp(5))  # функция из math

# Известные системе пути:
pprint(sys.path)
# ['C:\\python\\reposit\\education\\egoroff\\begin_python',
#  'C:\\python\\reposit\\education',
#  'C:\\python\\python39\\python39.zip',
#  'C:\\python\\python39\\DLLs',
#  'C:\\python\\python39\\lib',
#  'C:\\python\\python39',
#  'C:\\python\\reposit\\education\\venv',
#  'C:\\python\\reposit\\education\\venv\\lib\\site-packages']
# sys.path - это список, тогда можно добавитьв Него свои пути (см начало файла):
print(type(sys.path))
sys.path.append('C:\\python\\reposit\\education\\egoroff\\begin_python\\dir')
pprint(sys.path)

# При импорте модуля, он полностью выполняется
# только один раз, даже при повторном импорте.
# Для повтороного импорта, использовать модуль
# importlib

import kbyers_code_structure

kbyers_code_structure.dns_ip()
sorted()