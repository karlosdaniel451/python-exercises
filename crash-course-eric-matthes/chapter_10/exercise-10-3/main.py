#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
10-3. Guest: Write a program that prompts the user for their name. When
they respond, write their name to a file called guest.txt.
"""

FILENAME = './guest.txt'

user_name = input('Your name: ')

with open(FILENAME, 'w') as file_object:
    file_object.write(user_name)

