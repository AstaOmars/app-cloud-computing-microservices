from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient("mongodb://host.docker.internal:27017/")
db = client["vessel_data"]  # Name of your database
collection = db["vessels"]  # Name of the collection where JSON data will be stored

@app.route('/')
@app.route('/ingest', methods=['POST'])
def ingest_json():
    """
    Endpoint to ingest vessel movement data.
    Expects JSON data with vessel movement records.
    """
    data = None

    # Check if 'file' is part of the request (file upload scenario)
    if 'file' in request.files:
        file = request.files['file']
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid JSON format in file"}), 400
    
    # Check if the request has JSON content (direct JSON payload scenario)
    elif request.is_json:
        try:
            data = request.get_json()
        except Exception as e:
            return jsonify({"error": f"Failed to parse JSON: {str(e)}"}), 400
    else:
        return jsonify({"error": "No JSON payload or file provided"}), 400

    # Insert JSON data into MongoDB
    try:
        if isinstance(data, list):  # If data is a list of records
            collection.insert_many(data)
        else:  # If data is a single record
            collection.insert_one(data)
        
        return jsonify({"message": "Data ingested successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/vessels', methods=['GET'])
def get_vessels():
    """
    Endpoint to retrieve all vessel movement records.
    """
    try:
        vessels = list(collection.find({}))
        for vessel in vessels:
            vessel['_id'] = str(vessel['_id'])  # Convert ObjectId to string for JSON serialization

        return jsonify(vessels), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

