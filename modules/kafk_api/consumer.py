import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='udaconnect-kafka-broker.default.svc.cluster.local:9092',auto_offset_reset='latest')
consumer.subscribe(['location'])

for message in consumer:
    try:
        value=json.loads(message.value.decode('utf-8'))
        print(value)
    except Exception as e:
        print("error reading jason: ", e)
        continue

