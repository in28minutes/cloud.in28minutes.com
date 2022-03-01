---
layout:     post
title:      Google Kubernetes Engine (GKE) - GCP Certification Cheat Sheet
date:       2022-03-01 10:13:00
summary:    Let's get a quick overview of Google Kubernetes Engine (GKE) in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE) in Google Cloud Platform.
categories:  GCP_General GCP_Kubernetes_Engine Google_Cloud_Platform
permalink:  /gcp-google-kubernetes-engine-gke-overview
---
Let's get a quick overview of Google Kubernetes Engine (GKE) in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE) in Google Cloud Platform.


## You will learn
- What is Kubernetes Engine?
- What is Google Kubernetes Engine (GKE)?
- How GKE work?
- Features provide by Kubernetes on Google Cloud?



## Kubernetes Engine

![kubernetes-engine-card](https://user-images.githubusercontent.com/57451228/156114123-2b84f9f8-02e1-410c-9be9-5b13b3633948.png)


```sh
Kubernetes is an open-source container orchestration system for automating software deployment, scaling, and management. 
Google originally designed Kubernetes, but the Cloud Native Computing Foundation now maintains the project.
```

## Google Kubernetes Engine (GKE)


![kubernetes-engine](https://user-images.githubusercontent.com/57451228/156112828-3156195a-f08b-43fc-96e9-f9fe4a1b9e45.png)


Google Kubernetes Engine known as GKE use Google Infrastructure and provides a managed environment, which provides following benifits to your containerized applications.
- Deploy
- Manage
- Scale 

## Cluster orchestration with Google Kubernetes Engine

![container-engine-card](https://user-images.githubusercontent.com/57451228/156113442-36e2a344-b9e7-40d5-9ed1-c9a2a8eabbca.png)



The clusters used by Google Kubernetes Engine are provided by open source cluster management system Kubernetes. 

Kubernetes provides all the mechanisms which you need to interact with container cluster. And also Kubernete's commands and resources are used to deploy, manage application, set policies, perform administrative tasks, and monitor the health of deployed workloads.


## Features provide by Kubernetes on Google Cloud

Google Kubernetes Engine (GKE) provides advantages of advanced cluster management featrures. 



### 1. Node pools
![kubernetes-engine-card](https://user-images.githubusercontent.com/57451228/156113261-4d2e4c7e-9306-46b4-b5dc-b07437d959ee.png)


- If you don't know Node pools, it's just a group of nodes with the same configuration within a cluster. 
- When you create a cluster, the number of nodes and type of nodes that you specify are used to create the first node pool of the cluster. Then, you can add additional node pools of different sizes and types to your cluster. 
- All nodes in any given node pool are identical to one another.
- It's to designate subsets of nodes within a cluster for additional flexibility


### 2. Load Balancing

![load-balancing-card](https://user-images.githubusercontent.com/57451228/156112972-e0f83dec-36ea-4150-babe-0e33f98cf31c.png)




- Google Cloud offers server-side load balancing so you can distribute incoming traffic across multiple virtual machine (VM) instances. Load balancing provides the following benefits:
  - Support Heavy Traffic
  - Scale your Application
  - It detects unhealthy VM instances and remove it using Health Checks. Re-added VM's automatically if it become healthy.
  - Routing traffic to the closest VM

### 3. Auto Scaling

![kubernetes-engine-card](https://user-images.githubusercontent.com/57451228/156113261-4d2e4c7e-9306-46b4-b5dc-b07437d959ee.png)

  - Based on the demand of your workload, Google Kubernetes Engine's Autoscaler automatically resizes the number of nodes in the given node pool. 
  - Note: You can set minimum and maximum siz for node pools, and rest of the things will be automatic, you don't have to do anuthing manually.


### 4. Auto Upgrades

![kubernetes-engine-card](https://user-images.githubusercontent.com/57451228/156113261-4d2e4c7e-9306-46b4-b5dc-b07437d959ee.png)

- Node auto-upgrade provides features to keep your nodes in your cluster up-to-date with the cluster control plane version when your control plane is updated on your behalf.
- Advantages of Auto-upgrade:
  - You don't have to worry about manually track and update your nodes when you upgrade your control plane.
  - Many times new upgrade are released to fix some security issues. With the help of auto-upgrade, GKE automatically check that the security update is applied and up-to-date.
  - With auto update your nodes get all the latest Kubernetes features.
    
### 5. Auto-repairing nodes 

![kubernetes-engine-card](https://user-images.githubusercontent.com/57451228/156113261-4d2e4c7e-9306-46b4-b5dc-b07437d959ee.png)

- Node auto-repair provide features to keep the nodes healthy and running state in the GKE Cluster. With periodic checks GKE check the health state of each node inside your cluster.
- GKE start a repair process for node, if it fails health check over a extended time period.


### 6. Logging & Monitoring

![logging-card](https://user-images.githubusercontent.com/57451228/156112747-2869c91f-5036-4f75-a101-f451435b3e38.png)

![monitoring-card](https://user-images.githubusercontent.com/57451228/156112763-af5677c9-5f9e-4f0b-a007-0dd5ae05b0e8.png)

- Google Cloud Operations for Google Kubernetes Engine is created to monitor GKE Clusters. 
- It provides services to manage Monitoring and Logging together. 
- It also provides a GKE dashboard which gives a customized interface for GKE clusters. With it you can view:
   - Cluster's key metrics like Memory utilization, the number of open incidents and, CPU Utilization.
   - Inspect namespaces, nodes, workloads, services, pods, and containers.
   - Metrics as a function of time and view log entries for pods and containers
   - Clusters with filters like Infrastructure, workloads, or services 


<BR/>
<BR/>


**Congratulations! Now you have basic understanding of Google Kubernetes Engine (GKE).**




<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
<a href="https://www.linkedin.com/in/debrup-365/">Debrup Mondal ❤️</a>
