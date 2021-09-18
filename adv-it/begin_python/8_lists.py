cars = ['vw',
        'lada',
        'geely',
        'volvo',
        'toyota']

for car in cars:
    print('The auto name is: ', car.title())

for car in range(0, 6, 2):
    print('Best auto is: ', cars[car].title())

numb_list = [0, 55555, 10, 100, 33, 56, 1893, 3, 456, 1]
max_numb = numb_list[0]
for n_ind in numb_list:
    if max_numb < n_ind:
        max_numb = n_ind

print('\nMax number of "numb_list" is: ', max_numb)

print('\n', '+'*5,  'Max number of "numb_list" is:', max(numb_list))

numb_list.sort(reverse=True)
print(numb_list[0])


