from app import create_app

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

from app.udaconnect.services import ConnectionService

DATE_FORMAT = "%Y-%m-%d"

# open log file
logfile = open('flask-grpc-server.log', 'a')

# Redirect stdout and stderr
sys.stdout = logfile
sys.stderr = logfile 

print("creat app")

app = create_app(os.getenv("FLASK_ENV") or "test")

print("__name__: ", __name__)

print("prepare app with class ConnectionsServicer")

class ConnectionServicer(connections_pb2_grpc.ConnectionServiceServicer):
    def GetConnections(self, request, context):
        person_id: int = request.person_id
        start_date: datetime = datetime.strptime(request.start_date, DATE_FORMAT)
        end_date: datetime = datetime.strptime(request.end_date, DATE_FORMAT)
        distance: Optional[int] = request.distance

        results = ConnectionService.find_contacts(
            person_id=person_id,
            start_date=start_date,
            end_date=end_date,
            meters=distance
        )
        return results
print("Create a gRPC server")
# Create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

print("Specify the port to listen on")
# Specify the port to listen on
server.add_insecure_port('localhost:5003')

print("Add the defined service to the server")
# Add the defined service to the server
connections_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionServicer(), server)

print("Start the server")
# Start the server
server.start()

print("Server is running on port 5003...")

def interrupt():
    global server
    server.stop(0)

atexit.register(interrupt)

print("run the app")  

if __name__ == "wsgi":
    app.run(debug=True)