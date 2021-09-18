
x = int(input('Enter your number: '))
y = input('Enter Y: ')
if x == 100:
    print('You have entered nice number !:', x)
elif (x <= 30) and (x >= 20):
    print('Yor number is in 20...30 range')
else:
    print('Try another !')
print(type(y))

cars_list = ['Lada',
             'Renault',
             'Citroen',
             'Geely',
             'Toyota',
             'Ford']
car_name = input("Enter car's name: ")
print(type(cars_list))
if cars_list[0].lower() == car_name.lower():
    print('Lada is first !')
else:
    print('There is no interesting car in first position!')
