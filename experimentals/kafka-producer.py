from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='10.11.13.81:9092',
    value_serializer=lambda v: str(v).encode('utf-8')
)

topic_name = 'jsontest'

import json

jsonMessage = {
    "source": "twitter",
    "url": "https://x.com/4",
    "title": "Hello, four",
    "sentiment": True
}

header_name = [("source", b"twitter")]

try:
    message_value = json.dumps(jsonMessage)
    producer.send(topic_name, value=message_value, headers=header_name)
    print(f"Produced message: {message_value}")

except Exception as e:
    print(f"Error producing message: {e}")

finally:
    producer.flush()
    producer.close()