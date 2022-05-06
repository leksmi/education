import pprint
from folder import mymodule
import sys
import mymodule_2 # При импорте будет выполнен весь код этого модуля !
from sys import path as mod_import_paths
from folder.mymodule import floor


print(mymodule)
print(f'{ mymodule.NAME=}')

# mymodule.floor(5.4)
print(f'{ mymodule.floor(5.4)=}')
print(f'{floor(5.9)=}')

pprint.pp(dir(mymodule))

# a = mymodule.math.floor(-5.6)
# print(a)
print(f'{ mymodule.pi=}')

# Список путей импорта: sys.path
pprint.pprint(sys.path)
# Или:
# pprint.pprint(mod_import_paths)
