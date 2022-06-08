from flask import Flask, jsonify, request
from flask_cors import CORS
from flask.wrappers import Request
from flaskext.mysql import MySQL
from pymysql import cursors
from pymysql.err import ProgrammingError
from pymysql.cursors import DictCursor
from werkzeug.wrappers import response

app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'granja'

mysql = MySQL()
mysql.init_app(app)

cursor = mysql.connect().cursor(cursor=DictCursor)

@app.route('/')
def index():
        return "<h2>Esto es una API<h2>\
        <p><a href='/products'>Esto es para Productos</a></p>\
        <p><a href='/orders'>Esto es para Ordenes</a></p>"


@app.route('/products')
def products():
    sql = "SELECT * FROM products WHERE is_deleted = 0"
    try:
        cursor.execute(sql)
        response = cursor.fetchall()
    except ProgrammingError as e:
        code, msg = e.args
        response = (code, msg)

    return jsonify(response)


@app.route('/products/<string:id>')
def getProductoById(id):
    response = {'error': False, 'data': None}
    sql = f'SELECT * FROM products WHERE is_deleted = 0 AND id = {id};'

    try:
        cursor.execute(sql)
        response['data'] = cursor.fetchall()

    except:
        response['error'] = True
    
    return jsonify(response)

@app.route('/orders', methods=['GET'])
def getOrders():
    response = {'error': False, 'data': None}
    sql = "SELECT * FROM orders"
    try:
        cursor.execute(sql)
        response['data'] = cursor.fetchall()
    except:
        response['error'] = True

    return jsonify(response)

def insertInOrders(sql):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

    return cursor.lastrowid

@app.route('/orders', methods=['POST'])
def createOrders():
    res = request.json
    
    try:
        sql = f'INSERT INTO orders(total, customer_id) values ({res["total"]},1)'
        orderId = insertInOrders(sql)

        for prod in res['products']:
            sql = f'INSERT INTO order_details(order_id, product_id, quantity) values ({orderId}, {prod["id"]}, {prod["quantity"]}) '
            print(insertInOrders(sql))


        return {"error": False, "data": res}
    except:
        return {"error": True, "data": None}

@app.route('/orders/<string:id>')
def getOrderById(id):
    response = {'error': False, 'data': None}
    sql = f'SELECT * FROM order_details WHERE order_id = {id};'

    try:
        cursor.execute(sql)
        response['data'] = cursor.fetchall()

    except:
        response['error'] = True
    
    return jsonify(response["data"])



""" --------------------- """


if __name__ == '__main__':
    app.run(debug=True)