class Account:
    def __init__(self, name, balance: int):
        self.name = name
        self.balance = balance

    def deposit(self, amount: int):
        """
        Пополнение счета (баланса)
        :param amount:
        :return:
        """
        self.balance += amount

    def withdraw(self, amount: int):
        """
        Вывод со счета
        Предварительно проверить, что на балансе есть нужная сумма
        :param amount:
        :return:
        """
        if self.balance >= amount:
            self.balance -= amount
            print(f'Потрачено: {amount}\nОстаток на счете: {self.balance}\n')
        else:
            raise ValueError('На балансе недостаточно средств')

    def show_balance(self):
        """
        Отображение текущего счета
        :return:
        """
        print(f'Текущий баланс: {self.balance}')


acc1 = Account('Aleksei', 1000)
