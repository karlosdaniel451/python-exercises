#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from src.restaurant import Dish
from src.restaurant import Order
from src.restaurant import Restaurant
from src.restaurant import NoOrderYetError
from src.restaurant import RestaurantIsClosedError


@pytest.mark.restaurant
def test_number_of_orders_when_there_is_no_order_then_should_return_0():
    restaurant = Restaurant(name='Restaurant for tests', is_open=True)

    assert restaurant.number_of_orders == 0

    
@pytest.mark.restaurant
def test_number_of_orders_when_there_is_only_one_order_then_should_return_1():
    restaurant = Restaurant(name='Restaurant for tests', is_open=True)

    dish = Dish(
        name='Dish for tests',
        ingredients=['ingredient 1', 'ingredient 2'],
        unit_price_in_cents=20_00)

    order = Order(client_name='Client for tests', dish=dish, quantity=2)

    restaurant.push_order_to_order_queue(order=order)

    assert restaurant.number_of_orders == 1


@pytest.mark.restaurant
def test_number_of_orders_when_there_are_many_orders_of_single_dish():
    restaurant = Restaurant(name='Restaurant for tests', is_open=True)

    dish = Dish(
        name='Dish for tests',
        ingredients=['ingredient 1', 'ingredient 2'],
        unit_price_in_cents=20_00)

    order_1 = Order(client_name='Client for tests 1', dish=dish, quantity=2)
    order_2 = Order(client_name='Client for tests 2', dish=dish, quantity=1)
    order_3 = Order(client_name='Client for tests 3', dish=dish, quantity=3)

    restaurant.push_order_to_order_queue(order=order_1)
    restaurant.push_order_to_order_queue(order=order_2)
    restaurant.push_order_to_order_queue(order=order_3)

    assert restaurant.number_of_orders == 3

@pytest.mark.restaurant
def test_number_of_orders_when_there_are_many_orders_of_many_dishes():
    restaurant = Restaurant(name='Restaurant for tests', is_open=True)

    dish_1 = Dish(
        name='Dish for tests',
        ingredients=['ingredient 1', 'ingredient 2'],
        unit_price_in_cents=20_00)

    dish_2 = Dish(
        name='Dish for tests 2',
        ingredients=['ingredient 5', 'ingredient 6', 'ingredient 7'],
        unit_price_in_cents=20_00)

    order_1 = Order(client_name='Client for tests 1', dish=dish_1, quantity=2)
    order_2 = Order(client_name='Client for tests 2', dish=dish_2, quantity=1)
    order_3 = Order(client_name='Client for tests 3', dish=dish_1, quantity=3)

    restaurant.push_order_to_order_queue(order=order_1)
    restaurant.push_order_to_order_queue(order=order_2)
    restaurant.push_order_to_order_queue(order=order_3)

    assert restaurant.number_of_orders == 3


@pytest.mark.restaurant
def test_get_first_order_from_order_queue_when_there_is_no_order_then_should_raise_NoOrderYetError():
    restaurant = Restaurant(name='Restaurant for tests', is_open=True)

    with pytest.raises(NoOrderYetError):
        restaurant.get_first_order_from_order_queue()


@pytest.mark.restaurant
def test_push_order_to_order_queue_when_restaurant_is_closed_then_should_raise_RestaurantIsClosedError():
    restaurant = Restaurant(name='Restaurant for tests', is_open=False)

    dish = Dish(
        name='Dish for tests',
        ingredients=['ingredient 1', 'ingredient 2'],
        unit_price_in_cents=20_00)

    order = Order(client_name='Client for tests', dish=dish, quantity=2)

    with pytest.raises(RestaurantIsClosedError):

        restaurant.push_order_to_order_queue(order=order)
