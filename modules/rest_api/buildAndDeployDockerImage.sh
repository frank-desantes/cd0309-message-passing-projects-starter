#!/bin/bash
docker build -t udaconnect-api .
docker tag udaconnect-api frankdesantes/udaconnect-api:latest
docker push frankdesantes/udaconnect-api:latest
kubectl delete -f ../../deployment/udaconnect-api.yaml
kubectl apply -f ../../deployment/udaconnect-api.yaml
kubectl get pods
