from flask_cors import cross_origin 
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

globalServer = None

def start_grpc_server(app):
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
  
    #print("prepare gRPC server with class ConnectionsServicer")
    class ConnectionServicer(connections_pb2_grpc.ConnectionServiceServicer):
        @cross_origin()
        def GetConnections(self, request, context):
            
            # hint from mayur ->CORS(app, origins=['http://localhost:3000'])

            #context.set_trailing_metadata((('Access-Control-Allow-Origin', '*'),))
            #context.set_trailing_metadata((('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'),))
            #context.set_trailing_metadata((('Access-Control-Allow-Headers', 'Content-Type, Authorization'),))

            # Set CORS headers
            #CORS(app) //not working
            #context.set_trailing_metadata((('Access-Control-Allow-Origin', '*'),)) //not working

            person_id: int = request.person_id
            start_date: datetime = datetime.strptime(request.start_date, DATE_FORMAT)
            end_date: datetime = datetime.strptime(request.end_date, DATE_FORMAT)
            distance: Optional[int] = request.distance

            # print("request:")
            # print(" person_id:", person_id)
            # print(" start_date:", start_date)
            # print(" end_date:", end_date)
            # print(" distance:", distance)
            
            from app.udaconnect.services import ConnectionService         
            with app.app_context():
                db_connections = ConnectionService.find_contacts(
                    person_id=person_id,
                    start_date=start_date,
                    end_date=end_date,
                    meters=distance
                )

            connectionResponse = connections_pb2.ConnectionResponse()

            for db_connection in db_connections:
                # print("person: ")
                # print(" person_id]: ", db_connection.person.id)
                # print(" first_name: ", db_connection.person.first_name)
                # print(" last_name: ", db_connection.person.last_name)
                # print(" company_name: ", db_connection.person.company_name)

                # print("location: ")
                # print(" id: ", db_connection.location.id)
                # print(" person_id: ", db_connection.location.person_id)
                # print(" longitude: ", db_connection.location.longitude)
                # print(" latitude: ", db_connection.location.latitude)
                # print(" creation_time: ", db_connection.location.creation_time.isoformat())
             
                location = connections_pb2.Location(
                    id = db_connection.location.id,
                    person_id = db_connection.location.person_id,
                    longitude = db_connection.location.longitude,
                    latitude = db_connection.location.latitude,
                    creation_time = db_connection.location.creation_time.isoformat()
                )

                person = connections_pb2.Person(
                    id = db_connection.person.id,
                    first_name = db_connection.person.first_name,
                    last_name = db_connection.person.last_name,
                    company_name = db_connection.person.company_name
                )

                connection = connections_pb2.Connection(
                    person = person,
                    location = location    
                )

                connectionResponse.connections.append(connection)

            return connectionResponse 
                
    #print("Create a gRPC server")
    globalServer = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    #print("Specify the port to listen on")
    globalServer.add_insecure_port('[::]:5003')

    #print("Add the defined service to the server")
    connections_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), globalServer)

    #print("Start the server")
    globalServer.start()

    print("grpc Server is running on port 5003...")

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
    #CORS(app, resources={r"/*": {"origins": "*"}})

    register_routes(api, app)
    db.init_app(app)
        
    @app.route("/health")
    def health():
        return jsonify("healthy")
    
    start_grpc_server(app)
    
    return app

