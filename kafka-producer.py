from dotenv import load_dotenv
import os

from kafka import KafkaProducer

load_dotenv()

ip_addr = os.getenv("IP_ADDR")
port = os.getenv("PORT")

bootstrap_servers = '10.11.13.81:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

topic = 'yy_test'
key = b'tweet'  # Optional: If you want to specify a key for the message
value = b'Hello, mom!'  # The actual message content

producer.send(topic, key=key, value=value)
producer.close()