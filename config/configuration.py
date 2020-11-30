
import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv("URL")

#Conectando con la base de mongo en local
if not (DBURL):
    raise ValueError ("Tienes que especificar la URL") 


client = MongoClient(DBURL)
db = client.get_database()
collection = db["frases"]