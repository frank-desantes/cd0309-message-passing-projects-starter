from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['udaconnect-kafka-broker.default.svc.cluster.local:9094'], value_serializer=lambda v: json.dumps(v).encode('utf-8'), acks='all', retries=15)
producer.send('location', {"person_id": 6, "latitude": "-122.290883", "longitude": "37.55363", "creation_time": "2025-03-27T20:37:06"})

producer.flush()
producer.close()
