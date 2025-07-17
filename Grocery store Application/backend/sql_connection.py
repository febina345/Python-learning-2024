import mysql.connector
from mysql import connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='ottan@123',
                                        host='127.0.0.1',
                                        database='grocery_store')
        return __cnx
