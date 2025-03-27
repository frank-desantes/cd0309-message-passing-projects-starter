import grpc
from concurrent import futures
import atexit
from datetime import datetime
from typing import Optional   

# Import the generated classes
import connections_pb2
import connections_pb2_grpc
import sys

DATE_FORMAT = "%Y-%m-%d"

def start_grpc_server():
    
    print("prepare gRPC server with class ConnectionsServicer")

    class ConnectionServicer(connections_pb2_grpc.ConnectionServiceServicer):
        def GetConnections(self, request, context):
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