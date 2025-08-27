import json
from kafka import KafkaProducer


class Producer:
    def __init__(self):
        self.producer = None


    def conn(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                    value_serializer=lambda x:
                                    json.dumps(x).encode('utf-8')
                                    )

    def send_message(self, topic, message):
        if not self.producer:
            self.conn()
        self.producer.send(topic, message)
        print("נשלח:",message, "to", topic)
        self.close_conn()

    def close_conn(self):
        self.producer.close()