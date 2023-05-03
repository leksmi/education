class ThreadData:
    # создаем набор атрибутов, которые будут общими для всех экземпляров
    __shared_attrs = {
        'name': 'Default Name',
        'data': {},
        'id': 1
    }
    def __init__(self):
        # сделаем подмену коллекции атрибутов __dict__ создаваемого экземпляра на общую.
        # так как коллекция будет общей для всех экземпляров, тогда и набор атрибутов со значениями так же общий для всех.
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
print(f'{th1.__dict__=}\n{th2.__dict__=}\n')
th2.name = 'The New Name'
print(f'{th1.__dict__=}\n{th2.__dict__=}')  # name изменился для всех.