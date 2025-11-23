from pymongo import MongoClient

def get_database():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        # Connect to the database named 'Airbnb' (contains the full dataset)
        db = client["Airbnb"]
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None