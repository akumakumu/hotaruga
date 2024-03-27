import kafka

admin_client = kafka.KafkaAdminClient(bootstrap_servers=['10.11.13.81:9092'])

topic_list = admin_client.list_topics()

for topic in topic_list:
    print(topic)