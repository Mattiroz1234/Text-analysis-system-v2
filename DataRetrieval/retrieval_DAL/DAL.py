from pymongo import MongoClient

class DAL:
    def __init__(self, connection_string, db):
        self.connection_string = connection_string
        self.db = db
        self.last_fetched_date = None



    def get_all(self, collection):
        client = MongoClient(self.connection_string)
        db = client[str(self.db)]
        collection = db[str(collection)]
        cursor = collection.find({})
        data = list(cursor)
        return data