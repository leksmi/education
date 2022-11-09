# generator expression не создает коллекцию, а только инструкцию как получать элементы
# generator is lazy - не работает, пока не затребуешь очередной элемент через next()
# yield - показывает, что функция является генератором
# такая функция возвращает объект "генератор"

squares = (e ** 2 for e in range(0, 11, 2))  # выражение генератор: получили Генератор
print(squares)  # <generator object <genexpr> at 0x0000019785C197E0>
print(type(squares))  #<class 'generator'>


# for i in squares:
#     print(i)


# функция генератор:
def squares_gen():
    print('Генератор работает ..')
    for e in range(0, 10, 2):
        yield e ** 2


# результатом вызова squares_gen будет генератор, который получает ссылку "gen" :
gen = squares_gen()
print(gen)  # <generator object squares_gen at 0x0000019785C19850>
print(type(gen))  # <class 'generator'>

# for i in gen:
#     print(i)
#
# for j in squares_gen():
#     print(j, end=' ')
