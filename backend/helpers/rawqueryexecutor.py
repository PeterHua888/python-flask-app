from flask import current_app
from settings import DB
import logging.config

class RawQueryExecutor:
    def __init__(self, query):
        self.query = query

    def execute(self):
        connection = DB().get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(self.query)
            connection.commit()
            current_app.config["database_pool"].putconn(connection)
        except Exception as e:
            self.logger.error("Database connection issue: "+str(e), exc_info=True)
            connection.rollback()
        return