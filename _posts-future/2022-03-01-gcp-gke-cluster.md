---
layout:     post
title:      Google Kubernetes Engine (GKE) Cluster - GCP Certification Cheat Sheet
date:       2022-03-01 11:13:00
summary:    Let's get a quick overview of Google Kubernetes Engine (GKE) Cluster from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE) Cluster.
categories:  GCP_General GCP_Computing_Services Google_Kubernetes_Engine Google_Cloud_Platform
permalink:  /gcp-kubernetes-engine-cluster-gke
---
Let's get a quick overview of Google Kubernetes Engine (GKE) Cluster from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE) Cluster.

## You will learn

- What is Google Kubernetes Engine (GKE) Cluster?
- GKE Cluster Types?

<BR/>



## Google Kubernetes Engine (GKE) Cluster

```sh
A cluster is the foundation of Google Kubernetes Engine (GKE): the Kubernetes objects that represent your 
containerized applications all run on top of a cluster. In GKE, a cluster consists of at least one control 
plane and multiple worker machines called nodes.
```
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

<BR/>

## GKE Cluster Types

|Type	| Description|
|:--:|--|
|`Zonal Cluster`	|Single Zone - Single Control plane. Nodes running in the same zone.|
|               |Multi-zonal - Single Control plane but nodes running in multiple zones|
|`Regional cluster`	|Replicas of the control plane runs in multiple zones of a given region. Nodes also run in same zones where control plane runs.|
|`Private cluster`	|VPC-native cluster. Nodes only have internal IP addresses.|
|`Alpha cluster`	|Clusters with alpha APIs - early feature API's. Used to test new K8S features.|






<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
