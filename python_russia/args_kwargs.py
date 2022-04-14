a, b, c = 1, 2, 3
a, b, c = [True, False, None]
a, *b, c = 'ABCDEF'
*a, b, c = 'ABCDEF'
lst1 = [True, False, None]


def main(a, b, c):
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')


if __name__ == '__main__':
    main(a='Aa', c='Cc', b='Bb')
    main(101, 'bB', c='cC')
    main(*lst1)

def test_func_for_nothing():
    print('nothing')

print(*lst1)
