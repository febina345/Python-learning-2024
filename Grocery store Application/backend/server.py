from flask import Flask, jsonify, request

from sql_connection import get_sql_connection

import products_dao
import mysql.connector
import _json


app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Mnagement System")
    app.run(port=5000)
