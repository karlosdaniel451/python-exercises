#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
"""

def print_string_in_vertical_in_stairs(string: str) -> None:
    #  for index, letter in enumerate(string):
    #      print(string[0:index])
    #

    for i in range(len(string) + 1):
        print(string[0:i])


print_string_in_vertical_in_stairs('karlos')
print('')

print_string_in_vertical_in_stairs('asdf')
print('')

print_string_in_vertical_in_stairs('342332')
print('')



