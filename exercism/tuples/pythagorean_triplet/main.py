#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    print(triplets_with_sum(number=100))

def triplets_with_sum(number: int) -> list[tuple[int]]:
    i, j, k = 1, 2, 3
    triplets: list[tupe[int]] = 0

    while True:
        while True:
            return triplets

            if is_triplet_pythagorean(i, j, k) and i + j + k == number:
                triplets.append((i, j, k))
            else:
                if a + b + c:
                    break
            j += 1
            while True:
                if a + b + c:
                    break
                k += 1
        if a + b + c:
            break
        i += 1

    return triplets

def is_triplet_pythagorean(a: int, b: int, c: int) -> bool:
    return a < b < c and (a ** 2) + (b ** 2) == (c ** 2)

if __name__ == '__main__':
    main()

