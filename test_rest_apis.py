import requests

# Definiera bas-URL:er för dina mikroservicer
base_url_ingestion = "http://localhost:5001"
base_url_cargo_association = "http://localhost:5003"
base_url_anomaly_detection = "http://localhost:5002"

# Testa Vessel-Ingestion API
def test_vessel_ingestion():
    url = f"{base_url_ingestion}/ingest"
    payload = {
        "vessel_id": "V123",
        "movement": "Arrival",
        "timestamp": "2024-11-01T12:00:00Z",
        "port": "PortB"
    }
    response = requests.post(url, json=payload)
    print("Vessel Ingestion Response:", response.json())

# Testa Vessel-Cargo-Association API
def test_vessel_cargo_association():
    url = f"{base_url_cargo_association}/associate-cargo?vessel_id=V123"
    response = requests.get(url)
    print("Vessel Cargo Association Response:", response.json())

# Testa Anomaly Detection API
def test_anomaly_detection():
    url = f"{base_url_anomaly_detection}/detect"
    payload = {
        "vessel_data": [[0.1, 0.2, 17], [0.3, 0.4, 10]]  # Exempeldata
    }
    response = requests.post(url, json=payload)
    print("Anomaly Detection Response:", response.json())

# Anropa funktionerna
if __name__ == "__main__":
    test_vessel_ingestion()
    test_vessel_cargo_association()
    test_anomaly_detection()
