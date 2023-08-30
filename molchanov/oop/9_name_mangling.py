import pytz
from datetime import datetime
from rich import print, inspect

RED = '\033[1;31m'
WHITE = '\033[00m'
GREEN = '\033[0;92m'


class Account:
    """
    - нужно скрыть возможность напрямую править некоторые поля,
    - например счет.
    - использование переменных вида self.__variable приводит к генерации name mangling:
    - вида _ClassName__variable, который выполняется при компиляции кода.
    - Именно с этой переменной будут работать все методы Класса.
    - за счет этого не получится сделать подмену переменной в экземпляре Класса через
    - объявление двойника вида __variable

    """

    def __init__(self, name: str, balance: int):
        self.name = name
        self.__balance = balance  # произойдет создание _Account__balance
        self.history = []  # история операция

    @staticmethod
    def _get_current_time():
        """
        Простая функция, декорируем как статик_метод
        :return: time stamp
        """
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount: int):
        """
        Пополнение счета (баланса)
        :param amount:
        :return:
        """
        self.__balance += amount
        print(self.show_balance())
        self.history.append((amount, self._get_current_time()))

    def withdraw(self, amount: int):
        """
        Вывод со счета
        Предварительно проверить, что на балансе есть нужная сумма
        :param amount:
        :return:
        """
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'Потрачено: {amount}\nОстаток на счете: {self.__balance}\n')
            print(self.show_balance())
            self.history.append((-amount, self._get_current_time()))
        else:
            print('На балансе недостаточно средств')
            print(self.show_balance())

    def show_balance(self):
        """
        Отображение текущего счета
        :return:
        """
        return f'Текущий баланс: {self.__balance}'

    def show_history(self):
        """
        Вывод лога операций
        :return:
        """
        for amount, date in self.history:
            if amount > 0:
                transaction = 'Deposited'
                color = GREEN
            else:
                transaction = 'Withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE}\t{transaction} on {date.astimezone()}')


acc1 = Account('Safronov', 10)
print(inspect(acc1))
print(dir(acc1))
print(acc1.__dict__)
print(acc1.show_balance())
acc1.__balance = 1000000000  # переменная создается после создания экземпляра асс1
print(acc1.__dict__)
print(acc1.show_balance())
print(f"{acc1.__dict__['_Account__balance']=}\n{acc1.__dict__['__balance']=}")
