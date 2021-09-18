
# OPEN function
# open('testtext.txt', mode='r') # open Read only
# open('testtext.txt', 'r')      # open Read only too

file = open('testtext.txt', 'w') # open Write mode. But file has rewritten !
print(type(file))

file.write('\nHello World !')   # write data to the file
file.close()     # close file to write data from buffer to the file

name = 'Larisa'
file = open('testtext.txt', 'a') # open Write mode with Append !
file.write('\nVery important message !')
file.write(f'\nHer name is {name}')
file.close()

# Context manager WITH - файл закрывается автоматически
with open('testtext.txt', 'a') as file:
    file.write('\nAnother new data')





