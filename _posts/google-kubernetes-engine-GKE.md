---
layout:     post
title:      Google Kubernetes Engine (GKE) - GCP Certification Cheat Sheet
date:       2021-12-06 11:13:00
summary:    Let's get a quick overview of Encryption in Google Kubernetes Engine (GKE) from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).
categories:  GCP_General
permalink:  /google-kubernetes-engine-GKE
---
Let's get a quick overview of Encryption in Google Kubernetes Engine (GKE) from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).

## You will learn
- What is Kubernetes?
- What is Google Kubernetes Engine (GKE)?
- Why do we need Google Kubernetes Engine (GKE)?
- Advantages of Google Kubernetes Engine (GKE)?
- What is Google Kubernetes Engine (GKE) Cluster?
- GKE Cluster Types?
- What is Kubernetes - Pods?
- Kubernetes - Deployment vs Replica Set?
- GKE - Cluster Management - Command Line?
- GKE - Workload Management - Command Line?

## Kubernetes

![container-orchestration](https://user-images.githubusercontent.com/57451228/144887464-a10eb4f3-24aa-4c0a-bca8-3e87716c49ff.png)


Most popular open source container orchestration solution
Provides Cluster Management (including upgrades)
  - Each cluster can have different types of virtual machines
  
Provides all important container orchestration features:
  - Auto Scaling
  - Service Discovery
  - Load Balancer
  - Self Healing
  - Zero Downtime Deployments

## Google Kubernetes Engine (GKE)

![kubernetes-engine](https://user-images.githubusercontent.com/57451228/144887611-b39aabbf-7acc-4788-a2d4-b287f7ad16df.png)


- **Managed** Kubernetes service
- Minimize operations with **auto-repair** (repair failed nodes) and **auto-upgrade** (use latest version of K8S always) features
- Provides Pod and Cluster Autoscaling
- Enable **Cloud Logging and Cloud Monitoring** with simple configuration
- Uses **Container-Optimized OS,** a hardened OS built by Google
- Provides support for **Persistent disks and Local SSD**

## Kubernetes - A Microservice Journey 

### Getting Started

![kubernetes-engine-1](https://user-images.githubusercontent.com/57451228/144887814-cdd4bb9b-1969-4880-9a39-ff15d3d5ac30.png)


- **Let's Have Some Fun**: Let's get on a journey with Kubernetes:
  - Let's create a cluster, deploy a microservice and play with it in 13 steps!
- **1:** Create a Kubernetes cluster with the default node pool
  - gcloud container clusters create or use cloud console
- **2:** Login to Cloud Shell
- **3:** Connect to the Kubernetes Cluster
  - gcloud container **clusters get-credentials** my-cluster --zone us-central1-a --project solid-course-258105

### Deploy Microservice

- **4:** Deploy Microservice to Kubernetes:
  - Create deployment & service using kubectl commands
   - kubectl create deployment hello-world-rest-api --image=in28min/hello-world-rest-api:0.0.1.RELEASE
   - kubectl expose deployment hello-world-rest-api --type=LoadBalancer --port=8080
- **5:** Increase number of instances of your microservice:
  - kubectl scale deployment hello-world-rest-api --replicas=2
- **6:** Increase number of nodes in your Kubernetes cluster:
  - gcloud container clusters resize my-cluster --node-pool my-node-pool --num-nodes 5
  - You are NOT happy about manually increasing number of instances and nodes!

### Auto Scaling 

- **7:** Setup auto scaling for your microservice:
  - kubectl **autoscale deployment** hello-world-rest-api --max=10 --cpu-percent=70
     - Also called horizontal pod autoscaling - HPA - kubectl get hpa
- **8:** Setup auto scaling for your Kubernetes Cluster
  - gcloud **container clusters update** cluster-name --enable-autoscaling --min-nodes=1 --max-nodes=10
- **9:** Add some application configuration for your microservice
  - Config Map - kubectl **create configmap** todo-web-application-config --from-literal=RDS_DB_NAME=todos
- **10:** Add password configuration for your microservice
  - Kubernetes Secrets - kubectl **create secret** generic todo-web-application-secrets-1 --from-literal=RDS_PASSWORD=dummytodos

### Kubernetes Deployment YAML - Deployment

```sh
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: hello-world-rest-api
  name: hello-world-rest-api
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-world-rest-api
  template:
    metadata:
      labels:
        app: hello-world-rest-api
    spec:
      containers:
      - image: in28min/hello-world-rest-api:0.0.3.RELEASE
        name: hello-world-rest-api
```

### Kubernetes Deployment YAML - Service

```sh
apiVersion: v1
kind: Service
metadata:
  labels:
    app: hello-world-rest-api
  name: hello-world-rest-api
  namespace: default
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    app: hello-world-rest-api
  sessionAffinity: None
  type: LoadBalancer
```

### Kubernetes - A Microservice Journey - The End!

- **11:** Deploy a new microservice which needs nodes with a GPU attached
  - Attach a new node pool with GPU instances to your cluster
     - gcloud **container node-pools create** POOL_NAME --cluster CLUSTER_NAME
     - gcloud container node-pools list --cluster CLUSTER_NAME
  - Deploy the new microservice to the new pool by setting up nodeSelector in the deployment.yaml
     - nodeSelector: cloud.google.com/gke-nodepool: POOL_NAME
- **12:** Delete the Microservices
  - Delete service - kubectl **delete service**
  - Delete deployment - kubectl **delete deployment**
- **13:** Delete the Cluster
  - gcloud container **clusters delete**

## Google Kubernetes Engine (GKE) Cluster

![kubernetes-02-architecture-cluster](https://user-images.githubusercontent.com/57451228/144890891-eec5159d-0b73-4c65-a0e8-41e19a357170.png)


- **Cluster :** Group of Compute Engine instances:
  - **Master Node(s) -** Manages the cluster
  - **Worker Node(s) -** Run your workloads (pods)
- **Master Node** (Control plane) components:
  - **API Server** - Handles all communication for a K8S cluster (from nodes and outside)
  - **Scheduler -** Decides placement of pods
  - **Control Manager -** Manages deployments & replicasets
  - **etcd -** Distributed database storing the cluster state
- **Worker Node** components:
  - Runs your pods
  - **Kubelet** - Manages communication with master node(s)

## GKE Cluster Types

|Type	| Description|
|:--:|--|
|Zonal Cluster	|Single Zone - Single Control plane. Nodes running in the same zone.|
Multi-zonal - Single Control plane but nodes running in multiple zones
|Regional cluster	|Replicas of the control plane runs in multiple zones of a given region. Nodes also run in same zones where control plane runs.|
|Private cluster	|VPC-native cluster. Nodes only have internal IP addresses.|
|Alpha cluster	|Clusters with alpha APIs - early feature API's. Used to test new K8S features.|

<BR/>


<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
