#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
"""


def print_string_in_vertical_in_stairs2(string: str) -> None:
    for i in range(len(string) + 1):
        print(string[0:len(string) - i])


print_string_in_vertical_in_stairs2('karlos')
print('')

print_string_in_vertical_in_stairs2('asdf')
print('')

print_string_in_vertical_in_stairs2('342332')
print('')

