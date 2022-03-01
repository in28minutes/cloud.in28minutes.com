---
layout:     post
title:      Create a Google Kubernetes Engine (GKE) Cluster - GCP Certification Cheat Sheet
date:       2022-03-01 10:13:00
summary:    Let's get a quick overview of creating a Google Kubernetes Engine (GKE) Cluster in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding creating a Google Kubernetes Engine (GKE) Cluster in Google Cloud Platform.
categories:  GCP_General GCP_Kubernetes_Engine Google_Cloud_Platform
permalink:  /gcp-google-kubernetes-engine-gke-overview
---
Let's get a quick overview of creating a Google Kubernetes Engine (GKE) Cluster in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding creating a Google Kubernetes Engine (GKE) Cluster in Google Cloud Platform.



## You will learn
- How to create a Google Kubernetes Engine (GKE) Cluster?

<BR/>

Hope you are doing extremely well.
In this article I will be show you how to create a Google Kubernetes Engine (GKE) Cluster.

## Prerequisites

- Billing enabled GCP Account ( If you don't have one, create a billing account with your international transaction enabled credit card and you will get $300 credit for free and you can spend it over the next 90 days)


## Setup

**1.** Click the icon on the top right of the screen to open **Cloud Shell**.

<BR/>


![Screenshot 2022-02-01 at 5 04 28 PM](https://user-images.githubusercontent.com/57451228/151963019-73888945-a332-425f-b266-fae6149dc9ee.png)

<BR/>

Once it opened, you will able to view the **Cloud Shell Terminal**.

<BR/>

![Screenshot 2022-02-01 at 5 18 34 PM](https://user-images.githubusercontent.com/57451228/151963601-aa283d9e-79e4-4b73-992a-6342e68eda9f.png)

<BR/>


## Now Let's get started


### Step 1: Setup a default compute zone

To run your containerized application with Google Kubernetes Engine you have to setup your compute zone, in which approximate location your clusters and their resources will be live.

**1.** To setup default compute zone, you have to run the following command. Here I'm using **us-central1-a**.

```sh
gcloud config set compute/zone us-central1-a

```

You will get a output like the following:


![Screenshot 2022-02-26 at 10 23 34 AM](https://user-images.githubusercontent.com/57451228/155847170-815719e6-7ae0-41b9-81ac-839a24f66144.png)

<BR/>

### Step 2: Create Google Kubernetes Engine (GKE) Cluster

A cluster is the foundation of Google Kubernetes Engine (GKE): the Kubernetes objects that represent your containerized applications all run on top of a cluster.

In GKE, a cluster consists of at least one control plane and multiple worker machines called nodes.

Note: Cluster names can not be longer than 40 characters, and must be start with letter and end with alphanumeric.

**1.** Now create the cluster with the following command with your cluster name. 

```sh
gcloud container clusters create [YOUR-CLUSTER]
```

Here I'm using **in28minutes-cluster** as my cluster name. So, let's run the command.


```sh
gcloud container clusters create in28minutes-cluster
```
Now it will take a few minutes and you will get a ouput like below:


![Screenshot 2022-02-26 at 10 30 42 AM](https://user-images.githubusercontent.com/57451228/155847448-54675e47-e4b7-46c7-9fdc-55103406f78b.png)

<BR/>
<BR/>

**Yeppie! Congratulations you have successfully created your GKE Cluster.**






<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
<a href="https://www.linkedin.com/in/debrup-365/">Debrup Mondal ❤️</a>
