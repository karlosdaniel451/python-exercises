def ask_for_name() -> str:
    return input('Name: ')

def ask_for_password() -> str:
    return input('Password: ')


name = ask_for_name()
password = ask_for_password()

while name == password:
    print('\nError! Password cannot be equals to the name. Please try it again.\n')
    name = ask_for_name()
    password = ask_for_password()


print('\nSuccess...')
