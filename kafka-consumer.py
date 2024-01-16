#from dotenv import load_dotenv
#import os

from kafka import KafkaConsumer

#load_dotenv()

#ip_addr = os.getenv("IP_ADDR")
#port = os.getenv("PORT")

from kafka import KafkaConsumer

# Replace 'your_kafka_bootstrap_servers' with the actual address of your Kafka broker
bootstrap_servers = '10.11.13.81'

# Create a KafkaConsumer instance
consumer = KafkaConsumer('yy_test', group_id='yy_group', bootstrap_servers=bootstrap_servers)

# Consume messages from the 'test_topic' topic
for message in consumer:
    print(f"Received message: {message.value}")

# Close the consumer to release resources
consumer.close()