"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""

number1 = int(input())
number2 = int(input())

print(list(range(number1, number2 + 1)))


for i in range(number1, number2 + 1):
    print(i, end=', ')


print()

count = number1
while count <= number2:
    print(count, end=', ')
    count += 1

