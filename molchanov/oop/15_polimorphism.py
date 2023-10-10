# Полиморфизм - разное поведение методы, в зависимости от
# данных (Классов), к которым он применен.
# Например операторы: 1+1=2, "1"+"1"="11",
# ['1', '2'] + ['3', '4'] = ['1', '2', '3', '4']
# По факту, за операциями скрывается вызов спец.методов (дандер методы):
# '1'.__add__('F')
# Полиморфизм больше относится именно к дандер (специальным) методам.


class Room:
    """
    Класс для создания площадей (комнаты)
    """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, room_obj: object):
        """
        Реализация сложения
        """
        if isinstance(room_obj, Room):
            return self.area + room_obj.area
        else:
            raise TypeError("Wrong object")

    def __eq__(self, room_obj: object) -> bool:
        """
        Реализация сравнения (оператор ==)
        """
        return self.area == room_obj.area

    def show_area(self):
        print(f"\nCurrent area: {self.area}")


room1 = Room(2, 7)
room2 = Room(3, 5)
room1.show_area()
print(room1 + room2)
print(room1 == room2)
room2.area = 14
print(room1 == room2)
