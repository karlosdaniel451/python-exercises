#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial
from io import StringIO


# For debuggin purposes.
def main():
    print(proteins('AUG'))


proteins_by_codon = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan'
}

stop_codons = ('UAA', 'UAG', 'UGA')


def proteins(strand: str) -> list[str]:
    proteins: list[str] = []

    for codon in iter(partial(StringIO(strand).read, 3), ''):
        if codon in stop_codons:
            return proteins

        proteins.append(proteins_by_codon[codon])

    return proteins


if __name__ == '__main__':
    main()
