import os
from pymongo import MongoClient

mongo_client = None
db = None

def init_db():
    global mongo_client, db
    mongo_uri = os.environ.get("MONGO_URI")
    mongo_client = MongoClient(mongo_uri)
    db = mongo_client["video_app"]
    print("MongoDB connected:", db.name)
