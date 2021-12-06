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


**Managed** Kubernetes service
Minimize operations with **auto-repair** (repair failed nodes) and **auto-upgrade** (use latest version of K8S always) features
Provides Pod and Cluster Autoscaling
Enable **Cloud Logging and Cloud Monitoring** with simple configuration
Uses **Container-Optimized OS,** a hardened OS built by Google
Provides support for **Persistent disks and Local SSD**

## Kubernetes - A Microservice Journey 

### Getting Started

![kubernetes-engine-1](https://user-images.githubusercontent.com/57451228/144887814-cdd4bb9b-1969-4880-9a39-ff15d3d5ac30.png)


**Let's Have Some Fun**: Let's get on a journey with Kubernetes:
- Let's create a cluster, deploy a microservice and play with it in 13 steps!
**1:** Create a Kubernetes cluster with the default node pool
- gcloud container clusters create or use cloud console
**2:** Login to Cloud Shell
**3:** Connect to the Kubernetes Cluster
- gcloud container **clusters get-credentials** my-cluster --zone us-central1-a --project solid-course-258105

### Deploy Microservice

**4:** Deploy Microservice to Kubernetes:
- Create deployment & service using kubectl commands
  - kubectl create deployment hello-world-rest-api --image=in28min/hello-world-rest-api:0.0.1.RELEASE
  - kubectl expose deployment hello-world-rest-api --type=LoadBalancer --port=8080
**5:** Increase number of instances of your microservice:
- kubectl scale deployment hello-world-rest-api --replicas=2
**6:** Increase number of nodes in your Kubernetes cluster:
- gcloud container clusters resize my-cluster --node-pool my-node-pool --num-nodes 5
- You are NOT happy about manually increasing number of instances and nodes!

<BR/>


<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
