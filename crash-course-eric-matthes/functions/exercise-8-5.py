#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and
its country. The function should print a simple sentence, such as Reykjavik is in
Iceland. Give the parameter for the country a default value. Call your function for three
different cities, at least one of which is not in the default country.
"""

def main():
    for capital, country in countries_by_capital.items():
        describe_city(city_name=capital, city_country=country)


countries_by_capital = {
    'Brasília': 'Brazil',
    'Buenos Aires': 'Argentina',
    'Ottawa': 'Canada',
    'Washington': 'United States of America',
    'Beijing': 'China',
    'Berlin': 'Germany',
    'Paris': 'France',
    'Madri': 'Spain',
    'Amsterdam': 'Netherlands'
}

def describe_city(city_name: str, city_country):
    print(f'{city_name} is in {city_country}.')


if __name__ == '__main__':
    main()

