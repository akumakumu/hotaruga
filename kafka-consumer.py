from kafka import KafkaConsumer

#consumer = KafkaConsumer(bootstrap_servers='10.11.13.81:9092')

#consumer.subscribe(['yytest'])

#FORMAT
#consumer = KafkaConsumer(
#    subs_topic,
#    bootstrap_servers='ip-address:port',
#    auto_offset_reset='earliest' # consume from beginning topic
#)

consumer = KafkaConsumer(
    'yytest',
    bootstrap_servers='10.11.13.81:9092',
    auto_offset_reset='earliest'
)

for msg in consumer:
    print(msg)