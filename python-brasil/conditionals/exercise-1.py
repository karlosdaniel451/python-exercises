def get_greatest_number(a: int, b: int) -> int:
    if (a > b):
        return a
    elif a < b:
        return b
    else:
        return None
    

number1 = int(input('\nDigite um número inteiro qualquer: '))
number2 = int(input('\nDigite outro um número inteiro qualquer: '))

greatest_number = get_greatest_number(number1, number2)

if (greatest_number == None):
    print('\nOs dois números digitados são iguais.\n')
else:
    print(f'\nO maior número digitado é: {greatest_number}\n')

