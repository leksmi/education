# первоисточник сообщений - объект logRecord
# используем настройки из модуля logsettings_5.py
# extra={...}  для передачи в logRecord значений различных атрибутов


import logging.config
from logsettings_5 import logger_config

logging.config.dictConfig(logger_config)

logger = logging.getLogger("app_logger")


def new_func():
    name = "Alisa"
    logger.debug("Enter in to the New func ..", extra={"new_func_name": name})


def main():
    logger.debug("Enter in to the Main func.")


if __name__ == "__main__":
    # main()
    new_func()
