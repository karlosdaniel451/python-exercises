#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User:
    def __init__(self, name: str, owes: dict[str, float]={},
                 owed_by: dict[str, float]={}):
        self.name = name
        self.owes = owes
        self.owed_by = owed_by

    @staticmethod
    def get_balance_of_user_dict(user_dict: dict) -> float:
        balance = 0.0

        # Compute total owed to others.
        for value in user_dict['owes'].values():
            balance -= value

        # Compute total owed by others.
        for value in user_dict['owed_by'].values():
            balance += value

        return balance

        
    #  def get_balance(self) -> float:
    #      """
    #      (total owed by other users) - (total owed to other users).
    #      """
    #      balance = 0
    #
    #      # Compute total owed to others.
    #      for value in self.owes.values():
    #          balance -= value
    #
    #      # Compute total owed by others.
    #      for value in self.owe_by.values():
    #          balance += value
    #
    #      return balance


    #  @property
    #  def balance(self) -> float:
    #      """
    #      (total owed by other users) - (total owed to other users)
    #      """
    #      balance = 0
    #
    #      # Compute total owed to others.
    #      for value in self.owes.values():
    #          balance -= value
    #
    #      # Compute total owed by others.
    #      for value in self.owe_by.values():
    #          balance += value
    #
    #      return balance

    #  @property.setter
    #  def balance(self):
    #      raise ValueError('balance is read-only')

