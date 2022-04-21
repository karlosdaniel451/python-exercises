#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User(object):

    def __init__(self, name: str, username: str):
        self.name = name
        self.username = username

    def __eq__(self, other):
        return self.username.lower() == other.username().lower()



def username_already_exists(username: str, users: list[User]) -> bool:
    for user in users:
        if user.username.lower() == username.lower():
            return True

    return False


registered_users: list[User] = []

while True:
    new_user_name = input('\nEnter the name of the new user or "stop" to cancel: ')

    if new_user_name == 'stop':
        break

    new_user_username = input('Enter the username of the new user: ')

    if username_already_exists(new_user_username, registered_users):
        print('Error, this username is unavailable.')
    else:
        registered_users.append(User(new_user_name, new_user_username))


print('\nRegistered users:\n')
for user in registered_users:
    print(f'{user.name} - {user.username}')

