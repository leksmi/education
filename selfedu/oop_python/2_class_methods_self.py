# class ИмяКласса:
#    данные (атрибуты, они же свойства)
#    методы (действия)
#
# имена Методов являются атрибутами Классов, но ведут не к Данным а к Функциям !

from rich import print


class Point:  # Класс образует пространство имен (scope)
    """Класс для определения точек"""
    color = 'red'  # атрибут
    circle = 2  # атрибут

    def set_coords(self,x=0 ,y=0):  # объявление метода класса. Self это ссылка на Объект созданный от данного Класса
        print(f'Вызов метода set_ccords объекта {self}\nустановка x y:')
        self.x = x
        self.y = y
        return 0

    def get_coords(self):
        return self.x, self.y # вернет кортеж


print(f'set_coords это есть: {Point.set_coords}')
# print(f'Возврат от set_coords :\n{Point.set_ccords()}')

pt = Point()
pt.set_coords()
print(pt.__dict__)

pt.set_coords(11,12)
print(pt.__dict__)
print(pt.get_coords())

pt2 = Point()
pt2.set_coords(21,22)
print(pt2.__dict__)
print(pt2.get_coords())

# так как имена методов это атрибуты Класса
f = getattr(pt, 'get_coords')  # в f присваиваем атрибут (делаем доп.ссылку)
print(f())                     # вызываем атрибут
