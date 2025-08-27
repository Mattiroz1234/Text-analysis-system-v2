from kafka import KafkaConsumer
from cleaning_data.manager import Manager
import json

manager = Manager()

consumer = KafkaConsumer(
    'raw_tweets_not_antisemitic',
    bootstrap_servers='broker:9092',
    api_version=(0, 11, 5),
    group_id='my-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    request_timeout_ms=100000
)

print("raw_tweets_antisemitic מקשיב להודעות...")

for message in consumer:
    manager.start_the_cleaning_process(message["result"])
    print("התקבלה הודעה:", message.value)