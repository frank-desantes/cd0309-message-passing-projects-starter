#!/bin/bash
docker build -t udaconnect-kafka-api .
docker tag udaconnect-kafka-api frankdesantes/udaconnect-kafka-api:latest
docker push frankdesantes/udaconnect-kafka-api:latest

kubectl delete -f ../../deployment/udaconnect-kafka-api.yaml
kubectl apply -f ../../deployment/udaconnect-kafka-api.yaml

kubectl get pods
