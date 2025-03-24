#!/usr/local/bin/python
import grpc
import connections_pb2
import connections_pb2_grpc


# Establish a channel to the server
channel = grpc.insecure_channel('localhost:5003')
stub = connections_pb2_grpc.ConnectionServiceStub(channel)

# Create a request
request = connections_pb2.ConnectionRequest(
    person_id="5",
    start_date="2020-01-01",
    end_date="2020-12-30",
    distance=5
)

# Make the call
response = stub.GetConnections(request)

# Process the response
for connection in response.connections:
    print(f"Connection ID: {connection.id}, Name: {connection.name}")

