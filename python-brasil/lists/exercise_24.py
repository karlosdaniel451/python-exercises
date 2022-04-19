#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor
foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados
"""

import random

faces: list[int] = []
frequencies: list[int] = [0, 0, 0, 0, 0, 0]

number_of_rollings = int(input('Enter the number of rollings: '))

while number_of_rollings <= 0:
    number_of_rollings = int(
        input('Error! Enter the number of rollings: (> 0) '))

for i in range(number_of_rollings):
    faces.append(random.randint(1, 6))
    frequencies[faces[-1] - 1] += 1

user_answer_if_it_wants_to_see_the_faces = input(
    'Do you want to see the numbers obtained with the rolls of the dice? (y or n) ')

while user_answer_if_it_wants_to_see_the_faces not in ('y', 'n'):
    user_answer_if_it_wants_to_see_the_faces = input(
        'Invalid option! Do you want to see the numbers obtained with the rolls of the dice? (y or n) ')

user_wants_to_see_faces = user_answer_if_it_wants_to_see_the_faces == 'y'

if user_wants_to_see_faces:
    print('\nFaces obtained:')
    for face in faces:
        print(face, end=' ')
    print()

print('\nFrequency of each face:\n')
for index, frequency in enumerate(frequencies):
    print(f'{index + 1}: {frequency}')
