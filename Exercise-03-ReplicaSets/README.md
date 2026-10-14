# Exercise 3 — Scaling Flask with Kubernetes ReplicaSets

## Objective
Deploy a Flask flash-sale application on Minikube and understand ReplicaSets, scaling, health probes, and automatic Pod replacement.

## Application Endpoints
- `/` — Returns a welcome message and the serving Pod name.
- `/buy?user=123` — Simulates a purchase and identifies the serving Pod.
- `/health` — Reports application health.

## Implementation
1. Created the Flask application.
2. Built the Docker image `flashsale:1.0`.
3. Loaded the image into Minikube.
4. Created a ReplicaSet with three replicas.
5. Exposed the application through a NodePort Service.
6. Tested the application endpoints.
7. Scaled the ReplicaSet from three to five replicas.
8. Deleted a Pod and verified that Kubernetes created a replacement.

## Final Verification
- ReplicaSet: `flashsale-rs`
- Desired replicas: 5
- Current replicas: 5
- Ready replicas: 5
- Service: `flashsale-svc`
- Container port: 5000

## Key Learnings
- ReplicaSets maintain the desired number of Pod replicas.
- Scaling increases or decreases the number of managed Pods.
- Readiness and liveness probes help Kubernetes monitor application health.
- A deleted Pod is automatically replaced to maintain the desired replica count.
- A Kubernetes Service routes requests to matching Pods.

## Evidence
See the `evidence/` directory for screenshots of deployment, API testing, scaling, and Pod replacement.
