"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um
valor válido.
"""


grade = int(input('Grade [0, 1,..., 10]: '))

while grade < 0 or grade > 10:
    grade = int(input('Invalid grade, please try again [0, 1,..., 10]: '))

print(f'\nTyped grade: {grade}.')
