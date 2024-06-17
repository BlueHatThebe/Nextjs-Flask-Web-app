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
        # Set limit=1 and offset=2 to fetch the third device
        response = requests.get('https://api.waziup.io/api/v2/devices?q=owner==thebzennkhasi@gmail.com&limit=1&offset=2')
        data = response.json()  # Extract JSON data from the response
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5002)  # Second Flask app on port 5002
