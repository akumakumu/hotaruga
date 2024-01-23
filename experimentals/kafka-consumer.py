from dotenv import load_dotenv
from pymongo import MongoClient
from kafka import KafkaConsumer

import os
import json

load_dotenv()

myURI = os.getenv('URI')
myPORT = os.getenv('PORT')
myDB = os.getenv('DB')

client = MongoClient(myURI, int(myPORT))

db = client[myDB]

consumer = KafkaConsumer(
    bootstrap_servers='10.11.13.81:9092',
    group_id='yy',
    auto_offset_reset='earliest'
)

consumer.subscribe(['jsontest'])

message = next(consumer)

pointer = json.loads(message.value.decode('utf-8'))

db.yytestdb.insert_one(pointer)

consumer.close()