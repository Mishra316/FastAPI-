import pymongo

# Connect to local MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydb"]  # Your database name
collection = db["usersinput"]  # Your collection name

# Ensure phone number is unique
collection.create_index("phone", unique=True)
