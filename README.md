My Dependencygraph is in .dependency_graph.odg

## Running the app
The project has been set up such that you should be able to have the project up and running with Kubernetes.

## install the cluster
`kubectl apply -f deployment`

# verify installation
`kubectl get pods`
kubernetes                ClusterIP   10.43.0.1       <none>        443/TCP          5h59m
postgres                  NodePort    10.43.158.147   <none>        5432:32587/TCP   5h40m
udaconnect-api            NodePort    10.43.193.241   <none>        5000:30001/TCP   5h40m
udaconnect-app            NodePort    10.43.199.8     <none>        3000:30000/TCP   11m
udaconnect-grpc-api       NodePort    10.43.68.175    <none>        5003:30003/TCP   17m
udaconnect-kafka-api      NodePort    10.43.103.166   <none>        5004:30004/TCP   5h40m
udaconnect-kafka-broker   NodePort    10.43.166.127   <none>        9092:30005/TCP   16m
udaconnect-rest-api       NodePort    10.43.65.213    <none>        5002:30002/TCP   5h40m

`kubectl get svc`
kubernetes                ClusterIP   10.43.0.1       <none>        443/TCP          5h59m
postgres                  NodePort    10.43.158.147   <none>        5432:32587/TCP   5h40m
udaconnect-api            NodePort    10.43.193.241   <none>        5000:30001/TCP   5h40m
udaconnect-app            NodePort    10.43.199.8     <none>        3000:30000/TCP   11m
udaconnect-grpc-api       NodePort    10.43.68.175    <none>        5003:30003/TCP   17m
udaconnect-kafka-api      NodePort    10.43.103.166   <none>        5004:30004/TCP   5h40m
udaconnect-kafka-broker   NodePort    10.43.166.127   <none>        9092:30005/TCP   16m
udaconnect-rest-api       NodePort    10.43.65.213    <none>        5002:30002/TCP   5h40m

# seed database once
`sh scripts/run_db_command.sh <POD_NAME>` - Seed your database against the `postgres` pod. (`kubectl get pods` will give you the `POD_NAME`)


# access frontend
http://localhost:30000/

# see documentation (person)
http://localhost:30001/
