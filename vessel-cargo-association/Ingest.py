from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://host.docker.internal:27017/")
db = client["vessel_data"]
cargo_collection = db["cargo"]

# Define some test data for the cargo collection
test_data = [
    {"cargo_id": "C001", "description": "Tuna", "vessel_id": "V123", "weight": 2000},
    {"cargo_id": "C002", "description": "Cod", "vessel_id": "V124", "weight": 1500},
    {"cargo_id": "C003", "description": "Food Supplies", "vessel_id": "V125", "weight": 2500},
    {"cargo_id": "C004", "description": "Cod", "vessel_id": "V123", "weight": 3000},
    {"cargo_id": "C005", "description": "Textiles", "vessel_id": "V126", "weight": 1000}
]

# Insert test data into cargo collection
cargo_collection.insert_many(test_data)

print("Test data loaded into the cargo collection.")