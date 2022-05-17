#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytest import mark

from src.order import Order
from src.dish import Dish
from src.restaurant import Restaurant

@mark.order
@mark.parametrize(
    'dish_unit_price_in_cents, quantity',
    [
        (15_00, 2),
        (11_00, 1),
        (40_00, 10),
    ]
)
def test_get_total_price_in_cents(dish_unit_price_in_cents, quantity):
    dish = Dish(
        name='dish for tests',
        ingredients=['ingredient 1', 'ingredient 2'],
        unit_price_in_cents=dish_unit_price_in_cents)

    order = Order(client_name='client for tests', dish=dish, quantity=quantity)

    assert dish_unit_price_in_cents * quantity == order.get_total_price_in_cents()

