# Если при создании логгера не передать аргумент - имя, создается  RootLogger.
# Так как реализовано через Singleton, всегда есть единственный RootLogger
# logger можно создать через точку от корневого
# Propagation - распространение лог записей по иерархии

import logging
from rich import print, inspect

# RootLogger:
logger = logging.getLogger(name=None)  # make RootLogger, default level=30
print(f"{logger=}")

# Именованный логгер, наследуется от root:
app_logger = logging.getLogger(name="app_logger")
print(f"{app_logger=}")
print(f"{app_logger.parent=}")  # покажет наследование от RootLogger

# создание через точку с наследование:
utils_logger = logging.getLogger("app_logger.utils")
print(f"{utils_logger=}")
print(f"{utils_logger.parent=}")

# Меняем уровень логирования по иерархии:
# utils_logger.setLevel('DEBUG')
# logger.setLevel('DEBUG')
app_logger.setLevel("DEBUG")
print(logger, app_logger, utils_logger, sep="\n")
# уровень будет наследоваться от корневого и выше !

# Handlers:
print(f"\n{app_logger.parent.handlers=}\n")
utils_logger.debug("some debug message !")  # не появится, так как нет хендлеров
# создаем дефолтный хендлер, его уровень NotSet - т.е. обрабатывает ВСЕ сообщения
logging.basicConfig()  # создаст handler для root логгера
print(f"\n{app_logger.parent.handlers=}\n")
print(f"{utils_logger.handlers=}")
utils_logger.debug("some debug message !")
# propagetion - передача сообщений на обработку по иерархии наследования
print(f"{utils_logger.propagate=}")
# можно отключить:
utils_logger.propagate = False
print(f"{utils_logger.propagate=}")
utils_logger.debug("some debug message !")  # теперь Не выведется

# создание именованого хендлера:
console_handler = logging.StreamHandler()
# сопоставление логгеру:
app_logger.addHandler(hdlr=console_handler)
# создание форматировщика:
frmt = logging.Formatter(fmt="%(levelname)s : %(name)s : %(message)s")
# присоединение форматировщика к хендлеру:
console_handler.setFormatter(fmt=frmt)
