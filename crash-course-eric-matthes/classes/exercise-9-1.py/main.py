#!/usr/bin/env python
# -*- coding: utf-8 -*-

from restaurant import Restaurant, IceCreamStand


def main():
    cafe_de_flore = Restaurant(name='Café de Flore', cuisine_type='café')
    cafe_de_flore.set_number_served(15)
    cafe_de_flore.increment_number_served(10)

    bacio_di_latte = IceCreamStand(
        name='Bacio di Latte', is_open=True, flavors=['chocolate', 'strawberry'])

    restaurants: list[Restaurant] = []
    restaurants.append(cafe_de_flore)
    restaurants.append(bacio_di_latte)

    describe_restaurants(restaurants)


def describe_restaurants(restaurants: list[Restaurant]):
    for restaurant in restaurants:
        print(restaurant.get_description())


if __name__ == '__main__':
    main()

