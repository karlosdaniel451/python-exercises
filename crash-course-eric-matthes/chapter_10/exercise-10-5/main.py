#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
10-5. Programming Poll: Write a while loop that asks people why they
like programming. Each time someone enters a reason, add their reason to
a file that stores all the responses.
"""

from typing import Final


FILENAME: Final = 'reasons_to_program.txt'

def main():    
    new_reasons: list[str] = []
    
    new_reason: str
    while True:
        new_reason = input('Add a reason why you like programming or'
                           ' type stop to stop program execution: ')
        if new_reason == 'stop':
            break

        new_reasons.append(new_reason)

    append_new_reasons(new_reasons)


def append_new_reasons(new_reasons: list[str]) -> None:
    with open(FILENAME, 'a') as file_object:
        for new_reason in new_reasons:
            file_object.write(new_reason + '\n')


if __name__ == '__main__':
    main() 

