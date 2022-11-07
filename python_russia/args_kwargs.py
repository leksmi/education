a, b, c = 1, 2, 3
a, b, c = [True, False, None]
a, *b, c = 'ABCDEF'
*a, b, c = 'ABCDEF'
lst1 = [True, False, None]
print(*lst1)


def test_func_for_nothing():
    print('nothing')


def main(a, b, /, c, *, d=None):
    # / - слева от слэша это ОБЯЗАТЕЛЬНО позиционные аргументы
    # * - после звезды это ОБЯЗАТЕЛЬНО ключевые аргументы
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')


def my_print(a, *b):
    print(type(a), a)
    print(type(b), b)


def my_print_args(*args):  # множество поз-х арг-в будет Упаковано в кортеж
    for i in args:
        print(i)


def my_print_args_kwargs(*args, **kwargs):
    print(f'args это {type(args)}', args)
    print(f'kwargs это {type(kwargs)}', kwargs)
    if kwargs:
        for i in kwargs:
            print(kwargs[i])


if __name__ == '__main__':
    main('Aa', 'Bb', c='Cc')
    main(101, 'bB', c='cC')
    main(*lst1)
    my_print(101, 'H', 'e', 505, None)
    my_print_args(11, 12, 13, 14, 15, 16, 17)
    lst_2 = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
    my_print_args(lst_2)
    print()
    my_print_args(*lst_2)  # сначала будет распакован lst_2 и передан как множество поз-х арг-в
    print()
    my_print_args_kwargs(33, 44, 55, five= 5, seven=7)
    dev = {'host': '192.168.1.11', 'platform': 'Cisco inc', 'username': 'cisco', 'password': '12345'}
    my_print_args_kwargs(**dev)
    my_print_args_kwargs()  # пустой вызов: будет пустой кортеж и пустой словарь
