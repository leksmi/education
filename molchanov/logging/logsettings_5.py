# disable_existing_loggers - отключить все логгеры кроме корневого -
# логгеры, которые не перечислены в опиции настройки, использовать данный конфиг
# не будут.

import logging
from logging import LogRecord


class NewFuncFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        print(record.new_func_name)
        return record.funcName == 'new_func'  # True при совпадении с нужным именем


logger_config = {
    "version": 1,  # It can be 1 only
    "disable_existing_loggers": False,
    "formatters": {
        "fmrt_new": {
            "format": "{asctime}: {levelname}: {name}: {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "fmrt_new",
            "filters": ['new_filter']  # добавлен фильтр
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "logfile_example_2.log",
            "level": "DEBUG",
            "formatter": "fmrt_new",
        },
    },
    "loggers": {
        "app_logger": {
            "level": "DEBUG",
            "handlers": ["console_handler", "file_handler"],
            "propagate": False,  # default=True
        }
    },
    "filters": {
        'new_filter': {
            '()': NewFuncFilter  # () - спец.форма ключа указывающая на вызов значения как callable объекта
        }
    },
    # 'root': {},  # часто это пустая строка, являющаяся корневым логгером: '': {}
    # 'incremental': True  # признак того, что данный конфиг дополняет другой
}
