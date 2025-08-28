from kafka import KafkaConsumer
import json
from Persister.persister_DAL.save_DAL import DAL

dal = DAL("tweets_not_antisemitic")

consumer = KafkaConsumer(
    'enriched_preprocessed_tweets_not_antisemitic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='sub_group_1',
    auto_offset_reset = 'earliest'
)

for message in consumer:
    print(message.value)
    for i in message.value['result']:
        dal.consume_messages(i)