#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

from typing import Final


numbers: list[float] = []

LIST_SIZE: Final = 10

for i in range(LIST_SIZE):
    numbers.append(float(input('Enter some real number: ')))


numbers.reverse()

print('\nIn reverse order, the enter numbers were: ', end='')

for number in numbers:
    print(number, end=' ')

print()
