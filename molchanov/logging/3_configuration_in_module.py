# Способы настройки:
# 1. Обычный
import logging

# make App logger:
logger = logging.getLogger(name="app")
# make console output handler:
console_handler = logging.StreamHandler()
# add handler to logger:
logger.addHandler(hdlr=console_handler)
# make formatters with old and new style:
fmrt_old = logging.Formatter(fmt="%(asctime)s %(levelname)s %(name)s %(message)s")
fmrt_new = logging.Formatter(fmt="{asctime}: {levelname}: {name}: {message}", style="{")
# add formatter to handler:
console_handler.setFormatter(fmt=fmrt_new)
# check that logger works
logger.warning("It is some warning message")
# current level=0 (NOTSET)
print(f"\nCurrent logger level: {logger.level}")
# set to 10 (DEBUG):
logger.setLevel(10)
print(f"\nSet to DEBUG..\nCurrent logger level: {logger.level}\n")
logger.debug("It is some debug message")
#
# add file handler:
file_handler = logging.FileHandler(filename='logfile_example.log')
logger.addHandler(file_handler)
print(f"\nCurrent handlers:\n{logger.handlers}\n")
# список handlers содержит несколько обработчиков, применяются все !
# add formatter to file handler:
file_handler.setFormatter(fmt=fmrt_new)
#
logger.warning("It is a warning message")
logger.debug("It is a debug message")


# 2. Через конфигурацию в отдельном файле
# для этого создаем отдельный модуль logsettings.py
