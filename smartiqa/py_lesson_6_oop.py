class Human:
    # static fields:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name: str = default_name, age: int = default_age):
        # dynamic fields:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'\nПерсональные данные:')
        print(f'Name: {self.name}\nAge: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    # static method:
    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def earn_money(self, earned_money: [int, float]):
        """
        :param earned_money: [int, float]
        :return:
        """
        self.__money += earned_money
        print(f'Earned: {earned_money},\ncurrent money: {self.__money}')

    def buy_house(self, house, discount: int):  # house - ссылка на объект дома
        price = house.final_price(discount=discount)
        if self.__money >= price:
            self.__make_deal(house, price=price)
            print(f'Дом {self.__house} успешно куплен')
            print(f'Остаток денег: {self.__money}')
        else:
            print('Not enough money to buy a house !')

    def __make_deal(self, house, price):  # house - ссылка на объект дома
        self.__money -= price
        self.__house = house


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Итоговая цена дома: {final_price}')
        return final_price


class SmallHouse(House):
    def __init__(self, price):
        default_area = 40
        super().__init__(area=default_area, price=price)


if __name__ == '__main__':
    # print(f'\n{Human.default_name=}\n{Human.default_age=}')
    # fedor = Human('Fedor', 32)
    # fedor.info()
    # fedor.info()
    # #
    # house = House(area=100, price=15_000)
    # fedor.buy_house(house, discount=3)
    # fedor.earn_money(earned_money=10000)
    # shouse = SmallHouse(8_000)
    # print(shouse.__dict__)
    Human.default_info()
    person = Human(name='Nikole', age=28)
    person.info()
    sm_house = SmallHouse(7_500)
    person.buy_house(sm_house, discount=5)
    person.earn_money(5_300)
    person.buy_house(sm_house, discount=5)
    person.earn_money(3_300)
    person.buy_house(sm_house, discount=5)
    person.info()
