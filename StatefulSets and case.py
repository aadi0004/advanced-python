# What is a StatefulSet in Kubernetes?
# A StatefulSet is a Kubernetes resource used to manage stateful applications, ensuring each pod has a stable identity, persistent storage, and ordered scaling. Unlike a Deployment, where pods are stateless and interchangeable, StatefulSets maintain a consistent identity across restarts.

# Why Do We Use StatefulSets?
# We use StatefulSets for applications that require: ✅ Stable and Unique Network Identifiers – Each pod gets a persistent hostname (pod-0, pod-1, etc.).
# ✅ Stable Persistent Storage – Each pod gets a dedicated Persistent Volume Claim (PVC) that remains even if the pod is restarted.
# ✅ Ordered Deployment & Scaling – Pods are created one at a time, ensuring proper initialization before the next starts.
# ✅ Ordered Updates & Deletion – When updating or deleting, pods are terminated in reverse order (pod-2 before pod-1, etc.).


# Use Cases of StatefulSets
# 🚀 Databases – MySQL, PostgreSQL, MongoDB, Cassandra, etc.
# 🔄 Distributed Caches – Redis, Zookeeper, etc.
# 📡 Message Brokers – Kafka, RabbitMQ, etc.
# 🖥️ Monitoring Systems – Prometheus, ElasticSearch, etc.



# How StatefulSets Work?
# 1️⃣ Create a Headless Service (serviceName) – Provides stable DNS names for pods.
# 2️⃣ Pods Get Unique Names – mysql-statefulset-0, mysql-statefulset-1, etc.
# 3️⃣ Persistent Storage (PVCs) Per Pod – Each pod gets dedicated storage, not shared.
# 4️⃣ Rolling Updates and Deletion Order – Ensures consistency during updates.

# When NOT to Use StatefulSets?
# ❌ If your application is stateless (e.g., Nginx, frontend apps), use Deployments instead.
# ❌ If you don’t need persistent storage or ordered scaling, use ReplicaSets or Deployments.


# ---------------------------------------------------------------
# Scenario: Managing Databases in an E-Commerce Platform
# A large-scale e-commerce platform like Flipkart, Amazon, or Myntra needs a highly available and scalable database system to store:
# ✅ User data (accounts, order history)
# ✅ Product catalog (price, inventory, details)
# ✅ Orders and transactions (payment processing, order tracking)

# For such applications, MySQL with StatefulSets is a perfect choice because:
# 🔹 Pods need stable hostnames to ensure replication works correctly.
# 🔹 Each database instance requires persistent storage to prevent data loss.
# 🔹 Scaling needs to be ordered to maintain consistency in a database cluster.


# used killerconda


# 1️⃣ Create a Namespace for the E-Commerce Platform
# Namespaces isolate resources, so we create a separate namespace flipkart for our application.

# kubectl create namespace flipkart

# kubectl get namespaces

# 2️⃣ Deploy a Headless Service for MySQL
# A headless service ensures that each MySQL pod gets a stable DNS name, crucial for cluster replication.

# vim mysql-service.yaml
# ---------------------------------------------
# apiVersion: v1
# kind: Service
# metadata:
#   name: mysql-service
#   namespace: flipkart
# spec:
#   clusterIP: None  # Headless service
#   selector:
#     app: mysql
#   ports:
#     - name: mysql
#       port: 3306
#       targetPort: 3306
# --------------------------------------------
# kubectl apply -f mysql-service.yaml

# 3️⃣ Deploy MySQL StatefulSet
# We create a 3-replica MySQL cluster with persistent storage.

# vim mysql-statefulset.yaml

# ------------------------------------
# apiVersion: apps/v1
# kind: StatefulSet
# metadata:
#   name: mysql-statefulset
#   namespace: flipkart
# spec:
#   serviceName: mysql-service
#   replicas: 3  # 3 MySQL instances
#   selector:
#     matchLabels:
#       app: mysql
#   template:
#     metadata:
#       labels:
#         app: mysql
#     spec:
#       containers:
#         - name: mysql
#           image: mysql:8.0
#           ports:
#             - containerPort: 3306
#           env:
#             - name: MYSQL_ROOT_PASSWORD
#               value: root
#             - name: MYSQL_DATABASE
#               value: flipkart_db
#           volumeMounts:
#             - name: mysql-data
#               mountPath: /var/lib/mysql
#   volumeClaimTemplates:
#     - metadata:
#         name: mysql-data
#       spec:
#         accessModes: ["ReadWriteOnce"]
#         resources:
#           requests:
#             storage: 5Gi  # Each pod gets a 5GB PVC

# -------------------------------------------------------------------------

# kubectl apply -f mysql-statefulset.yaml

# kubectl get pods -n flipkart

# kubectl get pvc -n flipkart

# kubectl exec -it mysql-statefulset-0 -n flipkart -- bash

# mysql -u root -p 

# Enter password: root
##### Welcome to the MySQL monitor.  Commands end with ;

### Hmne abhi tk ek stateful set k through mysql bna diya . 

# show databases; 
# exit 
# exit 
# kubectl delete pod mysql-statefulset-0 -n flipkart
# kubectl get pods -n flipkart


