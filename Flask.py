from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootSQL8'
app.config['MYSQL_DB'] = 'Example1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_all_data():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM example_table")
        data = cursor.fetchall()
        cursor.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
