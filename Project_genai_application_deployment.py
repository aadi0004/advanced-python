# Streamlit Application 
# Requirements.txt(streamlit , google-generativeai , python-dotenv)
# .env file (API_KEY)
# App.py file 

# localhost ---> Run 8501 Port 

# step-1 
# Create a github repo of your application 

# https://github.com/1602saurab/pce_bot.git

# step-2 
# Go to AWS ---> 
# 2 EC2 SERVER (1. CI SERVER   2. DEPLOYMENT SERVER)

# 2.1. CI SERVER ----> Install docker  , clone github repository , create docker image , docer login, push image to docker hub . 

# 2.2. DEPLOYMENT SERVER ---> docker install , minikube install , Deployment file , Service.yaml  , EXPOSE SERVICE   , ec2 server ---> security ---> edit inbound rules ---> port(8501)--> New tab on browser ---> public_IP:8501 



# clone git repo 

# IN CI-SERVER 
# sudo apt-get update 
# sudo apt-get install docker.io -y 
# sudo usermod -aG docker $USER && newgrp docker 

# vim Dockerfile 

# press ---> i 
# -------------------------------------------------------------
# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set the working directory
# WORKDIR /app

# # Copy requirements.txt and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the application code
# COPY . .

# # Expose the Streamlit port
# EXPOSE 8501

# # Run the Streamlit application
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# -------------------------------------------------------------------
# press ---> esc ---> :wq 

# sudo systemctl status docker

# docker build -t aaditya2/resume . 

# docker login 

# docker push aaditya2/resume:latest 

# ----------------------------------------------------------------

# In deployment server 

# sudo apt-get update 
# sudo apt-get install docker.io -y
# sudo usermod -aG docker $USER && newgrp docker
# mkdir minikube 
# cd minikube/
# sudo apt install -y curl wget apt-transport-https

# sudo systemctl enable --now docker 
#  
## Is command s docker enable kr rhe h . systemctl enable docker ka mtlb h let's say hmara docker system k sath restart ho gya to bhi docker apne ap restart ho jayga . 

# curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64


### Is command s minikube install ho jaygi 
# ls 
# chmod +x minikube
# sudo mv minikube /usr/local/bin/
# minikube version 


# minikube start --driver=docker --vm=true 

### Is command s minikube start ho jaygi 
# vm=true hm tb likhte h jb hm ec2-server ya virtual machine per chla rhe ho . y thoda sa time lega . 

# sudo snap install kubectl --classic 


# vim Deployment.yaml 

# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: streamlit-chatbot
#   labels:
#     app: streamlit-chatbot
# spec:
#   replicas: 2
#   selector:
#     matchLabels:
#       app: streamlit-chatbot
#   template:
#     metadata:
#       labels:
#         app: streamlit-chatbot
#     spec:
#       containers:
#       - name: streamlit-chatbot
#         image: saurabhbrd/pce_bot:latest
#         ports:
#         - containerPort: 8501
#         env:
#         - name: GOOGLE_API_KEY
#           valueFrom:
#             secretKeyRef:
#               name: google-api-key-secret
#               key: GOOGLE_API_KEY



# service.yaml
# -----------------------------------------------
# apiVersion: v1
# kind: Service
# metadata:
#   name: streamlit-chatbot-service
# spec:
#   type: LoadBalancer
#   selector:
#     app: streamlit-chatbot
#   ports:
#   - protocol: TCP
#     port: 80
#     targetPort: 8501
# ---------------------------------------------------


# kubectl create secret generic google-api-key-secret --from-literal=GOOGLE_API_KEY="AIzaSyANXr72zrdUU9fQPx9CM-YfZpb2vGsmjJM"


# kubectl create secret generic google-api-key-secret --from-literal=GOOGLE_API_KEY = "433TGRFVGFGVG"


# kubectl apply -f Deployment.yaml 
# kubectl apply -f service.yaml 

# kubectl get pods 
# kubectl get svc 

# minikube service streamlit-chatbot-service --url
# Output ---> http://192.168.49.2:31702

# curl -L http://192.168.49.2:31702

# kubectl expose deployment streamlit-chatbot --type=NodePort

# kubectl port-forward svc/streamlit-chatbot-service 8501:80 --address 0.0.0.0


####Now go to ec2instance(Deployment-server) ---> go to security credentials ---> Edit enbound rules ---->Add rules --->Port range(8501),Source(AnywhereIPV4) ---> click to save .

# Access the app on the browser using the public IP and port 8501

