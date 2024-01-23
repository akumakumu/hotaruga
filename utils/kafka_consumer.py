from kafka import KafkaConsumer

class KafkaConsumerWrapper:
    def __init__(self, bootstrap_servers, group_id, auto_offset_reset):
        self.consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            auto_offset_reset=auto_offset_reset
        )

    def subscribe(self, topics):
        self.consumer.subscribe(topics)

    def get_message(self):
        return next(self.consumer)