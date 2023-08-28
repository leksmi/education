import pytz
from datetime import datetime

RED = '\033[1;31m'
WHITE = '\033[00m'
GREEN = '\033[0;92m'


class Account:
    """
    - нужно скрыть возможность напрямую править некоторые поля,
    - например счет.
    -

    """
    def __init__(self, name, balance: int):
        self.name = name
        self.__balance = balance
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
