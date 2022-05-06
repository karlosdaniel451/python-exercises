#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


possible_results = (list(range(0,11)) + ['a', 'e', 'i', 'o', 'u'])

def main():
    results = set()
    for _ in range(4):
        new_result = random.choice(possible_results)

        # Ensure that there is no repeated result.
        while new_result in results:
            new_result = random.choice(possible_results)

        results.add(new_result)

    for possible_result in possible_results:
        print(possible_result, end=' ')
    print()

    for result in results:
        print(result, end=' ')
    print()

if __name__ == '__main__':
    main()

