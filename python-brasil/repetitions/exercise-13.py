"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Não utilize a função de potência da
linguagem.
"""

def get_pow(base: int, expoent: int) -> int:
    result = 1
    count = 1
    while count <= expoent:
        result *= base
        count += 1

    return result

def get_pow2(base: int, expoent: int) -> int:
    result = 1
    for i in range(expoent):
        result *= base
    
    return result

base = int(input())
expoent = int(input())

print(get_pow(base, expoent))
print(get_pow2(base, expoent))
print(pow(base, expoent))
