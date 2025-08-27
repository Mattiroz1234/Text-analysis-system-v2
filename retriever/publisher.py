from kafka import KafkaProducer
import json

class Publisher:

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_to_topics(self, antisemitic_data, not_antisemitic_data):
            self.producer.send('raw_tweets_antisemitic', antisemitic_data)

            self.producer.send('raw_tweets_not_antisemitic', not_antisemitic_data)

            self.producer.flush()

