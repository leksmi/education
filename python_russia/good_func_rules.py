import random

# Хорошая функция это:
# 1. читаемое название говорящее о назначении функции
# 2. необходимые данные принимает в аргументах
# 3. короткая и читаемая
# 4. возвращает результат: некоторые данные (НЕ вывод на печать)
# 5. независима от Global переменных (No Global !) т.е. получает все данные при вызове: см. п.2
# 6. следствие п.5 - не изменять глобальных переменных
# 7. принцип Единой ответственности: делает что-то одно
# 8. в случае изменения входных аргументов (списка например) функция должна вернуть None !
# 9. Итог написанного выше: функция должна быть тестируема: подали что-то на вход, получили искомое

# Как НЕ надо делать:
# data = []
# value = 8
#
#
# def solution():
#     for i in range(5):
#         result = ''.join(str(random.randint(0, 9)) for _ in range(value))
#         print(result)
#         data.append(result)
#     print(data)
#     for index in range(len(data)):
#         if '5' in data[index]:
#             data[index] = data[index].replace('5', '6')
#     with open('test.txt', 'w') as f:
#         f.write('\n'.join(data))
#

def generate_pin(lenght: int) -> str:
    # lenght - количество цифр в пинкоде
    return ''.join(str(random.randint(0, 9)) for _ in range(lenght))


def replace_fives(a_lst: list, value: str) -> list[str]:
    # value это то, на что заменим все 5-ки
    # возвращает новый список
    return [element.replace('5', value) for element in a_lst]


def write_file(filename: str, data: str):
    # результат работы - записанный файл
    with open(filename, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    # если запуск текущего модуля, выполняем задачу с помощью функций
    # solution() - так было
    # правильный вариант:
    pins = [generate_pin(8) for _ in range(5)] # 5 пин кодов
    pins_without_fives = replace_fives(pins, '6')
    str_from_list = '\n'.join(pins_without_fives) # конвертируем (склеиваем) список в строку
    write_file('test_new.txt', str_from_list) # записали на диск
