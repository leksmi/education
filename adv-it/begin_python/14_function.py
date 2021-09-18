import math

def func_test(string_1='Some text'):
    print('You wrote:', string_1)


func_test('No text')


# Factorial calculation
def fact_calc(f_numb=1):
    indx = 1
    for i in range(1, f_numb + 1):
        indx *= i
    return indx


print(fact_calc(5))
print(math.factorial(5))

proverka = __name__
print(type(proverka))
