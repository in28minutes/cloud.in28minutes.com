---
layout:     post
title:      Google Kubernetes Engine (GKE) Command Line Cheat Sheet - GCP Certification Cheat Sheet
date:       2022-03-01 11:13:00
summary:    Let's get a quick overview of Google Kubernetes Engine (GKE) Command Cheat Sheet from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).
categories:  GCP_General GCP_Computing_Services Google_Kubernetes_Engine Google_Cloud_Platform
permalink:  /gcp-kubernetes-engine-cheat-sheet-command-line-gke
---
Let's get a quick overview of Google Kubernetes Engine (GKE) Command Cheat Sheet from an GCP certification perspective. We will look at important certification questions regarding Google Kubernetes Engine (GKE).

## You will learn

- Google Kubernetes Engine (GKE) Command Line Cheat Sheet

<BR/>

## GKE - Cluster Management - Command 

<BR/>

|Description	|Command|
|:--:|--|
|`Create Cluster`	|gcloud container clusters create my-cluster --zone us-central1-a --node-locations us-central1-c,us-central1-b|
|`Resize Cluster`	|gcloud container clusters resize my-cluster --node-pool my-node-pool --num-nodes 10|
|`Autoscale Cluster`	|gcloud container clusters update cluster-name --enable-autoscaling --min-nodes=1 --max-nodes=10|
|`Delete Cluster`	|gcloud container clusters delete my-cluster|
|`Adding Node Pool`	|gcloud container node-pools create new-node-pool-name --cluster my-cluster|
|`List Images`	|gcloud container images list|

<BR/>

## GKE - Workload Management - Command 
|Description	|Command|
|:--:|--|
|`List Pods/Service/Replica Sets`|	kubectl get pods/services/replicasets|
|`Create Deployment`	|kubectl apply -f deployment.yaml or kubectl create deployment|
|`Create Service`	|kubectl expose deployment hello-world-rest-api --type=LoadBalancer --port=8080|
|`Scale Deployment`	|kubectl scale deployment hello-world --replicas 5|
|`Autoscale Deployment`	|kubectl autoscale deployment --max --min --cpu-percent|
|`Delete Deployment`	|kubectl delete deployment hello-world|
|`Update Deployment`	|kubectl apply -f deployment.yaml|
|`Rollback Deployment`	|kubectl rollout undo deployment hello-world --to-revision=1|







<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
