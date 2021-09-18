#       key: value
enemy = {
    'loc_x': 70,
    'loc_y': 150,
    'color': 'green',
    'health': 100,
    'name': 'Drakula'
}

print('It is X position: ', enemy['loc_x'], '\n'
      'It is Y position: ', enemy['loc_y'], '\n'
      'It is name is: ', enemy['name']
      )

enemy['rank'] = 'Focusnik'
print(enemy['rank'])

print(enemy)
del enemy['rank']
print(enemy)
enemy['loc_x'] += 10
print(enemy['loc_x'])
print(enemy.keys())
print(enemy.values())
