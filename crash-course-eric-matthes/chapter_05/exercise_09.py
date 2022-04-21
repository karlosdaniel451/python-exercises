#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of
users is not empty.

- If the list is empty, print the message We need to find some users!
- Remove all of the usernames from your list, and make sure
  the correct message is printed.
"""


usernames = ['admin', 'silva_789', 'maria_122', 'joao_321', 'john_55']

# usernames.clear()

if not usernames:
    print('We need to find some users!')
else:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report?\n')
        else:
            print(f'Hello {username}, thank you for logging in again.\n')



