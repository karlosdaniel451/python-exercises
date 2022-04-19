#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

numbers: list[int] = []

LIST_SIZE = 5

for i in range(LIST_SIZE):
    numbers.append(int(input('Enter some integer value: ')))


print('\nThe entered numbers were: ', end='')

for number in numbers:
    print(number, end=' ')

print()
