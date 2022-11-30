from time import sleep


# decorator
def decor(func):
    def inner():
        print(f'Start decorator ..')
        func()  # вызов декорируемой фун-ии
        print(f'Finish decorator')

    return inner


def some_func():
    print(f'Main function working ..')
    sleep(3)


d = decor(some_func)
print(d, '\n', d.__closure__)
d()

# декорирование предусматривает переприсвоение имени
# декорируемой функции и последующий ее вызов:
some_func = decor(some_func)
some_func()
# при этом имя функции ссылается на возврат декоратора:
print(some_func, '\n', some_func.__closure__)


# за счет этого, под прежним именем функции мы получили ее же,
# но с расширенным функционалом от decor
#
# передачу аргументов Всегда делать через *args, **kwargs !
def decor_args(func):
    def inner(*args, **kwargs):
        print(f'\n* Decorator starts doing something..')
        func(*args, **kwargs)  # вызов декорируемой фун-ии с любыми аргументами
        print(f'* Decorator has finished his job\n')

    return inner


def say_hello(name, surname, age=None):
    print(f'Hello {name} {surname} {age} year old !')


say_hello = decor_args(say_hello)
say_hello('Sintiya', 'Krauft', age=33)
say_hello('Semen', 'Gorodetskiy')


# вместо переопределения фун-ии, используют @
@decor_args
def get_config(ip=None, login=None, password=None):
    print(f'Config file..\n{ip}\n{login}\n{password}')


get_config(ip='192.168.111.1', login='my_login', password='my_password')
