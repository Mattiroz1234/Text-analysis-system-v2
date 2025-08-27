from dotenv import load_dotenv
from DAL.dal import DAL
import os

load_dotenv()
database_url = os.getenv('IRANIAN_MONGO_URL', 'mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/')
db = os.getenv('IRANIAN_DB', 'IranMalDB')
collection = os.getenv('IRANIAN_COLLECTION', 'tweets')
d = DAL(database_url, db, collection)
a = d.get_all()
print(str(a["result"][0]['CreateDate']))

