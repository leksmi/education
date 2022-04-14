def get_V(a, b, c):
    print(f'A = {a} B = {b} C = {c}')
    return a * b * c


print(get_V(1, 2, 5))
print(get_V(b=3, c=5, a=2))


def get_Ver(a=1, b=1, c=1, verbose=True):
    if verbose:
        print(f'Print params: A = {a} B = {b} C = {c}')
    else:
        print('Do not print params')
    return a * b * c


print(get_Ver())
print(get_Ver(2, 3))
print(get_Ver(c=15, verbose=False))

def add_value(value, lst=[]):
    lst.append(value)
    return lst

l =add_value(1)
l = add_value(2)
print(l)

