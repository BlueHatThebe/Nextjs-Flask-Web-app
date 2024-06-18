from flask import Flask, jsonify
from flask_cors import CORS
import requests
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootSQL8'
app.config['MYSQL_DB'] = 'demo'

mysql = MySQL(app)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_all_data():
    try:
        # Make a GET request to Wazicloud API endpoint
        url = 'https://api.waziup.io/api/v2/devices'
        params = {
            'q': 'owner==thebzennkhasi@gmail.com',
            'limit': 1
        }
        response = requests.get(url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Ensure data is a list and has at least one device
            if isinstance(data, list) and len(data) > 0:
                device = data[0]  # Assuming we want the first device in the list

                # Extract relevant fields from the device data
                name = device.get('name', '')
                id = device.get('id', '')
                actuators = ','.join(device.get('actuators', []))  # Convert list to comma-separated string
                sensors = ','.join(device.get('sensors', []))  # Convert list to comma-separated string
                gateway_id = device.get('gateway_id', '')
                domain = device.get('domain', '')
                owner = device.get('owner', '')
                visibility = device.get('visibility', '')

                # Connect to MySQL
                cur = mysql.connection.cursor()

                # Insert data into `devices_data2` table
                cur.execute("INSERT INTO devices_data2 (name, id, actuators, sensors, gateway_id, domain, owner, visibility) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (name, id, actuators, sensors, gateway_id, domain, owner, visibility))

                mysql.connection.commit()  # Commit changes
                cur.close()  # Close cursor

                return jsonify(device)  # Return the device data as JSON
            else:
                return jsonify({'error': 'No device found or invalid API response'})
        else:
            return jsonify({'error': 'Failed to fetch data from Wazicloud API'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
