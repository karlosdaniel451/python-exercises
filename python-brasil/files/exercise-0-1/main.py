#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços
IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos
e inválidos.
"""

import ipaddress


def main():
    source_filename = input('Enter the name of the file of the IPv4 addresses: ')
    destination_file = input('Enter the name of the destination file: ')

    ipv4_addresses: list[str] = []

    try:
        with open(source_filename) as f:
            ipv4_addresses = f.readlines()
    except FileNotFoundError:
        print(f'Error! {source_filename} not found.')
        exit(1)


    with open(destination_file, mode='a') as f:
        for ipv4_address in ipv4_addresses:
            if is_ipv4_address_valid(ipv4_address.strip()):
                f.write(ipv4_address)


def is_ipv4_address_valid(ipv4_address: str) -> bool:
    try:
        ipaddress.ip_address(ipv4_address)
    except ValueError:
        print(f'{ipv4_address} is invalid.')
        return False

    print(f'{ipv4_address} is valid.')
    return True


if __name__ == '__main__':
    main()

