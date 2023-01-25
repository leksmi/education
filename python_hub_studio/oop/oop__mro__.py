class A:  # Базовый (супер) класс
    def a_method(self):
        print('Отработал метод А класса')


class B:  # Базовый (супер) класс
    def a_method(self):
        print('Отработал метод В класса')


class C(B):  # Дочерний класс
    def a_method(self):
        print('Отработал метод С класса')


class D(C, A):  # Дочерний класс
    def a_method(self):
        super().a_method()
        print(self.__class__.__mro__)


class E(A, C):  # mro рекурсивно обходит каждый наследуемый класс, и только в самом конце переходит к "object"
    def a_method(self):
        super().a_method()
        print(self.__class__.__mro__)


D().a_method()
print('\n')
E().a_method()
