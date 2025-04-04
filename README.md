# Running the app
The project has been set up such that you should be able to have the project up and running with Kubernetes.

# clone from github
frank-desantes/cd0309-message-passing-projects-starter

# install the cluster
`kubectl apply -f deployment/`

# verify installation
`kubectl get pods`

kubernetes, postgres, udaconnect-api, udaconnect-app, udaconnect-grpc-api, udaconnect-kafka-api, udaconnect-kafka-broker, udaconnect-rest-api       

# seed database once
`sh scripts/run_db_command.sh <POD_NAME>` - Seed your database against the `postgres` pod. (`kubectl get pods` will give you the `POD_NAME`)

# access frontend
http://localhost:30000/

# see documentation (person)
http://localhost:30001/
