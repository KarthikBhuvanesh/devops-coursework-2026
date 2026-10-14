# Exercise 2 — Deploy Flask on Minikube

## Objective
Deploy a Flask web application to Kubernetes using Minikube, Docker, and kubectl.

## Application
The Flask application listens on port 15000 and returns:

`Hello from Flask on Kubernetes!`

## Implementation
1. Created the Flask application in `app.py`.
2. Added Flask to `requirements.txt`.
3. Built the Docker image `flask-app:latest`.
4. Loaded the image into Minikube.
5. Created a Kubernetes Deployment with one replica.
6. Exposed the application through a NodePort Service.

## Verification
- Deployment: `flask-app`
- Pod status: `Running`
- Container port: `15000`
- Service: `flask-app-service`
- Expected response: `Hello from Flask on Kubernetes!`

## Evidence
See `evidence/flask-response.png` for the successful application response.
