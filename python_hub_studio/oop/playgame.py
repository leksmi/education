from class3PyHS import Player

gamer1 = Player()
print(gamer1.lvl)
gamer1.lvl = 7
print(gamer1.lvl)
gamer1.set_cls_fields()  # без аргументов установит значения по умолчанию для КЛАССА !
gamer1.show_cls_fields()
gamer2 = Player()
gamer2.lvl = 4
print(gamer2.lvl)
gamer2.lvl = 4.5
