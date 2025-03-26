#!/bin/bash
docker build -t udaconnect-app .
docker tag udaconnect-app frankdesantes/udaconnect-app:latest
docker push frankdesantes/udaconnect-app:latest
kubectl delete -f ../../deployment/udaconnect-app.yaml
kubectl apply -f ../../deployment/udaconnect-app.yaml
kubectl get pods
