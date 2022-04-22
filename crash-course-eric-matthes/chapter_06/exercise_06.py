#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""

rivers = {'nile': 'egypt', 'amazon': 'brazil', 'rhine': 'germany'}

# Print the pairs river, country.
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')


# Print the rivers.
print('\nRivers: ', end=' ')
for river in rivers.keys():
    print(river.title(), end=' ')
print()

# Print the countries.
print('\nCountries: ', end=' ')
for country in rivers.values():
    print(country.title(), end=' ')
print()

