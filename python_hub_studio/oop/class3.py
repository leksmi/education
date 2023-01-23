class A:
    def a(self):
        print('method from class A')


class B:
    def b(self):
        print('method from class B')


class C(B):
    def a(self):
        print('method from class C')


class D(C, A):  # порядок Важен ! super() отработает именно в этом порядке
    def a(self):
        super().a()
        print(f'{self.__class__.__mro__=}')  # __mro__ выводит порядок поиска методов в наследовании классов (поиск в глубину)


d1 = D()
d1.a()
print(D.__mro__)
print(B.__mro__)

class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenpassword()
        print(f'Отработал __init__ базового класса')

    def __lenpassword(self):
        if len(self.password) < 8:
            raise ValueError('Пароль короче 8 символов !')

    def save(self):
        with open('users.txt', 'a') as r:
            r.write(f'{self.login, self.password}\n')
