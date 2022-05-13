from flask import current_app
from flask_executor import Executor
from yaml import load
from yaml import Loader

from accountbalance.accountbalanceupdater import AccountBalanceUpdater
from helpers.jsonresponsebuilder import JSONResponseBuilder

"""
This class is used to check account balance throughout the wagering day

Adopting AmTote FileBet Best practice: throughout the wagering day,
1. Call UpdateBalance() to insure winnings are applied to the balance
"""

class AccountBalance:
    def __init__(self, username, InvalidAPIUsage):
        stream = open("src/config.yaml", "r")
        params = load(stream, Loader=Loader)
        self.all_cmtys = params["all_cmtys"]
        self.InvalidAPIUsage = InvalidAPIUsage
        self.username = username

    def get(self):
        account_balance = AccountBalanceUpdater(
            self.username,
            self.InvalidAPIUsage
        ).update_balance()

        return JSONResponseBuilder(
            "Checked Balance Successfully, balances are: "
            +str(account_balance),
            201
        ).build()
