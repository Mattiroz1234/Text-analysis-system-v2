from pymongo import MongoClient

class DAL:
    def __init__(self, connection_string, db, collection):
        self.connection_string = connection_string
        self.db = db
        self.collection = collection
        self.last_fetched_date = None



    def get_all(self):
        client = MongoClient(self.connection_string)
        db = client[str(self.db)]
        collection = db[str(self.collection)]
        cursor = collection.find()
        data = {"result": list(cursor)}
        return data



    def get_next_100_oldest(self):
        client = MongoClient(self.connection_string)
        db = client[str(self.db)]
        collection = db[str(self.collection)]

        query = {}
        if self.last_fetched_date:
            query["CreateDate"] = {'$gt': self.last_fetched_date}

        results = list(
            collection.find(query)
            .sort("CreateDate", 1)
            .limit(100)
        )

        if results:
            self.last_fetched_date = results[-1]["CreateDate"]

        return results

