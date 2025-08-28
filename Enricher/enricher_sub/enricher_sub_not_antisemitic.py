from kafka import KafkaConsumer
from enricher_manager import Manager
import json

manager = Manager()

consumer = KafkaConsumer(
    'preprocessed_tweets_not_antisemitic',
    bootstrap_servers='text-analiysis-system-v2:9093',
    api_version=(0, 11, 5),
    group_id='my-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    request_timeout_ms=100000
)

print("preprocessed_tweets_not_antisemitic listening ...")

for message in consumer:
    print("an not antisemitic message was received:", message.value)
    manager.start_the_cleaning_process(message.value["result"])
