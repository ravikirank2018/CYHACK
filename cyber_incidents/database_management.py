from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['cyber_incidents_db']
collection = db['incidents']

# Load data from JSON file
with open('incidents.json') as f:
    data = json.load(f)

# Insert data into MongoDB
collection.insert_many(data)
