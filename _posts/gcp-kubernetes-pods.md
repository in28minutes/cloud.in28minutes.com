---
layout:     post
title:      Google Kubernetes Engine (GKE) Pods - GCP Certification Cheat Sheet
date:       2022-03-01 11:13:00
summary:    Let's get a quick overview of Google Kubernetes Engine (GKE) Pods from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).
categories:  GCP_General GCP_Computing_Services Google_Kubernetes_Engine Google_Cloud_Platform
permalink:  /gcp-kubernetes-engine-pods-gke
---
Let's get a quick overview of Google Kubernetes Engine (GKE) Pods from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).


<BR/>

## Kubernetes - Pods

```sh
Pods are the smallest, most basic deployable objects in Kubernetes. A Pod represents a single instance of a running 
process in your cluster. Pods contain one or more containers, such as Docker containers. When a Pod runs multiple 
containers, the containers are managed as a single entity and share the Pod's resources.
```
![kubernetes-deployment-hierarchy](https://user-images.githubusercontent.com/57451228/144892457-d3ae80b7-0fe1-4e34-b659-425e254a8ef2.png)


- Smallest deployable unit in Kubernetes
- A Pod contains **one or more containers**
- Each Pod is assigned an ephemeral **IP address**
- All containers in a pod share:
  - Network
  - Storage
  - IP Address
  - Ports and
  - Volumes (Shared persistent disks)
- POD statuses : Running /Pending /Succeeded /Failed /Unknown

<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
