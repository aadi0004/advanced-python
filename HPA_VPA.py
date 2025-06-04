# HPA (Horizontal Pod Autoscaler) and VPA (Vertical Pod Autoscaler) in Kubernetes
# Kubernetes provides autoscaling mechanisms to efficiently manage resource utilization and ensure application performance. The two primary autoscaling types are Horizontal Pod Autoscaler (HPA) and Vertical Pod Autoscaler (VPA).

# 1. HPA (Horizontal Pod Autoscaler)
# 📌 What is HPA?
# HPA scales the number of pods in a deployment, replica set, or stateful set based on CPU, memory, or custom metrics.

# 📌 How does it work?

# Monitors CPU utilization (default), memory, or external/custom metrics.
# Automatically increases or decreases the number of pods.
# Ensures that the workload meets demand while optimizing resource usage.
# 📌 Use Case:

# Suitable for stateless applications (e.g., web servers, APIs).
# Best for applications that experience fluctuating loads (e.g., e-commerce, streaming services).

# Example: 
# apiVersion: autoscaling/v2
# kind: HorizontalPodAutoscaler
# metadata:
#   name: my-app-hpa
# spec:
#   scaleTargetRef:
#     apiVersion: apps/v1
#     kind: Deployment
#     name: my-app
#   minReplicas: 2
#   maxReplicas: 10
#   metrics:
#     - type: Resource
#       resource:
#         name: cpu
#         target:
#           type: Utilization
#           averageUtilization: 50


# Key Features: Adjusts the number of pods dynamically.
# Uses CPU, memory, or custom metrics for scaling.
# Works well with stateless workloads.

# --------------------------------------------------------------------------

# 2. VPA (Vertical Pod Autoscaler)
# What is VPA?
# VPA adjusts CPU and memory requests/limits for pods based on actual usage.

# How does it work?

# Analyzes pod resource consumption.
# Recommends or automatically updates CPU/memory requests.
# May restart pods to apply new resource limits.
# Use Case:
# Ideal for stateful applications (e.g., databases, ML models).
# Helps optimize resource allocation and prevents under/over-provisioning.

# Example : 
# apiVersion: autoscaling.k8s.io/v1
# kind: VerticalPodAutoscaler
# metadata:
#   name: my-app-vpa
# spec:
#   targetRef:
#     apiVersion: apps/v1
#     kind: Deployment
#     name: my-app
#   updatePolicy:
#     updateMode: "Auto"


#  Key Features:  Adjusts CPU and memory dynamically.
#  Ensures optimal resource allocation.
#  May restart pods to apply new requests/limits.

# -----------------------------------------------------------------------------


# Case Scenario 1: Real-Time Inventory Update Service (VPA) Explained Using Zepto
# Problem: In Zepto, where delivering groceries in 10 minutes is the core promise, the inventory management system plays a crucial role. This system updates stock levels in real time based on restocking or customer orders.

# During flash sales or restocking events, the inventory service needs more CPU and memory resources to handle the surge in updates. However, during regular hours, the workload is much lighter. If resource limits are not properly configured, the system might face two issues:

# Resource Throttling: If the system runs out of allocated resources, it slows down or crashes, causing delays in updating stock availability.
# Over-Provisioning: If resources are over-allocated, Zepto ends up paying for unused resources, increasing operational costs.

# Solution Using VPA: To tackle these challenges, Zepto can use Vertical Pod Autoscaler (VPA) for the inventory management service.

# How it works:
# VPA monitors the service's CPU and memory usage over time. It automatically adjusts the resource requests and limits for the service based on actual usage patterns.
# During a flash sale, VPA increases CPU and memory to handle the high workload.
# During normal hours, it scales down resource allocation to save costs.
# Benefits for Zepto:

# Improved Stability: The inventory system won't crash due to resource throttling during high-demand periods, ensuring accurate stock updates.
# Cost Optimization: Resources are dynamically allocated, avoiding over-provisioning and reducing operational expenses.
# Better Customer Experience: With real-time stock updates, customers can always see accurate product availability, enhancing trust and satisfaction.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Solution : 

