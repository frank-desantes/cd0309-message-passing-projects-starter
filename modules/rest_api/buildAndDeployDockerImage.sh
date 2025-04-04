#!/bin/bash
docker build -t udaconnect-api .
docker tag udaconnect-api frankdesantes/udaconnect-rest-api:latest
docker push frankdesantes/udaconnect-rest-api:latest
kubectl delete -f ../../deployment/udaconnect-rest-api.yaml
kubectl apply -f ../../deployment/udaconnect-rest-api.yaml
kubectl get pods
