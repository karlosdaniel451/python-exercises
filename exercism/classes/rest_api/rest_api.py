#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from typing import Optional

from user import User
from iou import IOU


class RestAPI:
    def __init__(self, database: dict[str, list[dict]]=None):
        self.database = database

    def get(self, url: str, payload: str=None):
        if payload:
            payload_dict = json.loads(payload)

        #  match url:
        #      case '/users':
        #          return {'users': self.get_all_users_sorted_by_name()}
        #      case _:
        #          pass
        if url == '/users':
            if payload is None:
                return json.dumps({'users': self.get_all_users_sorted_by_name()})

            user_name = payload_dict['users'][0]
            return json.dumps(
                {
                    'users': [self.get_user_dict_by_name(name=user_name)]
                }
            )
        

    def post(self, url: str, payload: str=None):
        if payload:
            json_payload = json.loads(payload)

        #  match url:
        #      case '/add':
        #          return self.add_user(user=user)
        #      case '/iou':
        #          iou = IOU(
        #              lender = json_payload['lender'],
        #              borrower = json_payload['borrower'],
        #              amount = json_payload['amount']
        #          )
        #          return self.add_iou(iou=iou)
        #      case _:
        #          pass

        if url == '/add':
            new_user = User(json_payload['user'])
            return json.dumps(self.add_user(user=new_user).__dict__ | {'balance': 0.0})

        if url == '/iou':
            iou = IOU(
                lender = json_payload['lender'],
                borrower = json_payload['borrower'],
                amount = json_payload['amount']
            )
            return json.dumps(
                {
                    'users': self.add_iou(iou)
                }
            )

    def get_all_users_sorted_by_name(self) -> list[User]:
        return sorted(self.database['users'], key=lambda user: user['name'])

    def get_user_dict_by_name(self, name) -> dict:
        for user_dict in self.database['users']:
            if user_dict['name'] == name:
                return user_dict

        return None

    def add_user(self, user: User) -> User:
        """
        Add a user to `self.database` and returns it.
        """
        self.database['users'].append(user)

        return user

    def add_iou(self, iou: IOU) -> dict:
        """
        Create an IOU and returns the updated database of users.
        """
        lender_user_dict = {}
        borrower_user_dict = {}

        # Update database.
        for user_dict in self.database['users']:
            if iou.lender == user_dict['name']:
                lender_user_dict = user_dict
                # If lender owes borrower.
                if iou.borrower in user_dict['owes']:
                    # If lender owes borrower less than new loan.
                    if iou.amount > user_dict['owes'][iou.borrower]:
                        user_dict['owed_by'][iou.borrower] = iou.amount - user_dict['owes'][iou.borrower]
                        del user_dict['owes'][iou.borrower]
                    # If lender owes borrower same as new loan.
                    elif iou.amount == user_dict['owes'][iou.borrower]:
                        del user_dict['owes'][iou.borrower]
                    else:
                        user_dict['owes'][iou.borrower] -= iou.amount
                else:
                    if iou.borrower in user_dict['owed_by']:
                        user_dict['owed_by'][iou.borrower] += iou.amount
                    else:
                        user_dict['owed_by'][iou.borrower] = iou.amount

                user_dict['balance'] = User.get_balance_of_user_dict(
                    user_dict=user_dict)

            if iou.borrower == user_dict['name']:
                borrower_user_dict = user_dict
                # If lender owes borrower.
                if iou.lender in user_dict['owed_by']:
                    # If lender owes borrower less than new loan.
                    if iou.amount > user_dict['owed_by'][iou.lender]:
                        user_dict['owes'][iou.lender] = iou.amount - user_dict['owed_by'][iou.lender]
                        del user_dict['owed_by'][iou.lender]
                    # If lender owes borrower same as new loan.
                    elif iou.amount == user_dict['owed_by'][iou.lender]:
                        del user_dict['owed_by'][iou.lender]
                    else:
                        user_dict['owed_by'][iou.lender] -= iou.amount
                else:
                    if iou.lender in user_dict['owes']:
                        user_dict['owes'][iou.lender] += iou.amount
                    else:
                        user_dict['owes'][iou.lender] = iou.amount

                user_dict['balance'] = User.get_balance_of_user_dict(
                    user_dict=user_dict)

        output = sorted([lender_user_dict, borrower_user_dict], key=lambda user: user['name'])
        return output

