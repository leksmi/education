#
#
import logging.config
from logsettings_4 import logger_config
from rich import print, inspect

# load config from file(dict)
logging.config.dictConfig(config=logger_config)
# make logger. Logger name must be listed in logger_config !
logger = logging.getLogger("app_logger")


def my_split(in_data: tuple):
    """
    1-й вариант: через ручное формирование сообщения
    """
    for item in in_data:
        try:
            print(item.split())
        except:
            logger.debug(msg=f"Exception for item: {item}", exc_info=True)
            pass


def my_split_exc(in_data: tuple):
    """
    2-й вариант: через вызов метода логгера exception
    при этом уровень сообщения формируется автоматически
    """
    for item in in_data:
        try:
            print(item.split())
        except:
            logger.exception(msg=f"Exception for item: {item}")


def main():
    """
    Output some log messages
    """
    logger.debug("Func main() has called !")


if __name__ == "__main__":
    words = ("new house", "apple", "ice cream", 100)
    # main()
    # my_split(words)
    my_split_exc(words)
