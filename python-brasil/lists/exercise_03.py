#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

from typing import Final


NUMBER_OF_GRADES: Final = 4

grades: list[float] = []
grade_sum = 0.0


for i in range(NUMBER_OF_GRADES):
    new_grade = float(input(f'Grade {i+1}: '))
    grades.append(new_grade)
    grade_sum += new_grade


grade_average = grade_sum / NUMBER_OF_GRADES

print(f'\nGrade average: {(grade_average)}')
