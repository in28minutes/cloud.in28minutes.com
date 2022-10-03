---
layout:     post
title:      Important Kubernetes Concepts Made Easy
date:       2022-10-02 12:31:19
summary:    Getting Started with Kubernetes is NOT easy.This article will help you understand some of the most important concepts of Kubernetes.
categories:  GCP_CLOUD
permalink:  /kubernetes-for-beginners-important-concepts-simplified
---

Kubernetes is the most popular open source container orchestration solution.

Getting Started with Kubernetes is NOT easy.

This article will help you understand some of the most important concepts of Kubernetes.

![](/gcpimages/02-architecture/container-orchestration.png)

<!-- MarkdownTOC -->

- 1: Why do we need Container Orchestration?
- 2: What is Container Orchestration?
- 3: What is Kubernetes?
- 4: What are the most important Kubernetes concepts?
	- 4.1: What is a Cluster?
	- 4.2: Let's Deploy a Microservice
	- 4.3: What is a Pod?
	- 4.4: What is a ReplicaSet?
	- 4.5: What is a Deployment?
	- 4.6: A Quick Review - Deployment vs Replica Set
	- 4.7: What is a Service?
- 5: Next Steps

<!-- /MarkdownTOC -->


### 1: Why do we need Container Orchestration?

![](/gcpimages/02-architecture/microservices.png)

Most enterprises are adopting Microservices architectures.

Microservices provide the **flexibility to innovate**. 

However, Microservices don't come free. Instead of deploying a few applications, we are deploying hundred's of microservices. This results in increased complexity.

Containers can help simplify your deployment and observability challenges. However, there are still challenges with respect to managing your infrastructure and deployments. Example: I want 10 instances of Microservice A container, 15 instances of Microservice B container, .. and so on for multiple microservices. In addition, I want a number of other features for my microservices. A few typical features include:
- **Auto Scaling** - Scale containers based on demand
- **Service Discovery** - Help microservices find one another
- **Load Balancer** - Distribute load among multiple instances of a microservice
- **Self Healing** - Do health checks and replace failing instances
- **Zero Downtime Deployments** - Release new versions without downtime

### 2: What is Container Orchestration?

Container orchestration solutions provide most technical features need by microservices architectures. You will be able to create a cluster of multiple vm instances and deploy microservices to the cluster. Container orchestration solution will manage the clusters and deployments.

![](/gcpimages/02-architecture/container-orchestration.png) 

### 3: What is Kubernetes?

There are a number of container orchestration platforms: Docker Swarm, Mesosphere, Kubernetes among others. In the last few years, Kubernetes has emerged as the winners in the container orchestration space.

### 4: What are the most important Kubernetes concepts?

Let's say you want to setup a microservices architecture with Kubernetes. Here's how the workflow would look like:
- Step 1: Create a Kubernetes cluster with multiple nodes (or virtual machines)
- Step 2: Deploy and configure your first Microservice
- Step 3: Deploy and configure your second Microservice

Let's now look at each of these in depth.

#### 4.1: What is a Cluster?

![](/gcpimages/gcp/kubernetes-02-architecture-cluster.png)

A **cluster** is a group of virtual machines. In the cluster, there are two types of nodes:
- **Master Node(s)** - Manages the cluster. You send all your deployment instructions to master node.
- **Worker Node(s)** - All microservices run on the worker nodes.


Here are some of the important **Master Node** (Control plane) components:
- **API Server** - Handles all communication for a K8S cluster (from nodes and outside)
- **Scheduler** - Decides placement of pods
- **Control Manager** - Manages deployments & replicasets
- **etcd** - Distributed database storing the cluster state

The job of a **worker node** is to run your microservices. In addition, a Kubernetes component called a Kubelet runs on each pod. Kubelet enables worker nodes to communicate with the master node(s).

#### 4.2: Let's Deploy a Microservice

Let's say I want to deploy 5 instances of V1 of microservice A. The command to issue to create a deployment and set number of instances for it is similar to what you see below:

