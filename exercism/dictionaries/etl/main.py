#!/usr/bin/env python
# -*- coding: utf-8 -*-


# For debuggin purposes.
def main():
    print(transform(legacy_data={1: ['A']}))
    print(transform(legacy_data={1: ['A', 'E', 'I', 'O', 'U']}))
    print(transform(legacy_data={1: ['A', 'E'], 2: ['D', 'G']}))


def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    transformed_data = {}

    for point, letters in legacy_data.items():
        for letter in letters:
            transformed_data[letter.lower()] = point

    return transformed_data


if __name__ == '__main__':
    main()

