#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""

def get_number_of_digits(number: int) -> int:
    if number == 0:
        return 1

    return int(math.log10(number) + 1)


print(get_number_of_digits(0))
print(get_number_of_digits(1))
print(get_number_of_digits(2))
print(get_number_of_digits(10))
print(get_number_of_digits(11))
print(get_number_of_digits(20))
print(get_number_of_digits(21))
print(get_number_of_digits(99))
print(get_number_of_digits(100))
print(get_number_of_digits(101))
print(get_number_of_digits(1000))
print(get_number_of_digits(1001))

