import pymongo

# Create a client instance of the MongoClient class
client = pymongo.MongoClient(host="mongodb://localhost:27017/")

# Create a database instance of the Database class
db = client["test"]

# Create a collection instance of the Collection class
collection = db["test"]

# Create a document
document = {"name": "test", "age": 18}

# Insert a document
collection.insert_one(document)

# Query a document
result = collection.find_one({"name": "test"})

# Print the result
print(result)
