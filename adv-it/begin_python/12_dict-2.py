
enemy = {
    'loc_x': 70,
    'loc_y': 150,
    'color': 'green',
    'health': 100,
    'name': 'Drakula',
    'awards': ['Silver', 'Gold'],
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

print(type(enemy), '\n')

enemy_list = []
print(type(enemy_list))

for ind in range(0, 10):
    enemy_list.append(enemy)

for enemy in enemy_list:
    print(enemy)

print('-'*20, '*'*20, '-'*20)

enemy_list[4]['health'] = 70
for enemy in enemy_list:
    print(enemy)

print('\n'*3, 'File name for this: ', __file__)


