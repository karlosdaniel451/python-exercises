#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Data com mês por extenso. Construa uma função que receba uma data no
formato DD/MM/AAAA e devolva uma string no formato 'D de mesPorExtenso
de AAAA'. Opcionalmente, valide a data e retorne NULL caso a data seja
inválida.
"""

from months import months_of_the_year


def main():
    date = input()

    try:
        formatted_date = get_formatted_date(date)
    except ValueError as error:
        print(error)
        exit()
        

    print(get_formatted_date(date))


def get_formatted_date(date: str) -> str:
    day_number, month_number, year_number = extract_date(date)

    if month_number < 0 or month_number > 12:
        raise ValueError('Invalid month number.')

    month_name = months_of_the_year[month_number - 1]

    return f'{day_number} de {month_name} de {year_number}'


def extract_date(date: str) -> tuple[int, int, int]:
    date = date.replace('/', '')

    day_number = int(date[0:2])
    month_number = int(date[2:4])
    year_number = int(date[4:9])

    return (day_number, month_number, year_number)


if __name__ == '__main__':
    main()

