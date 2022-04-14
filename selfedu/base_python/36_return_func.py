#
def get_sqrt(x: int) -> int:
    res = None if x < 0 else x ** 0.5
    return res, x


def get_max2(a: int, b: int) -> int:
    print('get_max2 is working ..')
    return a if a > b else b


def get_max3(a, b, c):
    print('get_max3 is working ...')
    return get_max2(a, get_max2(b, c))


print(get_max3(7, 3, 11))
print(get_max3(12, 55, 3))

# Определение функции с условием:
FLAG = True
# FLAG = False

if FLAG:
    def get_res(z, x):
        print('Perimetr:')
        return 2 * (z + x)
else:
    def get_res(z, x):
        print('Square:')
        return z * x

print(get_res(5, 4))
