from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='10.11.13.81:9092',
    value_serializer=lambda v: str(v).encode('utf-8')  # Assuming the message is a string
)

topic_name = 'yytest'

try:
    message_value = "Hello, Mom!"
    producer.send(topic_name, value=message_value)
    print(f"Produced message: {message_value}")

except Exception as e:
    print(f"Error producing message: {e}")

finally:
    producer.flush()
    producer.close()