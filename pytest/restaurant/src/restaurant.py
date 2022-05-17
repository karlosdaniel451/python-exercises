#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field

from src.dish import Dish
from src.order import Order


class NoOrderYetError(Exception):
    """
    This exception should be raised when it is tried to do some operation
    which requires that `order_queue` of a Restaurant is not empty, but in
    fact, it is empty.
    """
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

class RestaurantIsClosedError(Exception):
    """
    This exception should be raised when it is tried to do some operation
    which requires that a Restaurant is opened, but in fact, it is closed.
    """
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

@dataclass
class Restaurant:
    name: str
    is_open: bool = False
    __menu: set[Dish] = field(default_factory=set, init=False)
    order_queue: list[Order] = field(default_factory=list, init=False)

    #  @property
    #  def is_open(self) -> bool:
    #      return self.is_open

    def open_restaurant(self):
        self.is_open = True

    def close_restaurant(self):
        if self.order_queue:
            raise ValueError('Restaurant has some orders to be serviced yet.')

        self.is_open = False

    @property
    def number_of_orders(self) -> int:
        return len(self.order_queue)

    @property
    def number_of_available_dishes(self) -> int:
        return len(self.__menu)

    def add_dish_to_menu(self, dish: Dish):
        if dish in self.__menu:
            raise ValueError('There is no such a dish in the menu.')
        
        self.__menu.add(dish)

    def get_menu(self) -> set[Dish]:
        return self.__menu


    def push_order_to_order_queue(self, order: Order):
        """
        Add order to the end of order queue.
        """
        if not self.is_open:
            raise RestaurantIsClosedError('Restaurant is not opened.')

        self.order_queue.append(order)

    def pop_first_order_from_order_queue(self) -> Order:
        """
        Get and remove the first order of order queue.
        """
        if not self.is_open:
            raise RestaurantIsClosedError('Restaurant is not opened.')

        if not self.order_queue:
            raise NoOrderYetError('There is no order in the order queue.')

        return self.order_queue.pop(0)

    def get_first_order_from_order_queue(self) -> Order:
        """
        Get (AND NOT REMOVE) the first order of order queue.
        """
        if not self.is_open:
            raise RestaurantIsClosedError('Restaurant is closed.')

        if not self.order_queue:
            raise NoOrderYetError('There is no order in the order queue.')

        return self.order_queue[0]

