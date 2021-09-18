mess = 'Go Go'
name = 'Leks'
print(id(mess))


def greet(perem, name='', mess=''):
    result = f'{mess} {name}'
    name_s = perem
    # print(result)
    # print('Hello', name, '!')
    return result
    # Без return функция вернет None - символ пустоты.
    # Это неявный возврат.
    # Если нужно вернуть None лучше это делать явно: return None


print(greet('some_script', name, mess).lower())
print(id(mess))
print(type(greet('')))
