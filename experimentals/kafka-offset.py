import kafka

admin_client = kafka.KafkaAdminClient(bootstrap_servers=['localhost:9092'])

topic_list = admin_client.list_topics()

for topic in topic_list:
    print(topic)