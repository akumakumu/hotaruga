from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers='10.11.13.81:9092',
    group_id='yy',
    auto_offset_reset='earliest'
)

consumer.subscribe(['jsontest'])

message = next(consumer)
print(message.value.decode('utf-8'))

consumer.close()