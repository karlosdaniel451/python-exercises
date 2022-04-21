"""
Faça um programa que itera em uma string e toda vez que uma vogal aparecer
imprima o seu nome entre as letras.
"""

vowels = ['a', 'e', 'i', 'o', 'u']

string = 'bananas'

for letter in string:
    if letter.lower() in vowels:
        print('Karlos')
    else:
        print(letter)
