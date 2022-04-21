#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e
mostre a soma dos quadrados dos elementos do vetor.
"""

from typing import Final

numbers: list[int] = []
LIST_LENGTH: Final = 10
sum_of_squares: int

for _ in range(LIST_LENGTH):
    numbers.append(int(input()))

sum_of_squares = sum([number ** 2 for number in numbers])

print(f'sum of squares = {sum_of_squares}')

