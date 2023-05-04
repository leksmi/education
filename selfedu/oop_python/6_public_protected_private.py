from typing import Union


class Point:
    def __init__(self, a: int, b: int, x: Union[int, float], y: Union[int, float]):
        self.a = a
        self.b = b
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coords should be numbers')

    @staticmethod
    def __check_value(n) -> bool:
        return type(n) in (int, float)

    def set_coord(self, new_x, new_y):
        # это так называемый "сеттер":
        if self.__check_value(new_x) and self.__check_value(new_y):
            self.__x = new_x
            self.__y = new_y
        else:
            raise ValueError('Coords should be numbers')

    def get_coords(self):
        # это "геттер":
        return self.__x, self.__y


pt1 = Point(11, 22, 35, 56)
print(pt1.get_coords())
pt1.set_coord(new_x=77, new_y=88)
print(pt1.get_coords())
# pt1.set_coord(new_x=111, new_y='none')  # raise ValueError('Coords should be numbers')