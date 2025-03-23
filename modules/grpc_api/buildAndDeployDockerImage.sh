#!/bin/bash
docker build -t udaconnect-grpc-api .
docker tag udaconnect-grpc-api frankdesantes/udaconnect-grpc-api:latest
docker push frankdesantes/udaconnect-grpc-api:latest
kubectl delete -f ../../deployment/udaconnect-grpc-api.yaml
kubectl apply -f ../../deployment/udaconnect-grpc-api.yaml
kubectl get pods
