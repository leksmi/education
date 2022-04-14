class Car:
    model = 'BMW'
    engine = 1.6

    def drive():
        print('Car is going ..')


class NewCar:
    model = 'BMW'
    engine = 1.6

    @staticmethod
    def drive():
        print('Car is going ..')


car = Car()
car.drive()

new_car = NewCar()
new_car.drive() # сработает за счет декоратора @staticmethod
