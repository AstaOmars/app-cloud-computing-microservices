from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB connection setup
# client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb://host.docker.internal:27017/")
db = client["vessel_data"]
vessels_collection = db["vessels"]
cargo_collection = db["cargo"]

# Funktion för att konvertera ObjectId till sträng
def serialize_mongo_document(doc):
    """Convert a MongoDB document to a JSON-serializable format."""
    doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
    return doc

@app.route('/')

@app.route('/associate-cargo', methods=['GET'])
def associate_cargo():
    """
    Endpoint to retrieve probable cargo based on vessel_id.
    
    Query Parameters:
    - vessel_id: ID of the vessel to retrieve cargo predictions for.
    
    Returns:
    - JSON list of probable cargo records associated with the vessel's visited ports.
    """
    try:
        vessel_id = request.args.get("vessel_id")
        
         # Check if 'vessel_id' has been entered
        if not vessel_id:
            return jsonify({"error": "Missing vessel_id parameter"}), 400  # 400 Bad Request if 'vessel_id' missing
        
        # get vessel from database
        vessel = vessels_collection.find_one({"vessel_id": vessel_id})
        
        # Check if vessel or port information is included in the data
        if not vessel or "ports_visited" not in vessel:
            return jsonify({"error": "Vessel or required data not found"}), 404 # 404 Not Found if data missing

        # Query for probable cargo based on ports visited by the vessel
        probable_cargo = cargo_collection.find({"port": {"$in": vessel["ports_visited"]}})
        probable_cargo_list = list(probable_cargo)
        probable_cargo_list = [serialize_mongo_document(cargo) for cargo in probable_cargo_list]  # Use the serialization function
        
        return jsonify(probable_cargo_list), 200 # 200 OK Indicates that everything went well
    
    except Exception as e:
        app.logger.error("Error occurred: %s", str(e))
        return jsonify({"error": str(e)}), 500 # 500 Internal Server Error if any other error occurs

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
