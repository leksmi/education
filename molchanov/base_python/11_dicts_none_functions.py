
# Способ создать словарь литералом
person = {'name': 'vasya', 'phone': '322223', 'email': 'vasya@mail.com'}
print(person)
print(person['name'])

# Способ создать словарь функцией "dict"
person_2 = dict(name='Sveta', sex='female')
print(person_2)

# -----

# Получение данных из словаря:
# Обращение напрямую к ключу:
print('\n')
print(person_2['name'])

# "get" метод позволяет опросить словарь и если ключа нет вместо исключения получим - None
# None - это зарезервированное слово для обозначения пустоты
print('\n')
print(person.get('phone'))
print(person_2.get('phone'))

# Если указать второй аргумент, он будет подставлен при отсутствии ключа:
print(person_2.get('phone', 'nothing'))

# Если при опросе ключа его нет но нужно создать, используем setdefault:
print('\n')
print(person_2.setdefault('phone', '773337'))
# При этом словарь модифицирован данной парой ключ:значение
print(person_2)

# Опрос всего словаря:
for item in person_2:
    print(item)
    # Вернет только ключи !
# Аналогичный результат используя методы словаря:
print('\n')
for item in person_2.keys():
    print(item)
    # Вернет только ключи !

# Для получения ключа и значения метод .items()
print('\n')
person_list = []
for item in person.items():
    person_list.append(item)
    # Вернет список кортежей ! ! !
print(person_list)

# Использование распаковки кортежа (аналогично спискам) позволяет получить ключ и значение сразу
print('\n')
for key, val in person.items():
    print('Key: ', key, '\tValue: ', val)

# Изменение значений и/или дополнение новыми - методом .update()
new_name = {
    'name': 'Olesya',
    'email': 'okalez@mail.com',
    'region': 'Ryazansk.obl'
}
person.update(new_name)
print(person)
# Или указывать значение для ключей прямо в update()
person.update(name='Olya', email='olya@yand.com')
print(person)

