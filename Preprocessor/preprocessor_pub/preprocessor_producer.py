import json
from kafka import KafkaProducer


class Producer:
    def __init__(self):
        self.producer = self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                    value_serializer=lambda x:
                                    json.dumps(x).encode('utf-8')
                                    )


    def conn(self):
        pass

    def send_message(self, topic, message):
        self.producer.send(topic, message)
        print("sent:",message, "to", topic)

    def close_conn(self):
        self.producer.close()

