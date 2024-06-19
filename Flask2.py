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
            'limit': 1,
            'offset': 1
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
                device_id = device.get('id', '')
                actuators = ','.join(str(actuator) for actuator in device.get('actuators', []))
                sensors = ','.join(str(sensor) for sensor in device.get('sensors', []))
                gateway_id = device.get('gateway_id', '')
                domain = device.get('domain', '')
                visibility = device.get('visibility', '')

                # Connect to MySQL
                cur = mysql.connection.cursor()

                # Insert data into `devices_data2` table
                sql = "INSERT INTO devices_data2 (name, id, actuators, sensors, gateway_id, domain, visibility) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (name, device_id, actuators, sensors, gateway_id, domain, visibility)

                cur.execute(sql, values)
                mysql.connection.commit()  # Commit changes
                cur.close()  # Close cursor

                return jsonify(device)  # Return the device data as JSON
            else:
                return jsonify({'error': 'No device found or invalid API response'})
        else:
            return jsonify({'error': 'Failed to fetch data from Wazicloud API'})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request Exception: {str(e)}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)