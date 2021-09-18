
a = 'hello'
print(dir(a))

print(a.upper())
print(a)  # Действие .upper() не изменяет саму строку

b = a.upper()
print(id(b))
print(id(a))
# Это показывает, что строки не изменяемы

# Форматирование строк (подстановка значений)
# Два способа: метод .format() и f-string notation
name = 'World'
s = 'Hello, {}'
result = s.format(name)
print(result)

film = 'Leon'
number = 100

print('{} - {}'.format(film, number))

# Именованные присваивания
pattern = '{movie} - {rating}'
print(pattern.format(movie=film, rating=number))

# f-string notation
result = f'{film} - {number}'
print(result)
