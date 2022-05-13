from flask import current_app

class DB:
    def get_connection(self):
        return current_app.config["database_pool"].getconn()