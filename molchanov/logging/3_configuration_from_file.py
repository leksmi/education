import logging.config
from logsettings import logger_config
from rich import print, inspect


# load config to logging module:
logging.config.dictConfig(logger_config)
# создаем логгер, имя должно совпадать с указанным в logsettings.py !:
logger = logging.getLogger("app_logger")


# генерация логов:
logger.debug("This is a debug string")
logger.info("This is a info text message")
logger.warning("This is a warning message")
