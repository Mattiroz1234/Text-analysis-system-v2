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
#
# a = Producer()
# data = {"result":[{
#   '_id': '68ae981e5e29e58934bb2617',
#   'TweetID': 1220000000000000000,
#   'CreateDate': '2020-02-02T20:50:15.000Z',
#   'Antisemitic': 0,
#   'text': 'uzi @FrankPercival @YorkshireLady3 gun Leave 2021-05-03 grenade 2022-02-19 gun ak47 my timeline 2022-06-28 you’re a Marxist 2021-12-27 and anti Israel'
# }]}
# a.send_message("raw_tweets_antisemitic", data)
