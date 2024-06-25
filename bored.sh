#!/bin/bash
kubectl delete all --all
docker compose down
docker compose up --build

kubectl apply -f postgres-deployment.yaml
sleep 10
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml

sleep 10

minikube dashboard