# Step 1: Create Namespace
# Create a namespace to isolate the inventory service resources:

# kubectl create namespace inventory-management

# Verify the namespace:
# kubectl get namespaces


# Step 2: Deploy the Inventory Update Service
# Create a deployment YAML file named inventory-deployment.yaml:

# ----------------------------------

# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: inventory-update-service
#   namespace: inventory-management
#   labels:
#     app: inventory-update
# spec:
#   replicas: 2
#   selector:
#     matchLabels:
#       app: inventory-update
#   template:
#     metadata:
#       labels:
#         app: inventory-update
#     spec:
#       containers:
#       - name: inventory-container
#         image: python:3.9-slim
#         command: ["python", "-m", "http.server", "8080"]
#         ports:
#         - containerPort: 8080
#         resources:
#           requests:
#             cpu: "100m"
#             memory: "128Mi"
#           limits:
#             cpu: "500m"
#             memory: "256Mi"

# ---------------------------------------------------------

# kubectl apply -f inventory-deployment.yaml
# kubectl get pods -n inventory-management


# Step 3: Expose the Service
# Create a service YAML file named inventory-service.yaml:

# -------------------------
# apiVersion: v1
# kind: Service
# metadata:
#   name: inventory-service
#   namespace: inventory-management
# spec:
#   selector:
#     app: inventory-update
#   ports:
#     - protocol: TCP
#       port: 80
#       targetPort: 8080
#   type: ClusterIP

# -------------------------


# kubectl apply -f inventory-service.yaml

# kubectl get svc -n inventory-management


# Step 4: Install Vertical Pod Autoscaler (VPA)
# Install the VPA components:

# ubuntu@ip:/kuber/apache$ git clone https://github.com/kubernetes/autoscaler.git

# cd autoscaler/vertical-pod-autoscaler/

# ./hack/vpa-up.sh 
# cd .. 
# ubuntu@ip:/kuber/apache$ ls


# Verify the VPA components are running:
# kubectl get pods -n kube-system | grep vpa


# Step 5: Configure VPA
# Create a VPA YAML file named inventory-vpa.yaml:

# -------------------------------
# apiVersion: autoscaling.k8s.io/v1
# kind: VerticalPodAutoscaler
# metadata:
#   name: inventory-vpa
#   namespace: inventory-management
# spec:
#   targetRef:
#     apiVersion: "apps/v1"
#     kind: Deployment
#     name: inventory-update-service
#   updatePolicy:
#     updateMode: "Auto"

# ------------------------------------------

# kubectl apply -f inventory-vpa.yaml

# kubectl get vpa -n inventory-management


# Step 6: Test the Solution
# Simulate load by running a load generator:

# kubectl run -i --tty load-generator --image=busybox --restart=Never --namespace=inventory-management -- /bin/sh
# while true; do wget -q -O- http://inventory-service; done


# Monitor VPA recommendations:
# kubectl describe vpa inventory-vpa -n inventory-management


# Check resource usage of pods:
# kubectl top pods -n inventory-management


# --------------------------------------------------------------------------------------------------------------------------------


# Case Scenario 2: Delivery Route Optimization API Scaling 
# Problem:
# The route optimization API, which calculates the shortest delivery routes, experiences unpredictable spikes in usage. For example, when multiple delivery agents log in simultaneously or during a sudden surge in orders in a specific region.

# Solution Using HPA and VPA:

# Use HPA to scale the number of API pods dynamically based on the number of active delivery agents or API response time.
# Simultaneously, use VPA to ensure that each API pod has optimal CPU and memory allocations to handle computationally expensive route calculations efficiently.
# Implementation Details:

# Set up a custom metric to monitor the number of active API requests or response latency.
# Configure VPA to adjust resource limits for the API pods based on their workload patterns.
# Benefits:

# Ensures low latency in route optimization calculations.
# Maintains high availability and responsiveness of the API service.
# Combines the benefits of HPA and VPA for both scaling and resource optimization.

# ----------------------------------------------------------

