from dotenv import load_dotenv

from databases.pymongo_poll import MongoDBConnector
from utils.kafka_consumer import KafkaConsumerWrapper

import os
import json

load_dotenv()

bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
group_id = os.getenv('KAFKA_GROUP_ID')
auto_offset_reset = os.getenv('KAFKA_AUTO_OFFSET_RESET')

kafka_consumer = KafkaConsumerWrapper(bootstrap_servers, group_id, auto_offset_reset)
kafka_consumer.subscribe(['jsontest'])

mongo_connector = MongoDBConnector()

message = kafka_consumer.get_message()
pointer = json.loads(message.value.decode('utf-8'))

mongo_connector.insert_data(pointer, 'yytestdb')

kafka_consumer.consumer.close()