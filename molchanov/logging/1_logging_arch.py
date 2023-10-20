# Генерация лог записей происходит в 3 этапа:
# 1. создается объект logger, который генерирует объект logrecord
# 2. logrecord поступает в handler(s), причем уровень логгера и хендлера должны соответствовать
# 3. хендлер передает целевой logrecord форматтеру для преобразования в строку
# затем форматтер отдает строку хендлеру обратно, тот выводит ее по назначению (консоль, файл, почта и т.д.)
# Logging реализует паттерн singleton, все логгеры наследуются от RootLogger
# можно (и нужно) менять уровень отдельных, дочерних логгеров:
# logging.getLogger('logger_name').setLevel('LEVEL')


import logging
import requests
from rich import print, inspect

# создаем логгер (API для создания записей):
logger = logging.getLogger()  # default level=30 (Warning). RootLogger
print(f"Параметры созданного логгера: {logger}")
# текущий уровень логгера:
print(logger.level)
# понизим уровень до 10 (Debug)
logger.setLevel(level="DEBUG")
print(f"Параметры измененного логгера: {logger}")
# текущий уровень логгера:
print(logger.level)
# Handler по умолчанию обрабатывает уровни 30 и выше
# По умолчанию работает дефолтный хэндлер StreamHandler (пишет в StdErr)
print(f"Current handlers: {logger.handlers=}")
# для настройки уровня handler можно использовать basicConfig:
logging.basicConfig(level="DEBUG")
print(f"Current handlers: {logger.handlers=}")

# вывод всех текущих логгеров:
for key in logging.Logger.manager.loggerDict:
    print(key)


def main(name, logger=logger):
    # создаем объект LogRecord:
    logger.warning(f"Module main begins work. The name is {name}")
    logger.debug(f"Main function begins work, so it is ok.")


def web_request(url):
    logger.debug(f"Try to get site page")
    r = requests.get(url=url)


if __name__ == "__main__":
    main(name="Oleg")
    # print(dir(logger))
    web_request(url="https://www.google.ru")
