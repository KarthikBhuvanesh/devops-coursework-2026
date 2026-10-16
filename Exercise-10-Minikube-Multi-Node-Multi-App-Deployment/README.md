# Exercise 10: Minikube Multi-Node, Multi-App Deployment

## Objective
Deploy two Flask applications on a three-node Kubernetes cluster using Minikube, Kubernetes Deployments, pod anti-affinity, and NodePort Services.

## Environment
- Operating system: Windows with Docker Desktop
- Kubernetes: Minikube profile `devops-multinode`
- Kubernetes version: v1.37.0
- Cluster: 1 control-plane node and 2 worker nodes
- Container images: `product-catalog:latest`, `shopping-cart:latest`

## Applications

### App A: Product Catalog
- File: `product_catalog.py`
- Endpoint: `GET /products`
- Returns a sample list of three products: Laptop, Phone, and Headphones.
- Deployment: `product-catalog`
- Replicas: 2
- Service: `product-catalog-service`
- NodePort: 30081

### App B: Shopping Cart
- File: `shopping_cart.py`
- Endpoint: `GET /cart` retrieves the cart.
- Endpoint: `POST /cart` adds a JSON item to the cart.
- Deployment: `shopping-cart`
- Replicas: 3
- Service: `shopping-cart-service`
- NodePort: 30082

The Shopping Cart application stores data in process memory. Each replica maintains its own cart, so requests routed to different replicas may return different cart contents. Persistent, shared cart storage is not implemented.

## Kubernetes Configuration
The application Deployments use required pod anti-affinity with the topology key `kubernetes.io/hostname`. This distributes replicas of the same application across separate nodes.

Both Deployments use `imagePullPolicy: Never` because the images are loaded into the Minikube cluster locally.

## Implementation Steps
1. Started the `devops-multinode` Minikube profile with three nodes.
2. Verified that all three nodes reached the `Ready` state.
3. Built the Docker images for both Flask applications.
4. Loaded both images into the Minikube profile.
5. Created and applied the two Deployment manifests.
6. Created and applied the two NodePort Service manifests.
7. Verified that all five application pods were running.
8. Tested the Product Catalog GET endpoint and Shopping Cart POST endpoint.

## Verification
- All three Kubernetes nodes were `Ready`.
- Product Catalog Deployment: 2/2 replicas ready.
- Shopping Cart Deployment: 3/3 replicas ready.
- Both NodePort Services were created.
- `GET /products` returned the three sample products.
- `POST /cart` accepted a JSON item and returned the submitted cart item.
- A subsequent cart GET returned an empty cart, demonstrating the limitation of replica-local in-memory state.

## Useful Commands

Check nodes:
```powershell
kubectl --context=devops-multinode get nodes -o wide
```

Check pods and node placement:
```powershell
kubectl --context=devops-multinode get pods -o wide
```

Check Deployments and Services:
```powershell
kubectl --context=devops-multinode get deployments,services
```

Apply the manifests:
```powershell
kubectl --context=devops-multinode apply -f product_catalog_deployment.yaml
kubectl --context=devops-multinode apply -f shopping_cart_deployment.yaml
kubectl --context=devops-multinode apply -f product_catalog_service.yaml
kubectl --context=devops-multinode apply -f shopping_cart_service.yaml
```

## Evidence
Screenshots are available in the `evidence/` directory:

1. `cluster-nodes.png` — three-node cluster status.
2. `pods-distribution.png` — pod status and node placement.
3. `deployments-services.png` — Deployment replica counts and Services.
4. `product-catalog-api.png` — Product Catalog API response.
5. `shopping-cart-post.png` — Shopping Cart POST response.

## Limitations
The Shopping Cart application uses an in-memory Python list rather than a shared database. In a multi-replica deployment, this means data is not consistent across pods and is not persistent across container restarts. A shared datastore would be needed for production use.
