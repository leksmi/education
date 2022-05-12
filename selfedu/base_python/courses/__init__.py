import courses.python # нужно указать каталог, так как нет пути в sys.path
from courses.python import get_python # Это абсолютный импорт
from .php import get_mysql
from . import html, java

NAME = 'package courses'

