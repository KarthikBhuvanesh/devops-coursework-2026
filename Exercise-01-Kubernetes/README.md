# Exercise 1: Kubernetes Getting Started

## Objective
Deploy an Nginx Pod on Kubernetes, expose it through a NodePort Service, and access it using a browser.

## Environment
- OS: Windows
- Container runtime: Docker Desktop
- Kubernetes: Minikube
- Application: Nginx

## Commands Executed
```bash
 kubectl run hello-k8s --image=nginx --port=80
 kubectl get pods -o wide
 kubectl expose pod hello-k8s --type=NodePort --port=80
 minikube service hello-k8s
```

## Result
The Nginx Pod reached Running status with 1/1 containers ready. The Nginx welcome page opened successfully in the browser.

## Evidence
- evidence/nginx-welcome.png

## Reference
https://github.com/SunagP/DevOps-Lab/blob/main/Exercises/1-Kubernetes-Getting-Started.md
