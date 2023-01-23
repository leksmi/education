from pprint import pp
from class3 import Verification
from tkinter import Tk, Button


class V2(Verification):
    def __init__(self, login, password):
        super().__init__(login, password)
        self.__save()

    def show(self):
        return self.login, self.password

    def __save(self):
        with open('users.txt', 'r') as r:
            for i in r:
                if f'{self.login, self.password}' in i:
                    raise ValueError('Запись уже существует !')
        super().save()


# x = V2('John', 'kRoss_1_3')
# pp(x.__dict__)
# print(x.show())

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.setUI()

    def setUI(self):
        button = Button(self, text='OK')  # запуск другого класса - композиция
        button.pack()


myapp = MyApp()
myapp.mainloop()
