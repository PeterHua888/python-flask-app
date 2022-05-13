from dotenv import dotenv_values
from flask import Flask, jsonify, request
from flask_log_request_id import RequestID
from psycopg2 import pool

import psycopg2

from endpoints.accountbalance import AccountBalance
from endpoints.placingorder import PlacingOrder
from helpers.emailnotification import EmailNotification

class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=400, func=None, notification=False):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.func = func
        self.notification = notification

    def to_dict(self):
        if self.notification==True:
            EmailNotification(self.message, self.func).send()
        return {
            'response': self.message,
            'code': self.status_code
        }

def create_app():
    app = Flask(__name__)
    RequestID(app)
    database_config = dotenv_values(".env")

    app.config['database_pool'] = psycopg2.pool.SimpleConnectionPool(
        5, 15,
        host = database_config['host'],
        database = database_config['database'],
        user = database_config['user'],
        password = database_config['password']
    )

    @app.route("/")
    def home():
        return jsonify({"response": "OK", "code": 200})
    
    @app.route("/<username>/Balance", methods=['GET'])
    def check_balance(username):
        response = AccountBalance(username, InvalidAPIUsage).get()
        return response

    @app.route("/<username>/PlacingOrder", methods=['POST'])
    def order(username):
        return PlacingOrder(request.json, username, InvalidAPIUsage).post()
    
    @app.errorhandler(InvalidAPIUsage)
    def invalid_api_usage(e):
        return jsonify(e.to_dict())
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)