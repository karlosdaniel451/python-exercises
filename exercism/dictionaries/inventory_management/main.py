#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    print(create_inventory(["wood", "iron", "iron", "diamond", "diamond"]))
    print(add_items({"wood": 2, "gold": 1, "diamond": 3}, ["wood", "gold", "gold"]))
    print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))


"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]) -> dict[str, int]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = {}

    for item in set(items):
        inventory[item] = items.count(item)

    return inventory

def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    updated_inventory = inventory.copy()

    new_items_dictionary = create_inventory(items)

    for item, amount_of_item in new_items_dictionary.items():
        if item in updated_inventory:
            updated_inventory[item] += amount_of_item
        else:
            updated_inventory[item] = amount_of_item

    return updated_inventory


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    updated_inventory = inventory.copy()

    for item in set(items):
        if updated_inventory[item] - items.count(item) > 0:
            updated_inventory[item] -= items.count(item)
        else:
            updated_inventory[item] = 0

    return updated_inventory


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    updated_inventory = inventory.copy()

    if item in updated_inventory:
        del updated_inventory[item]

    return updated_inventory


def list_inventory(inventory: dict[str, int]) -> list[tuple[str, int]]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    #return list((item, amount_of_item) for item, amount_of_item in inventory.items() if amount_of_item > 0)
    return [(item, amount_of_item) for item, amount_of_item in inventory.items() if amount_of_item > 0]

    #return tuple([(item, amount_of_item) for inventory.items() if amount_of_item > 0])


if __name__ == '__main__':
    main()

