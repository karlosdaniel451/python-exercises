#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
"""

multiples_of_three = [i for i in range(3, 31, 3)]
# alternative: multiples_of_three = [i for i in range(3, 31) if i % 3 == 0]

for i in multiples_of_three:
    print(i, end= ' ')

print()

