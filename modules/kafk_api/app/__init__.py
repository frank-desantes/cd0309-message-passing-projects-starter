from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from threading import Thread

db = SQLAlchemy()

DATE_FORMAT = "%Y-%m-%d"

def kafka_consumer(app):
    import json
    from kafka import KafkaConsumer
    from datetime import datetime

    consumer = KafkaConsumer(bootstrap_servers='udaconnect-kafka-broker.default.svc.cluster.local:9092',auto_offset_reset='latest')
    consumer.subscribe(['location'])

    for message in consumer:
        try:
            location=json.loads(message.value.decode('utf-8'))
            print("rceived location: ", location)
            
            person_id: int = location["person_id"]
            latitude:  str = location["latitude"]
            longitude:  str = location["longitude"]
            creation_time: datetime = datetime.strptime(location["creation_time"], DATE_FORMAT)

            from app.udaconnect.services import LocationService         
            with app.app_context():
                LocationService.create(
                    person_id=person_id,
                    latitude=latitude,
                    longitude=longitude,
                    creation_time=creation_time
                )
        except Exception as e:
            print("error writing location: ", e)
            continue
    return

def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes


    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development
    #CORS(app, resources={r"/*": {"origins": "*"}})

    register_routes(api, app)
    db.init_app(app)
        
    @app.route("/health")
    def health():
        return jsonify("healthy")
    
    #Start a kafka consumer
    thread = Thread(target = kafka_consumer, args = (app, ))
    #thread.start()
    print("kafka consumer started")

    return app
