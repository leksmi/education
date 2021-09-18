#
# Enter login & password
login = input('Enter your username: ')
pass_key = input('Enter password: ')
#
while True:
    if (pass_key.lower() in login.lower()) or (len(pass_key) <= 8):
        print('Password is not correct ! Try again ..')
        pass_key = input('Enter password again: ')
    else:
        print('Login and passord are OK !')
        break
#
#
#
user_input = ''
if user_input:
    print('Your input is not empty!\n')
else:
    print('You enter nothing !')
#
#
# Ternary operator form:
print('Your input is not empty!\n') if user_input else print('You enter nothing !')
#

