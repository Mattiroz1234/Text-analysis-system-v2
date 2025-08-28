import os
from dotenv import load_dotenv
from .dal.dal import DAL
from data_retrieval.utils import Utils


class Manager_retrieval:
    def __init__(self):
        load_dotenv()
        database_url = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
        db = os.getenv('IRANIAN_DB', 'Processed_tweets')
        self.collection_antisemitic = os.getenv('COLLECTION_ANTISEMITIC', 'tweets_antisemitic')
        self.collection_not_antisemitic = os.getenv('COLLECTION_NOT_ANTISEMITIC', 'tweets_not_antisemitic')
        self.dal = DAL(database_url,db)

    def get_all_data(self, collection):
        if collection == "antisemitic":
            collection = self.collection_antisemitic
        else:
            collection = self.collection_not_antisemitic
        result = self.dal.get_all(collection)
        result = Utils.correct_the_id(result)
        return result