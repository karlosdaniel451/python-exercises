#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string


ascii_lowercase_set = set(string.ascii_lowercase)

def main():
    print(is_pangram('abcdefghijklmnopqrstuvwxyz'))
    print(is_pangram('the quick brown fox jumps over the lazy dog'))
    print(is_pangram('a quick movement of the enemy will jeopardize five gunboats'))


def is_pangram(sentence: str) -> bool:
    # Alternative solution:
    #  #  alphabet_letters_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
    #  #                            'g': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
    #  #                            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
    #  #                            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0
    #  #                            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    #  alphabet_letters_count = {}
    #
    #  for alphabet_letter in string.ascii_lowercase:
    #      alphabet_letters_count[alphabet_letter] = 0
    #
    #  for letter in sentence.lower():
    #      if letter in string.ascii_lowercase:
    #          alphabet_letters_count[letter] += 1
    #
    #  for count in alphabet_letters_count.values():
    #      if count == 0:
    #          return False
    #
    #  return True

    return ascii_lowercase_set.issubset(set(sentence.lower()))


if __name__ == '__main__':
    main()

