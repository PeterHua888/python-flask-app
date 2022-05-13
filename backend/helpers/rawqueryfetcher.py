from flask import current_app
from settings import DB

class RawQueryFetcher:
    def __init__(self, query):
        self.query = query
    
    def fetch(self):
        connection = DB().get_connection()
        cursor = connection.cursor()    # Connection with Database
        cursor.execute(self.query)
        result = cursor.fetchall()
        # put connection back to pool
        current_app.config["database_pool"].putconn(connection)
        return result