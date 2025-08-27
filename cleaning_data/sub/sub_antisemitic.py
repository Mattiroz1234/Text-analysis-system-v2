from kafka import KafkaConsumer
import json


consumer = KafkaConsumer(
    'raw_tweets_antisemitic',
    bootstrap_servers='broker:9092',
    api_version=(0, 11, 5),
    group_id='my-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    request_timeout_ms=100000
)

print("raw_tweets_antisemitic מקשיב להודעות...")

for message in consumer:
    print("התקבלה הודעה:", message.value)