#!/usr/bin/env python
# -*- coding: utf-8 -*-


def convert(number: int) -> str:
    output = ''

    if number % 3 == 0:
        output += 'Pling'
    if number % 5 == 0:
        output += 'Plang'
    if number % 7 == 0:
        output += 'Plong'

    return output if output != '' else str(number)

