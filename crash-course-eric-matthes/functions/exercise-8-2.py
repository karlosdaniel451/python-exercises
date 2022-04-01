#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my favorite
books is Alice in Wonderland. Call the function, making sure to include a book title
as an argument in the function call.
"""


def favorite_book(title: str) -> None:
    print(f'My favourite book is {title}')


favorite_book(title='Fanhreint 451')
print('')

favorite_book(title='Animal farm')
print('')


