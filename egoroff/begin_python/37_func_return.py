def example():
    print('One')
    print('Two')
    return 'The End !'
    print('some text')  # Это уже не выполняется


res = example()
print(res)


def even(x):
    return x % 2 == 0


for i in range(1, 11):
    print(f'CHeck for: {i} result: {even(i)}')

