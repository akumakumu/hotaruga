from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

class MongoDBConnector:
    def __init__(self):
        myURI = os.getenv('URI')
        myPORT = os.getenv('PORT')
        myDB = os.getenv('DB')
        self.client = MongoClient(myURI, int(myPORT))
        self.db = self.client[myDB]

    def insert_data(self, data, collection_name):
        collection = self.db[collection_name]
        collection.insert_one(data)