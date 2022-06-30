class Point:
    """
    Создание точек и их координат
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        # когда больше нет ссылок на объект, он удаляется
        # непосредственно перед удалением вызывается метод __del__
        # и после отработки __del__ объект сразу удаляется
        print(f'Отработал финализатор __del__ для: {self}\nдалее объект будет удален.')

    def set_coords(self, new_x, new_y):
        print('Установка новых x, y')
        self.x = new_x
        self.y = new_y

    def show_coords(self):
        print(f'Объект: {self}\nx={self.x}\ny={self.y}')


pt1 = Point(10, 20)
print(f'{pt1} {pt1.__dict__}')
pt2 = Point()
print(f'{pt2} {pt2.__dict__}')

pt1.set_coords(101, 202)
pt1.show_coords()
pt2.set_coords(new_y=555, new_x=333)
pt2.show_coords()
