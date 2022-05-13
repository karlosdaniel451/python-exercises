#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Final


FILENAME: Final = 'favourite_number.json'

def main():
    try:
        with open(FILENAME) as f:
            favourite_number = json.load(f)
    except FileNotFoundError:
        print(f'Error: file "{FILENAME}" not found.')
        exit(1)
    else:
        print(f"I know your favourite number! It's {favourite_number}.")


if __name__ == '__main__':
    main()

