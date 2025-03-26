#!/usr/local/bin/python
import grpc
import connections_pb2
import connections_pb2_grpc


# Establish a channel to the server
channel = grpc.insecure_channel('localhost:5003')
stub = connections_pb2_grpc.ConnectionServiceStub(channel)

# Create a request
request = connections_pb2.ConnectionRequest(
    person_id=5,
    start_date="2020-01-01",
    end_date="2020-12-30",
    distance=5
)

# Make the call
response = stub.GetConnections(request)

# Process the response
print("Connections")
for connection in response.connections:
    print("Person:")
    print(f"           id: {connection.person.id}")
    print(f"   first_name: {connection.person.first_name}")
    print(f"    last_name: {connection.person.last_name}")
    print(f" company_name: {connection.person.company_name}")
    print()
    print("Location:")
    print(f"           id: {connection.location.id}")
    print(f"    person_id: {connection.location.person_id}")
    print(f"    longitude: {connection.location.longitude}")
    print(f"     latitude: {connection.location.latitude}")
    print(f"creation_time: {connection.location.creation_time}")
    print()
    print()

