#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
8-13. User Profile: Start with a copy of user_profile.py from page 149.
Build a profile of yourself by calling build_profile(), using your
first and last names and three other keyvalue pairs that describe you.
"""

def main():
    print(build_profile(first_name='Karlos', last_name='Silva', age=20,
                        country='Brazil', gender='Male'))


def build_profile(first_name: str, last_name: str, **user_info: dict) -> dict:
    """Build a dictionary containing everything we know about a user."""

    user_info['first_name'] = first_name
    user_info['last_name'] = last_name 

    return user_info


if __name__ == '__main__':
    main()

