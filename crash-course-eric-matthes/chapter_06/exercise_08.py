#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In
each dictionary, include the kind of animal and the owner’s name. Store these dictionaries
in a list called pets . Next, loop through your list and as you do, print everything you
know about each pet.6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In
each dictionary, include the kind of animal and the owner’s name. Store these dictionaries
in a list called pets . Next, loop through your list and as you do, print everything you
know about each pet.
"""

pets: list[dict] = []

pet_animal: str
pet_owner: str

while True:
    pet_animal  = input('\nEnter the kind of animal of the new pet or "c" to cancel: ')
    if pet_animal == 'c':
        break

    pet_owner = input("Enter the owner's name: ")

    pets.append({'pet_animal': pet_animal, 'pet_owner': pet_owner})


print()
for pet in pets:
    print(f"pet animal: {pet['pet_animal']}, owner: {pet['pet_owner']}")

