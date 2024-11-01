from flask import Flask, request, jsonify
from sklearn.ensemble import IsolationForest
import numpy as np

app = Flask(__name__)

# Initialize a simple Isolation Forest model for anomaly detection
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)

# Health check endpoint to confirm service is running
@app.route('/')
@app.route('/status', methods=['GET'])
def status():
    """Endpoint to check the status of the anomaly detection service."""
    return jsonify({"status": "Service is up and running"}), 200 # 200 Ok Indicates that everything went well

# Endpoint to train the model with new data
@app.route('/train', methods=['POST'])
def train():
    """Train the Isolation Forest model with provided vessel movement data."""
    data = request.json.get('vessel_data', [])
    if not data:
        return jsonify({"error": "No data provided"}), 400 # 400 Bad Request if data missing
    
    try:
    
        # Convert the data to a numpy array
        data_array = np.array(data)
        model.fit(data_array)
        return jsonify({"message": "Model trained successfully"}), 200 # 200 Ok 
    except ValueError as e:
        return jsonify({"error": f"Invalid data format: {e}"}), 400 # 400 Bad Request if invalid data
    except Exception as e:
        app.logger.error("An unexpected error occurred during training: %s", str(e))
        return jsonify({"error": "An unexpected error occurred"}), 500 # 500 Internal Server Error if any other error occurs
    
# Endpoint to detect anomalies
@app.route('/detect', methods=['POST'])
def detect():
    """Detect anomalies in the provided vessel movement data."""
    data = request.json.get('vessel_data', [])
    if not data:
        return jsonify({"error": "No data provided"}), 400 # 400 Bad Request if data missing
    
    try:
        # Convert the data to a numpy array
        data_array = np.array(data)
        predictions = model.predict(data_array)
    
        # Anomalies are marked as -1 by Isolation Forest
        anomalies = [i for i, pred in enumerate(predictions) if pred == -1]
        return jsonify({"anomalies": anomalies}), 200 # 200 OK Indicates that everything went well
    except ValueError as e:
        return jsonify({"error": f"Invalid data format: {e}"}), 400 # 400 Bad Request if invalid data format
    except Exception as e:
        app.logger.error("An unexpected error occurred during detection: %s", str(e))
        return jsonify({"error": "An unexpected error occurred"}), 500 # 500 Internal Server Error if any other error occurs.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
