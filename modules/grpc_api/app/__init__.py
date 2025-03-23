from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

globalServer = None
globalApp = None

def start_grpc_server():
    import grpc
    from concurrent import futures
    import time
    import atexit
    from datetime import datetime
    import os
    from typing import Optional   

    # Import the generated classes
    import connections_pb2
    import connections_pb2_grpc
    import sys

    DATE_FORMAT = "%Y-%m-%d"
    
    global globalServer
    global globalApp
    
    print("prepare gRPC server with class ConnectionsServicer")

    class ConnectionServicer(connections_pb2_grpc.ConnectionServiceServicer):
        def GetConnections(self, request, context):
            with globalApp.app_context():
                person_id: int = request.person_id
                start_date: datetime = datetime.strptime(request.start_date, DATE_FORMAT)
                end_date: datetime = datetime.strptime(request.end_date, DATE_FORMAT)
                distance: Optional[int] = request.distance

                from app.udaconnect.services import ConnectionService

                results = ConnectionService.find_contacts(
                    person_id=person_id,
                    start_date=start_date,
                    end_date=end_date,
                    meters=distance
                )
            return results
        
    print("Create a gRPC server")
    globalServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    print("Specify the port to listen on")
    globalServer.add_insecure_port('[::]:5003')

    print("Add the defined service to the server")
    connections_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), globalServer)

    print("Start the server")
    globalServer.start()

    print("Server is running on port 5003...")

    def interrupt():
        globalServer.stop(0)
        print("Server stopped")

    atexit.register(interrupt)
    return

def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)
    
    @app.route("/health")
    def health():
        return jsonify("healthy")
    global globalApp 
    globalApp = app
    start_grpc_server()

    return app

