# Digit from 1 to 100
# Если кратно 3 то пишем Fizz
# Если кратно 5 то пишем Buzz
# Если кратно и 3 и 5 то пишем FizzBuzz

# Version 1:
def fizzbuzz_v1(count):
    for n in range(1, count + 1):
        if (n % 3) == 0 and (n % 5) == 0:
            print(f'Number = {n} so ', 'FizzBuzz')
        elif (n % 3) == 0:
            print(f'Number = {n} so ', 'Fizz')
        elif (n % 5) == 0:
            print(f'Number = {n} so ', 'Buzz')
        else:
            print(f'Number is {n}')


# Version 2: True & False
def fizzbuzz_v2(count):
    for n in range(1, count + 1):
        if not (n % 3) and not (n % 5):
            print(f'Number = {n} so ', 'FizzBuzz')
        elif not (n % 3):
            print(f'Number = {n} so ', 'Fizz')
        elif not (n % 5):
            print(f'Number = {n} so ', 'Buzz')
        else:
            print(f'Number is {n}')


fizzbuzz_v1(30)
fizzbuzz_v2(50)

