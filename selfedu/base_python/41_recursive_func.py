def recurs(value):
    print(value)
    if value < 4:
        recurs(value + 1)
    print(value)

recurs(1)

# Факториал числа: !n = 1 * 2 * 3 * .. * n OR n * (n-1) * (n-2) * (n-3) * .. * 1
def calc_fact(n):
    if n <= 0:
        return 1
    else:
        return n * calc_fact(n-1)

print(f'\nCalc_fact func starting ..')
result = calc_fact(6)
print(f'Factorial is {result}')
