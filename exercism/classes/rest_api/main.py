#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from rest_api import RestAPI


def main():
    pass
    # No users
    #  database = {'users': []}
    #  api = RestAPI(database=database)
    #
    #  response = api.get(url='/users')
    #  expected = {'users': []}
    #  print(response)
    #  print(json.loads(response) == expected)

    # Both users has 0 balance.
    #  database = {
    #      "users": [
    #          {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
    #          {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
    #      ]
    #
    #  }
    #  api = RestAPI(database)
    #  payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
    #  response = api.post("/iou", payload)
    #  expected = {
    #      "users": [
    #          {"name": "Adam", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
    #          {"name": "Bob", "owes": {"Adam": 3.0}, "owed_by": {}, "balance": -3.0},
    #      ]
    #  }
    #  print(type(response))
    #  print(response)

    # Add user.
    #  database = {"users": []}
    #  api = RestAPI(database)
    #  payload = json.dumps({"user": "Adam"})
    #  response = api.post("/add", payload)
    #  expected = {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0}
    #
    #  print(type(expected))
    #  print(expected)
    #
    #  print(type(response))
    #  print(response)

    # Get single user.
    #  database = {
    #      "users": [
    #          {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
    #          {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
    #      ]
    #  }
    #  api = RestAPI(database)
    #  payload = json.dumps({"users": ["Bob"]})
    #  response = api.get("/users", payload)
    #  expected = {
    #      "users": [{"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0}]
    #  }
    #
    #  print(type(expected))
    #  print(expected)
    #
    #  print(type(response))
    #  print(response)

    # Bottower has negative balance.
    #  database = {
    #      "users": [
    #          {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
    #          {"name": "Bob", "owes": {"Chuck": 3.0}, "owed_by": {}, "balance": -3.0},
    #          {"name": "Chuck", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
    #      ]
    #  }
    #  api = RestAPI(database)
    #  payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
    #  response = api.post("/iou", payload)
    #  expected = {
    #      "users": [
    #          {"name": "Adam", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
    #          {
    #              "name": "Bob",
    #              "owes": {"Adam": 3.0, "Chuck": 3.0},
    #              "owed_by": {},
    #              "balance": -6.0,
    #          },
    #      ]
    #  }
    #
    #  print(json.dumps(expected), end='\n\n')
    #
    #  print(response)

    # Lender owes borrower.
    #  database = {
    #      "users": [
    #          {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
    #          {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
    #      ]
    #  }
    #  api = RestAPI(database)
    #  payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 2.0})
    #  response = api.post("/iou", payload)
    #  expected = {
    #      "users": [
    #          {"name": "Adam", "owes": {"Bob": 1.0}, "owed_by": {}, "balance": -1.0},
    #          {"name": "Bob", "owes": {}, "owed_by": {"Adam": 1.0}, "balance": 1.0},
    #      ]
    #  }
    #
    #  print(json.dumps(expected), end='\n\n')
    #  print(response)

    # Lender owes borrower less than new loan.
    #  database = {
    #      "users": [
    #          {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
    #          {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
    #      ]
    #  }
    #  api = RestAPI(database)
    #  payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 4.0})
    #  response = api.post("/iou", payload)
    #  expected = {
    #      "users": [
    #          {"name": "Adam", "owes": {}, "owed_by": {"Bob": 1.0}, "balance": 1.0},
    #          {"name": "Bob", "owes": {"Adam": 1.0}, "owed_by": {}, "balance": -1.0},
    #      ]
    #  }
    #
    #  print(json.dumps(expected), end='\n\n')
    #  print(response)

    # Lender owes borrower same as new loan.
    #  database = {
    #      "users": [
    #          {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
    #          {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
    #      ]
    #  }
    #  api = RestAPI(database)
    #  payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
    #  response = api.post("/iou", payload)
    #  expected = {
    #      "users": [
    #          {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
    #          {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
    #      ]
    #  }
    #
    #  print(json.dumps(expected), end='\n\n')
    #  print(response)

if __name__ == '__main__':
    main()

