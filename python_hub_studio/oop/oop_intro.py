class Purse:

    def __init__(self, valuta, money=0, name='Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError('Ошибка указания валюты')
        self.__money = money
        self.valuta = valuta
        self.name = name
        print(f'Исходное состояние:\nИмя: {self.name}\nНа счете: {self.__money}\nВалюта: {self.valuta}\n{"-"*20}')

    def info(self):
        return f'Текущий баланс кошелька {self.name}: {self.__money}'

    def top_up_balance(self, howmany):
        print(f'Пополнение кошелька {self.name} на {howmany}.')
        self.__money += howmany

    def top_down_balance(self, howmany) -> (int, float):
        """
        :param howmany: сколько списываем со счета
        :return: сколько списали
        """
        if self.__money - howmany < 0:
            print('Not enough money')
            raise ValueError('Not enough money')
        self.__money -= howmany
        return howmany

    def __str__(self):
        return f'Class: {self.__class__.__name__} name: {self.name}'

    def __del__(self):
        print(f'Отработал __del__ для {self}')
        return self.__money


x = Purse(valuta='USD', name='Aleks')
y = Purse(valuta='EUR', name='Bill')
x.top_up_balance(100)
print(x.info())
y.money = -200  # создаст новое локальное свойство объекта "y". Не повлияет на приватный __money
print(y.info())
print(f'{y.__dict__=}')
y.top_up_balance(555)
print(y.info())
print(str(y))
x.top_up_balance(howmany=y.top_down_balance(howmany=25))  # списание с одного и пополнение другого кошелька
print(x.info())
