from pymongo import MongoClient

class DAL:
    def __init__(self, collection):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["Processed_tweets"]
        self.collection = self.db[str(collection)]

    def consume_messages(self, msg):
        self.collection.insert_one(msg)
