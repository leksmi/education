a, b, c = 1, 2, 3
a, b, c = [True, False, None]
a, *b, c = 'ABCDEF'
*a, b, c = 'ABCDEF'


def main(a, b, c):
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')


if __name__ == '__main__':
    main(a='Aa', c='Cc', b='Bb')
    print([10, 20, 30])
    print(*[10, 20, 30])
