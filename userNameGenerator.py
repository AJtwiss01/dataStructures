firstName = input('Enter your First Name: ')
lastName = input('Enter your Last Name: ')

username = firstName[0] + lastName[:7]
username = username.lower()

print('Your username is ', username)

