#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for
informado um valor igual a -1 (que não deve ser armazenado). Após
esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
"""


def main():
    grades: list[float] = []

    new_grade = 0
    while True:
        new_grade = int(input('Enter a new grade: '))
        if new_grade == -1:
            break

        if new_grade < 0:
            print('Error! The grade should not be negative. Please try again.')
            continue
 
        grades.append(new_grade)

    average_grade = sum(grades) / len(grades) if len(grades) > 0 else 0

    print(
        f'''Number of entered grades: {len(grades)}\n'''
        f'''Entered grades: {grades}\n'''
        f'''Entered grandes in reverse order: {grades[::-1]}\n'''
        f'''Sum of all grades: {sum(grades)}\n'''
        f'''Average grade: {average_grade}\n'''
        f'''Number of grades above average:'''
        f''' {len([grade for grade in grades if grade > average_grade])}\n'''
        f'''Number of grades above 7:'''
        f''' {len([grade for grade in grades if grade > 7])}\n''')


if __name__ == '__main__':
    main()

