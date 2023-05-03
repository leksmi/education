# Pattern (шаблон разработки) - общий способ решения задач/проблем
# Singleton - шаблон для предоставления глобального доступа к состоянию

class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        """
        Переопределяем дефолтный __new__ и вынуждаем его при каждом создании
        экземпляра проверять есть ли уже какой-то экземпляр:
        если нет (None) создаем его,
        если уже создан - возвращаем ссылку на ранее созданный (по сути единственный)
        экземпляр Класса.
        :param args:
        :param kwargs:
        """
        if Singleton.instance is None:
            # создаем экземпляр, если еще не создан:
            Singleton.instance = super().__new__(cls)
        return Singleton.instance

    # Пример использования:
    def do_something(self, number):
        """
        Высоко нагруженный процесс
        :return:
        """
        self.data = number


if __name__ == '__main__':
    first = Singleton()
    second = Singleton()
    print(f'{first=}')
    print(f'{second=}')
    print('Check id: they are the same -', first is second)
    first.do_something(number=100000000001)
    print(first.data)
    print(second.data)
