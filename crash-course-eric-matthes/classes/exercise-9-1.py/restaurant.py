#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Restaurant:
    def __init__(self, name: str, cuisine_type: str, is_open=False):
        self.name = name
        self.cuisine_type = cuisine_type
        self.is_open = is_open
        self.number_served = 0

    def get_description(self):
        return(f'name: {self.name} - cuisine type: {self.cuisine_type} - is'
               f' open: {self.is_open} - number served = {self.number_served}')

    def open_itself(self):
        self.is_open = True

    def close_itself(self):
        self.is_open = False

    def set_number_served(self, number_served: int):
        if number_served <= 0:
            raise ValueError('Invalid number served.')

        self.number_served = number_served

    def increment_number_served(self, number_served: int):
        if number_served <= 0:
            raise ValueError('Invalid number served.')

        self.number_served += number_served


class IceCreamStand(Restaurant):
    def __init__(self, name: str, is_open=False, flavors: list[str] = []):
        super().__init__(name, 'Ice Cream Stand', is_open)
        self.flavors=flavors

    def get_description(self):
        return super().get_description() + f' - flavors: {self.flavors}'

