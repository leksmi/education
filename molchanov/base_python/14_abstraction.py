
# Proportion:
# 1000 * 15 = mass * x
# x = 15 * mass / 1000
# Функция вычисляет массу соли по массе мяса согласно пропорции:
def get_salt(mass):
    return 15 * mass / 1000

mass = int(input('Введите массу мяса: '))
print('Масса соли: ', get_salt(mass))

# Добавим функцию расчета перца
# Proportion:
# 1000 * 5 = mass * x
# x = 5 * mass / 1000
def get_pepper(mass):
    return 5 * mass / 1000

print('Масса перца: ', get_pepper(mass))

# Функция по сути повторяется. Сокращаем код: функция одна общая, данные берем из словаря:
# data:
ingridients = {
    'sault': 15,
    'pepper': 5
}

def get_ingridient(mass, ingr):
    return ingridients.get(ingr, 0) * mass / 1000

ingr_name = input('Введите ингридиент: ')
print(f'Масса {ingr_name}: ', get_ingridient(mass, ingr_name))
#
#
# Оборачивание функций своими функциями, на примере print()
def print_to_file(text):
    with open('testtext.txt', 'a') as text_file:
        print(text, file=text_file)


print_to_file('test text')



