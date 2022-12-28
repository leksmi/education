def rec(x):
    print(x)
    rec(x + 1)


# rec(1)  # после 996 вызовов падает исключение RecursionError: maximum recursion depth exceeded


def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)


rec(1)


def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x


print(f'Factorial: {fact(4)=}')


# Fibonacci
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(5))
print(fib(6))
print(fib(7))