```
**create deployment** hello-world-rest-api --image=in28min/hello-world-rest-api:0.0.1.RELEASE
scale deployment hello-world-rest-api --replicas=5
```

This would deploy v1 of your microservice A with 5 instances to the Kubernetes cluster.

Internally, Kubernetes would create
- A Deployment
- A ReplicaSet and
- 5 Pods

Why does Kubernetes do this?

Let's dig deeper.

#### 4.3: What is a Pod?

A pod is the smallest deployable unit in Kubernetes. A pod represents an instance of your microservice. Each Pod is assigned an ephemeral **IP address**. 

![](/gcpimages/gcp/kubernetes-deployment-hierarchy.png) 

If I have 10 instance of a Microservice A and 12 instances of Microservice B running in a Kubernetes cluster, then I would have a total of 10 + 12 = 22 pods running.

#### 4.4: What is a ReplicaSet?

We deployed microservice A with 5 instances to Kubernetes cluster. This would mean that you have 5 pods running. Let's say you kill one of the pods. Kubernetes would automatically recognize this and create a replacement pod. Kubernetes monitors the health of your pods and replace unhealthy pods. How does Kubernetes do this?

This is the job of a ReplicaSet. 

A ReplicaSet ensures that a specified number of pods are always running. In the above example, a ReplicaSet ensures that 5 instances of Microservice A are always running.

#### 4.5: What is a Deployment?

If a ReplicaSet ensures specific number of pods, what is the role of Deployment?

A deployment ensures that you have flexibility when you release new versions of your microservices.

A deployment represents all the versions of your microservice. 

Currently we have just one version of the microservice. However, you can deploy a new version. Let's say, I want to deploy V2 of microservice without any downtime. 

That's the job of a Deployment.

![](/gcpimages/gcp/kubernetes-deployment-hierarchy.png) 

When you deploy a new version of an existing microservice, the Deployment would create a new ReplicaSet for V2 of Microservice A.

You will have:
- One Deployment representing the Microservice A
- One ReplicaSet for V1 of Microservice A
- One ReplicaSet for V2 of Microservice A

Deployment uk

#### 4.6: A Quick Review - Deployment vs Replica Set

```
kubectl create deployment microservice1 --image=microservice1:v1
```
A **deployment** is created for each microservice. A Deployment represents a microservice (with all its releases). A Deployment manages new releases ensuring zero downtime.

A **Replica set** ensures that a specific number of pods are running for a specific microservice version. Even if one of the pods is killed, replica set will launch a new one.

```
kubectl set image deployment microservice1 microservice1=microservice1:v2
```

When you deploy a V2 of microservice, a new ReplicaSet (V2 Replic Set) is created.

Deployment updates V1 Replica Set and V2 Replica Set based on the release strategies configured.

#### 4.7: What is a Service?

In Kubernetes, each Pod has its **own IP address**. How do you ensure that external users are not impacted when:
- Either a pod fails and is replaced OR
- A new version of microservice is deployed and all existing pods of old release are replaced by ones of new release

Solution: Create a **Service**.

```
expose deployment name --type=LoadBalancer --port=80
```
A service expose you deployments to the outside world using a stable IP address. This ensures that your users are not impacted as pods go down and come up.

There are three types of services:
- **ClusterIP**: Exposes Service on a cluster-internal IP. Use case: You want your microservice only to be available inside the cluster (Intra cluster communication).
- **LoadBalancer**: Exposes Service externally using a cloud provider's load balancer. Use case: You want to create individual Load Balancer's for each microservice.
- **NodePort**: Exposes Service on each Node's IP at a static port (the NodePort). Use case: You DO not want to create an external Load Balancer for each microservice (You can create one Ingress component to load balance multiple microservices).

### 5: Next Steps

- 1: Try Kubernetes Playground - https://labs.play-with-k8s.com/
- 2: Create a Kubernete cluster in one of the cloud platforms and play with it (GKE has a free tier. You can try AKS and EKS but they are not part of free tier as of now!)