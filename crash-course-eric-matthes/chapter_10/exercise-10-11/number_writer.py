#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Final


FILENAME: Final = 'favourite_number.json'

def main():
    while True:
        try:
            favourite_number = int(input('What is your favourite number? '))
        except ValueError:
            print('Error: invalid input. Please try again.\n')
        else:
            print('\nNumber saved successfully.')
            break

    with open(FILENAME, 'w') as f:
        json.dump(favourite_number, f)


if __name__ == '__main__':
    main()

