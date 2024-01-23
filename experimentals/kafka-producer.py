from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='10.11.13.81:9092',
    value_serializer=lambda v: str(v).encode('utf-8')
)

topic_name = 'jsontest'

import json

jsonMessage = {
    "url": "https://x.com/3",
    "title": "Hello, three",
    "sentiment": True
}

try:
    message_value = json.dumps(jsonMessage)
    producer.send(topic_name, value=message_value)
    print(f"Produced message: {message_value}")

except Exception as e:
    print(f"Error producing message: {e}")

finally:
    producer.flush()
    producer.close()