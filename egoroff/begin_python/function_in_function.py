g = 'Gray'

def colors(param='r'):
    y = 'yellow'
    g = 'Green !'

    def print_red():
        nonlocal y
        r = 'red'
        print(r, y, g)
        y = 'Y was changed'

    def print_blue():
        b = 'blue'
        print(b, y, g)

    if param == 'r':
        print_red()
    elif param == 'b':
        print_blue()
    else:
        print('Unknown param !')

colors(param='c')
