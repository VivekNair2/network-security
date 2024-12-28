from pymongo import MongoClient

# MongoDB connection URL
MONGO_DB_URL = "mongodb+srv://vivekh2004:vivek2004@cluster0.deort.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def get_collection_data(database_name, collection_name):
    try:
        # Connect to MongoDB
        client = MongoClient(MONGO_DB_URL)
        
        # Access the database and collection
        db = client[database_name]
        collection = db[collection_name]
        
        # Retrieve all documents from the collection
        documents = collection.find()
        
        print(f"Data from collection '{collection_name}':")
        for document in documents:
            print(document)
        
        # Close the connection
        client.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'Cluster0' with your database name
    database_name = "Cluster0"
    # Replace 'NetworkData' with your collection name
    collection_name = "NetworkData"
    get_collection_data(database_name, collection_name)
