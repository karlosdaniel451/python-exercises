#!/usr/bin/env python
# -*- coding: utf-8 -*-


# For debuggin purposes.
def main():
    print(is_isogram('thumbscrew-japingly'))


def is_isogram(string: str) -> bool:
    for letter in string:
        if letter not in (' ', '-') and string.lower().count(letter) > 1:
            return False

    return True


if __name__ == '__main__':
    main()

