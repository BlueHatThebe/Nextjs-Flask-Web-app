from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_all_data():
    try:
        # Make a GET request to Wazicloud API endpoint
        # Modify the URL to include limit=1 to fetch only one device
        response = requests.get('https://api.waziup.io/api/v2/devices?q=owner==thebzennkhasi@gmail.com&limit=1')
        data = response.json()  # Extract JSON data from the response
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

