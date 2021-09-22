# Произвольное число позиционных аргументов:
def get_data(*args):
    print(args)
    print(f'We got {type(args)} data')


get_data(3, 8, 'some_text')
get_data()


def get_data2(*args, flag='R', check=False):  # Можно так же добавлять фиксированное количество ключевых аргументов
    print(args)
    print(f'We got {type(args)} data')
    print(f'Our keyword args are: {flag}, {check}')


get_data2()
get_data2(5, 9, check=True)


# Для указания произвольного количества как позиционных так и ключевых:
def get_data3(*args, **kwargs):
    print(f'We got args: {args} it is {type(args)}')
    print(f'We got keyword args: {kwargs} it is {type(kwargs)}')


# Так же можно указать ключевые параметры по умолчанию Перед **kwargs !:
def get_data3(*args, tocheck=True, **kwargs):
    print(f'We got args: {args} it is {type(args)}')
    print(f'We got keyword args: {kwargs} it is {type(kwargs)}')
    print(f'Default param: {tocheck}')

# Аналогично с позиционными, Но тогда минимум 1й параметр указать надо! :
def get_data3(count, *args, tocheck='Yes', **kwargs):
    print(f'We got args: {args} it is {type(args)}')
    print(f'We got keyword args: {kwargs} it is {type(kwargs)}')
    print(f'Mandatory positional: count {count}')
    print(f'Default param: {tocheck}')
