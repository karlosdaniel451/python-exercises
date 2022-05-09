#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    while True:
        try:
            number_1 = int(input('\nFirst number: '))
            number_2 = int(input('Second number: '))
        except ValueError:
            print('\nError! Please type a valid number.')
        else:
            sum = number_1 + number_2
            print(f'sum = {sum}')
            break


if __name__ == '__main__':
    main()

