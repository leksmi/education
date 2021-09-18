print('*'*10, 'Input data machine', '*'*10)
#
a = input('Enter your first name: ')
while True:
    try:
        b = int(input('Enter some number: '))
    except ValueError:
        print('Wrong data type !', 'You have to enter your number!\n')
        continue
    break
print('a is ', type(a))
print('b is ', type(b))
print(a.title(), b)
summ_name = a + str(b)
print(summ_name[::-1])

a_var = '.... some text .........'
print(a_var.strip('.').strip().title())