# Solution 
# kubectl create namespace delivery-system
# kubectl get namespaces

# Step 2: Deploy the Route Optimization API
# Create a deployment YAML file named route-optimization-deployment.yaml:
# ----------------------------------

# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: route-optimization-api
#   namespace: delivery-system
#   labels:
#     app: route-optimization
# spec:
#   replicas: 2
#   selector:
#     matchLabels:
#       app: route-optimization
#   template:
#     metadata:
#       labels:
#         app: route-optimization
#     spec:
#       containers:
#       - name: route-optimization-container
#         image: python:3.9-slim
#         command: ["python", "-m", "http.server", "8080"]
#         ports:
#         - containerPort: 8080
#         resources:
#           requests:
#             cpu: "100m"
#             memory: "128Mi"
#           limits:
#             cpu: "500m"
#             memory: "256Mi"

# ----------------------------------------


# kubectl apply -f route-optimization-deployment.yaml

# kubectl get pods -n delivery-system

# ----------------------------------------

# Step 3: Expose the API Using a Service
# Create a service YAML file named route-optimization-service.yaml:

# ---------------------
# apiVersion: v1
# kind: Service
# metadata:
#   name: route-optimization-service
#   namespace: delivery-system
# spec:
#   selector:
#     app: route-optimization
#   ports:
#     - protocol: TCP
#       port: 80
#       targetPort: 8080
#   type: ClusterIP

# -------------------------

# kubectl apply -f route-optimization-service.yaml

# kubectl get svc -n delivery-system

# Step 4: Enable Metrics Server
# Deploy the Metrics Server (required for HPA):

# kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Verify the Metrics Server is running:
# kubectl get pods -n kube-system

# Ensure the Metrics API is available:
# kubectl top pods -n delivery-system



# Step 5: Configure Horizontal Pod Autoscaler (HPA)
# Create an HPA YAML file named route-optimization-hpa.yaml:

# ----------------------------------
# apiVersion: autoscaling/v2
# kind: HorizontalPodAutoscaler
# metadata:
#   name: route-optimization-hpa
#   namespace: delivery-system
# spec:
#   scaleTargetRef:
#     apiVersion: apps/v1
#     kind: Deployment
#     name: route-optimization-api
#   minReplicas: 2
#   maxReplicas: 10
#   metrics:
#   - type: Resource
#     resource:
#       name: cpu
#       target:
#         type: Utilization
#         averageUtilization: 50
# -----------------------------------------


# kubectl apply -f route-optimization-hpa.yaml
# kubectl get hpa -n delivery-system

# Step 6: Configure Vertical Pod Autoscaler (VPA)
#ubuntu@ip:/kuber/apache$ git clone https://github.com/kubernetes/autoscaler.git

# cd autoscaler/vertical-pod-autoscaler/

# ./hack/vpa-up.sh 
# cd .. 
# ubuntu@ip:/kuber/apache$ ls


# Create a VPA YAML file named route-optimization-vpa.yaml:

# --------------------------------
# apiVersion: autoscaling.k8s.io/v1
# kind: VerticalPodAutoscaler
# metadata:
#   name: route-optimization-vpa
#   namespace: delivery-system
# spec:
#   targetRef:
#     apiVersion: "apps/v1"
#     kind: Deployment
#     name: route-optimization-api
#   updatePolicy:
#     updateMode: "Auto"
# --------------------------------------

# kubectl apply -f route-optimization-vpa.yaml
# kubectl get vpa -n delivery-system


# Step 7: Test the Solution
# Simulate load using a load generator. Run the following command in a pod:

# kubectl run -i --tty load-generator --image=busybox --restart=Never --namespace=delivery-system -- /bin/sh
# while true; do wget -q -O- http://route-optimization-service; done


# Monitor the HPA scaling:
# kubectl get hpa -n delivery-system -w

# Check VPA recommendations:
# kubectl describe vpa route-optimization-vpa -n delivery-system

# Check pod resource usage:
# kubectl top pods -n delivery-system
# -----------------------------------------------------------