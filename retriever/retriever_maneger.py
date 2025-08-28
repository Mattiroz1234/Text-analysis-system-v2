from dotenv import load_dotenv
from Receives_DAL.dal import DAL
from publisher import Publisher
import os
import time
from utils import Utils

load_dotenv()
database_url = os.getenv('IRANIAN_MONGO_URL', 'mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/')
db = os.getenv('IRANIAN_DB', 'IranMalDB')
collection = os.getenv('IRANIAN_COLLECTION', 'tweets')

def retrieve():
    con = DAL(database_url, db, collection)

    while True:
        antisemitic_data = []
        not_antisemitic_data = []
        tweets = con.get_next_100_oldest()
        for tweet in tweets:
            if tweet["Antisemitic"] == 1:
                antisemitic_data.append(tweet)
            else:
                not_antisemitic_data.append(tweet)

        antisemitic_data = Utils.correct_the_id(antisemitic_data)
        not_antisemitic_data =Utils.correct_the_id(not_antisemitic_data)

        pub = Publisher()
        pub.send_to_topics({"result": antisemitic_data}, {"result": not_antisemitic_data})

        time.sleep(60)

retrieve()