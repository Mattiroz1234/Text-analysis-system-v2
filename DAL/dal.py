from pymongo import MongoClient

class DAL:
    def __init__(self, connection_string, db, collection):
        self.connection_string = connection_string
        self.db = db
        self.collection =collection


    def get_all(self):
        client = MongoClient(self.connection_string)
        db = client[str(self.db)]
        collection = db[str(self.collection)]
        cursor = collection.find()
        data = {"result": list(cursor)}
        return data

