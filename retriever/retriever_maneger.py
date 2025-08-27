from pprint import pprint
from dotenv import load_dotenv
from DAL.dal import DAL
import os

load_dotenv()
database_url = os.getenv('IRANIAN_MONGO_URL', 'mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/')
db = os.getenv('IRANIAN_DB', 'IranMalDB')
collection = os.getenv('IRANIAN_COLLECTION', 'tweets')

d = DAL(database_url, db, collection)
a = d.get_next_100_oldest()
b = d.get_next_100_oldest()

pprint(a)
print("\n\n\n\n---------------------\n\n\n\n")
pprint(b)

