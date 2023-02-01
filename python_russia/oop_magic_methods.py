class Banknote:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):  # для программистов
        return f'{self.__class__.__name__}({self.value})'

    def __str__(self):  # для людей
        return f'\nБанкнота номиналом {self.value} рублей'


if __name__ == '__main__':
    bn10 = Banknote(10)
    bn50 = Banknote(50)
    print(bn10, bn50)
    print(f'{bn10!r}', f'{bn50!r}')

