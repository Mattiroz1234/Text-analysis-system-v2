from kafka import KafkaProducer
import json
import time

class Publisher:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_to_topics(self, antisemitic_data, not_antisemitic_data):
        while True:
            self.producer.send('antisemitic', antisemitic_data)
            print("Sent to antisemitic")

            self.producer.send('not_antisemitic', not_antisemitic_data)
            print("Sent to not_antisemitic")

            self.producer.flush()

            time.sleep(60)

