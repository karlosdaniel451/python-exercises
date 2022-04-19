#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

CONSONANTS = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

NUMBER_OF_CHARACTERS = 10

characters: list[str] = []
number_of_consonants = 0

for i in range(NUMBER_OF_CHARACTERS):
    characters.append(input('Enter some character: '))
    while len(characters[i]) > 1:
        characters[i] = input(
            'Error! Please enter a character, not a series of character: ')

    if characters[i] in CONSONANTS:
        number_of_consonants += 1


print('The consonants entered were:\n')
for character in characters:
    if character in CONSONANTS:
        print(character, end=' ')

print()
