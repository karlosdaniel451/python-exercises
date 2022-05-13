#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

FILENAME = 'favourite_number.json'

def main():
    favourite_number: int

    try:
        with open(FILENAME) as f:
            favourite_number = json.load(f)
    except FileNotFoundError:
        favourite_number = get_new_favourite_number()
        save_favourite_number(favourite_number)

    print(f'Your favourite number is {favourite_number}.')


def get_new_favourite_number() -> int:
    """
    Get and return a new favourite number frou user through STDIN.
    """
    new_favourite_number: int
    while True:
        try:
            new_favourite_number = int(input(
                "We don't know your favourite number yet, please enter it: "))
        except ValueError:
            print('Error: invalid input. Please try again.\n')
        else:
            return new_favourite_number


def save_favourite_number(favourite_number: int) -> None:
    """
    Write a favourite number `FILENAME`.
    Warning: the file `FILENAME` will be re-written!
    """
    with open(FILENAME, 'w') as f:
        json.dump(favourite_number, f)


if __name__ == '__main__':
    main()

