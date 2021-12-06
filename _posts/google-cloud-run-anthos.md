---
layout:     post
title:      Google Cloud Run & Cloud Run - GCP Certification Cheat Sheet
date:       2021-12-06 11:13:00
summary:    Let's get a quick overview of Cloud Run & Cloud Run for Anthos from an GCP certification perspective. We will look at important certification questions regarding Cloud Run & Cloud Run for Anthos.
categories:  GCP_General GCP_Computing_Services 
permalink:  /google-cloud-run-anthos
---

Let's get a quick overview of Cloud Run & Cloud Run for Anthos from an GCP certification perspective. We will look at important certification questions regarding Cloud Run & Cloud Run for Anthos.

![cloud-run](https://user-images.githubusercontent.com/57451228/144812368-360e0166-bfe4-4a84-ac05-691b225dfd0d.png)


## You will learn        
- What is Cloud Run?
- What is Cloud Run for Anthos?
- Advantages of Cloud Run & Cloud Run?   
- What is Cloud Run - From the Command Line?   

## Google Cloud Run - Need

In Kubernetes, we needed to create a cluster.
How about a easier way of deploying containerized applications?
That's the idea behind Cloud Run.

## Cloud Run  
"Container to Production in Seconds"
- Built on top of an open standard - **Knative**
- Fully managed serverless platform for containerized applications
  - ZERO infrastructure management
  - Pay-per-use (For used CPU, Memory, Requests and Networking)

## Cloud Run - Advantages
Fully integrated end-to-end developer experience:
- No limitations in languages, binaries and dependencies
- Easily portable because of container based architecture
- Cloud Code, Cloud Build, Cloud Monitoring & Cloud Logging Integrations

## Anthos - Run Kubernetes clusters anywhere
- Cloud, Multi Cloud and On-Premise
## Cloud Run for Anthos: 
Deploy your workloads to Anthos clusters running on-premises or on Google Cloud
 - Leverage your existing Kubernetes investment to quickly run serverless workloads

## Cloud Run - From the Command Line

| Description	| Command |
|:--:|--|:--:|--|
| Deploy a new container	| gcloud run deploy SERVICE_NAME --image IMAGE_URL --revision-suffix v1 
First deployment creates a service and first revision Next deployments for the same service create new revisions |
| List available revisions	| gcloud run revisions list |
| Adjust traffic assignments |	gcloud run services update-traffic myservice --to-revisions=v2=10,v1=90 |


<BR/>


<pre>
Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>
<br/>
Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
