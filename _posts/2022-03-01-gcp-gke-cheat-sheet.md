---
layout:     post
title:      Google Kubernetes Engine (GKE) Cheat Sheet - GCP Certification Cheat Sheet
date:       2022-03-01 11:13:00
summary:    Let's get a quick overview of Google Kubernetes Engine (GKE) Cheat Sheet from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).
categories:  GCP_General GCP_Computing_Services Google_Kubernetes_Engine Google_Cloud_Platform
permalink:  /gcp-kubernetes-engine-cheat-sheet-qna-gke
---
Let's get a quick overview of Google Kubernetes Engine (GKE) Cheat Sheet from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).

## You will learn

- Google Kubernetes Engine Scenarios -Case Study Q/A for GCP Certification?


<BR/>

## Google Kubernetes Engine - Scenarios - 1

| Scenario                                                                    | Solution                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `You want to keep your costs low and optimize your`<br>`GKE implementation` | Consider Preemptible VMs, Appropriate region, Committed-use discounts.<br>E2 machine types are cheaper than N1.<br>Choose right environment to fit your workload type (Use multiple node pools if needed). |
| `You want an efficient, completely auto scaling GKE solution`                 | Configure Horizontal Pod Autoscaler for deployments and Cluster Autoscaler for node pools                                                                                                                          |
| `You want to execute untrusted third-party code in Kubernetes Cluster`        | Create a new node pool with GKE Sandbox. Deploy untrused code to Sandbox node pool.                                                                                                                                |

<BR/>

## Google Kubernetes Engine - Scenarios - 2

| Scenario                                                                                                  | Solution                                                                  |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `You want enable ONLY internal communication between your microservice deployments in a Kubernetes Cluster` | Create Service of type ClusterIP                                          |
| `My pod stays pending`                                                                                      | Most probably Pod cannot be scheduled onto a node(insufficient resources) |
| `My pod stays waiting`                                                                                      | Most probably failure to pull the image                                   |






<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
