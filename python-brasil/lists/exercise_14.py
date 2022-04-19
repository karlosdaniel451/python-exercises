#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

months = ('january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december')

average_temperatures_per_month: list[float] = []

sum_of_average_temperature_per_month = 0
annual_average_temperature: float

months_with_temperature_above_annual_average: list[tuple[int, float]] = []

# Read the average temperature for each month from the user.
for month_and_temperature in months:
    average_temperatures_per_month.append(float(
        input(f'Enter the average temperature for {month_and_temperature.title()}: ')))
    sum_of_average_temperature_per_month += average_temperatures_per_month[-1]

annual_average_temperature = sum_of_average_temperature_per_month / len(months)

# Compute each month with average temperature above the annual average.
for index, average_temperature in enumerate(average_temperatures_per_month):
    if average_temperature > annual_average_temperature:
        months_with_temperature_above_annual_average.append(
            (index, average_temperature))


print(
    f'\nYearly average annual temperature: {annual_average_temperature} °C.\n')

print('Months with average temperature above the annual average:\n')
for month_and_temperature in months_with_temperature_above_annual_average:
    print(
        f'{months[month_and_temperature[0]].title()}, {month_and_temperature[1]} °C.')
