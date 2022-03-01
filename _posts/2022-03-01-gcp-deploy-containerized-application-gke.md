---
layout:     post
title:      Deploy a containerized application with Google Kubernetes Engine (GKE) - GCP Certification Cheat Sheet
date:       2022-03-01 10:13:00
summary:    Let's get a quick overview of deploy a containerized application with Google Kubernetes Engine (GKE) in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding cdeploy a containerized application with Google Kubernetes Engine (GKE) in Google Cloud Platform.
categories:  GCP_General GCP_Kubernetes_Engine Google_Cloud_Platform
permalink:  /gcp-deploy-containerized-application-with-google-kubernetes-engine-gke
---
Let's get a quick overview of deploy a containerized application with Google Kubernetes Engine (GKE) in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding deploy a containerized application with Google Kubernetes Engine (GKE) in Google Cloud Platform.


## You will learn
- How to deploy a containerized application with Google Kubernetes Engine (GKE)?

<BR/>

Hope you are doing extremely well.
In this article I will be show you how to deploy a containerized application with Google Kubernetes Engine (GKE).

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


**Yeppie! Congratulations you have successfully created your GKE Cluster.**

<BR/>

### Step 3: Get Authentication credentials for your GKE Cluster

Now you need authentication credentials to work with your GKE Cluster.

**1.** Now you have to run the follwoing command to authenticate with your cluster.

```sh
gcloud container clusters get-credentials [YOUR-CLUSTER]
```
Just replace the name with your cluster name and run the command like this.

```sh
gcloud container clusters get-credentials in28minutes-cluster
```

Now, you will get a output like the follwoing:

![Screenshot 2022-02-26 at 10 31 25 AM](https://user-images.githubusercontent.com/57451228/155847717-12d316cb-f156-45ee-9bab-f6ac4f16dad7.png)

**Congratulations! Now you can interact with your GKE Cluster.**

<BR/>

### Step 4: Deploy an application to the Cluster

Now this is the main agenda of the article, So, watch it carefully.
So, for this article we are using a **hello-app** container image in our cluster. And, we are using our server name as **in28minutes-server**, you can use yours according to your need.

**1.** Now let's create a new deployment in28minutes-server from the hello-app container image.

```sh
kubectl create deployment in28minutes-server --image=gcr.io/google-samples/hello-app:1.0

```
Now you will get a output like this:

![Screenshot 2022-02-26 at 10 32 16 AM](https://user-images.githubusercontent.com/57451228/155847985-aab8ebf3-d2bc-4dce-86bb-d1c95169242c.png)

**Awesome, You have done a great work.**

**2.** Now it's time to expose your application to external traffic by creating **Kubernetes service**.
Use the following command to do that operation:

```sh
kubectl expose deployment in28minutes-server --type=LoadBalancer --port 8080
```

Now you are thinking what is the type=LoadBalancer and port in this command. Port is just to specify the port, where container exposes, and type="LoadBalancer" creates a Compute Engine load balancer for your container.

Okkay! Now you will get a output like that.

```sh
service/in28minutes-server exposed
```

**3.** Now you can inspect your server with the follwing command, in my case it's my in28minutes-server.

```sh
kubectl get service
```

And, the output will be like

![Screenshot 2022-02-26 at 10 33 56 AM](https://user-images.githubusercontent.com/57451228/155848541-00c4d82a-29e9-4974-83d1-081a5f77aaef.png)


Sometime it might take a little more time to generate the external IP address, So, in that case re-run the command again.


**4.** Previous operations are little boring, I know. So, now let's view our application from our web browser with the follwing command.

```sh
http://[EXTERNAL-IPADDRESS]:8080
```

In my case I have to replace the [EXTERNAL-IPADDRESS] with the EXTERNAL-IP of in28minutes-server.

```sh
http://34.134.222.77:8080

```

Wow! Satisfaction!


![Screenshot 2022-02-26 at 10 35 30 AM](https://user-images.githubusercontent.com/57451228/155848696-18046061-11a0-491f-9340-0ffc920f4aa5.png)


**Congratulations you have successfully deployed containerized application to Google Kubernetes Engine (GKE).**

<BR/>

### Step 5: Delete the GKE Cluster

**1.** Now to delete the GKE Cluster we have created earlier, run the following command:

```sh
gcloud container clusters delete in28minutes-cluster
```

**2.** After running command you will get a prompt, You just type **Y** to confirm the action.

![Screenshot 2022-02-26 at 10 36 42 AM](https://user-images.githubusercontent.com/57451228/155848154-b2c91e06-2d43-4e8d-a200-2bbfe6be86a1.png)



It will take some some and you will get a output like this.

![Screenshot 2022-02-26 at 10 40 31 AM](https://user-images.githubusercontent.com/57451228/155848145-dcbf77d3-eac1-46e5-a8ad-b5e74f967f7d.png)

**Congratulations you have successfully deleted your CKE Cluster.**





<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
<a href="https://www.linkedin.com/in/debrup-365/">Debrup Mondal ❤️</a>
