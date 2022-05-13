from flask import current_app
from flask_executor import Executor
from helpers.jsonresponsebuilder import JSONResponseBuilder
from placingorder.orderplacer import OrderPlacer

class PlacingOrder:
    def __init__(self, data, username, InvalidAPIUsage):
        self.InvalidAPIUsage = InvalidAPIUsage
        self.data = data
        self.username = username

    def post(self):
        response = \
            OrderPlacer(self.InvalidAPIUsage, self.username)\
                .place(self.data)

        return JSONResponseBuilder(
            response, 
            201
        ).build()