#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.
"""

def count(string: str, letter: str) -> int:
    result = 0
    for i in string:
        if i == letter:
            result += 1

    return result


string = input('Enter some string: ')

whitespace_ocurrencies = count(string=string, letter=' ')

a_ocurrencies = count(string=string, letter=' ')
e_ocurrencies = count(string=string, letter='a')
i_ocurrencies = count(string=string, letter='e')
o_ocurrencies = count(string=string, letter='o')
u_ocurrencies = count(string=string, letter='u')

print(f"""Ocurrencies:\n
      whitespace: {count(string=string, letter=' ')}
      a: {a_ocurrencies}
      e: {i_ocurrencies}
      o: {i_ocurrencies}
      u: {u_ocurrencies}""")

