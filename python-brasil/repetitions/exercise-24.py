#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

number_of_grades = int(input('Número de notas: '))
grades: list[int] = []
average: int

while number_of_grades <= 0:
    number_of_grades =  int(input('Número de notas inválido. Por favor, digite novamente: '))

for index in range(number_of_grades):
    
    grade = int(input(f'Valor para a nota {index + 1}: '))

    while grade < 0:
        grade = int(input('Nota inválida. Por favor, digite novamente: '))

    grades.append(grade)

average = sum(grades) / number_of_grades

print(f'Média das notas: {average}')

