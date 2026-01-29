from pymongo import MongoClient

db = None

def init_db():
    global db
    mongo_uri = "mongodb://localhost:27017"
    client = MongoClient(mongo_uri)
    db = client["video_app"]
    print("MongoDB connected:", db.name)
    return db
