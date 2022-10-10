---
layout:     post
title:      Google Cloud For Beginners - How to choose a Compute Service?
date:       2022-10-09 12:31:19
summary:    Google Cloud offer multiple compute options. How to choose between them?
categories:  GCP_CLOUD
permalink:  /google-cloud-for-beginners-choosing-compute
---


We need a compute device to run your applications and services. Traditionally, we are used to making use of Virtual Machine's in our data centers. However, cloud platforms provide you with greater flexibility. How do you choose compute service in Google Cloud?

Let's find out!

![](/images/aws/cloud-2-PAAS.png)

<!-- MarkdownTOC -->

- 1: How do we run applications in a data center?
- 2: What is Infrastructure as a Service?
- 3: Does Cloud bring innovation?
	- 3.1: What is Platform as a Service?
	- 3.2: Why do we need Containers?
	- 3.3: How does Docker help?
	- 3.4: Why do we need Container Orchestration?
		- What is Container Orchestration?
		- What is Kubernetes?
	- 3.5 What is Serverless?
		- Are all serverless services really serverless?
- 4: What are the Google Cloud Compute Services?
	- 4.1: Google Compute Engine
	- 4.2: Google App Engine
		- Comparing Google Compute Engine and Google App Engine
			- **Compute Engine**
			- **App Engine**
	- 4.3: Google Kubernetes Engine
	- 4.4: Google Cloud Functions
	- 4.5: Google Cloud Run
	- 4.6: Google Cloud Anthos
- 5: Here is a Quick Summary

<!-- /MarkdownTOC -->

## 1: How do we run applications in a data center?

Here are the typical steps:
- 1: Create a VM
- 2: Install OS
- 3: Install Software You Need
- 4: Install Application Runtime (Python, Java , ...)
- 5: Deploy your Application

This is what we are used to doing for more than a decade.

And we can do this in the cloud too! 

## 2: What is Infrastructure as a Service?

In the cloud, we call this IaaS (Infrastructure as a Service).

![](/images/aws/cloud-0-IAAS.png)

Each of the cloud platforms provide an IaaS service. 

In Google Cloud, the service is Google Compute Engine (GCE).

You can use GCE to create a VM (choose the OS and hardware) and deploy your applications.

GCE will give you a lot of flexibility:
- Choice of hardware
- Choice of OS
- Full customization of software
- Ability to SSH into the machine

However, you take a lot of responsibility as well. You are responsible for:
- Configuring load balancing
- Auto scaling
- OS upgrades and patches
- Availability
- etc.. ( and a lot of things!)


## 3: Does Cloud bring innovation?

Question to ask is: "Do you want to continue **running applications in the cloud**, the **same way you run them** in your **data center**?" OR **are there OTHER approaches**?.

To answer this question, you should **understand some terminology** used with cloud services:
- **PaaS** (Platform as a Service) 
- **FaaS** (Function as a Service)
- **CaaS** (Container as a Service)
- **Serverless**

Let's get on a quick **journey** to understand these!


### 3.1: What is Platform as a Service?

![](/images/aws/cloud-2-PAAS.png)

> How about cloud platform taking more responsibility?

When you are making use of PAAS (Platform as a Service), you making use of a platform provided by cloud. You will have less access to infrastructure but you will give more responsibility to the cloud provider.

Typically **Cloud provider** is responsible for:
- OS (incl. upgrades and patches)
- Application Runtime
- Auto scaling, Availability & Load balancing etc..

**You** are responsible for:
- Configuration (of Application and Services)
- Application code (if needed)

There are a variety of PaaS offerings:
- **CAAS (Container as a Service)**: Containers instead of Apps
- **FAAS (Function as a Service)**: Functions instead of Apps
- Databases - Relational & NoSQL (Amazon RDS, Google Cloud SQL, Azure SQL Database etc), Queues, AI, ML, Operations etc!

### 3.2: Why do we need Containers?

One of the popular architectural trends of the last decade is microservices.

![](/images/aws/microservice-chain.png)

In a monolith applications, you have one large deployable unit serving most features of your applications.

In a microservices architecture, you are dividing your applications into smaller, independently deployable building blocks.

Microservices architecture provides you with a **flexibility to innovate** and build applications in different programming languages (Go, Java, Python, JavaScript,  etc).

However, flexibility comes at a cost. Deployments and operations become more complex.

How can we deploy applications and services built in different languages the same way?

How can we have single way to implement observability (logs, metrics, traces, ..) for different services and applications?

Enter **Docker** and **containers**!

### 3.3: How does Docker help?

![](/images/aws/Docker-DevOps-02.png)

When you are using Docker, you build a separate **Docker image** for each microservice. 

Each Docker image **contains everything that you need to run an instance of a microservice**:
- OS
- Application Runtime (JDK or Python or NodeJS)
- Application Code
- Application Dependencies 

You can deploy and run this Docker image **the same way** (using the same process) on any infrastructure - Your local machine, a corporate data center and in the cloud (AWS, Azure or Google Cloud).

Docker simplifies development:
- You can run your Docker image anywhere - on your local machine, or on your testers machine
- You can run your database and queues (MySql, Kafka,.. etc) as a docker containers without installing them on your local machine

Docker simplifies operations:
- You deploy all microservices the same way 
- You can implement observability (logs, metrics, traces, ..)  for all microservices the same way

### 3.4: Why do we need Container Orchestration?


![](/gcpimages/02-architecture/microservices.png)

Enterprises are heading towards microservices architectures. Microservices provide the **flexibility to innovate**. 

However, microservices architectures also have complex technical requirements. Example: I want 10 instances of Microservice A container, 15 instances of Microservice B container, .. and so on for multiple microservices. In addition, I want a number of other features for my microservices. A few typical features include:
- **Auto Scaling** - Scale containers based on demand
- **Service Discovery** - Help microservices find one another
- **Load Balancer** - Distribute load among multiple instances of a microservice
- **Self Healing** - Do health checks and replace failing instances
- **Zero Downtime Deployments** - Release new versions without downtime

#### What is Container Orchestration?

Container orchestration solutions provide most technical features need by microservices architectures. You will be able to create a cluster of multiple vm instances and deploy microservices to the cluster. Container orchestration solution will manage the clusters and deployments.

![](/gcpimages/02-architecture/container-orchestration.png) 

#### What is Kubernetes?

There are a number of container orchestration platforms: Docker Swarm, Mesosphere, Kubernetes among others. In the last few years, Kubernetes has emerged as the winners in the container orchestration space.

### 3.5 What is Serverless?

What do we think about when we develop an application?
- Where to deploy?
- What kind of hardware?
- What OS?
- How do we scale?
- How do we make the app highly available?


What if you don't need to worry about servers and focus on your code. That's Serverless in a nutshell for me. 

Here are couple of very important facets of Serverless offering:
- 1: You **don't worry** about infrastructure (You have ZERO visibility into infrastructure). And you get automated scaling and high availability.
- 2: **Pay for use** - You pay for invocations and usage NOT for servers. Ideally ZERO REQUESTS => ZERO COST.

Remember: **Serverless does NOT mean "No Servers"**.  It mean you don't want to worry about servers.

Summary: **You focus on code** and the cloud managed service takes care of all that is needed to scale your code to serve millions of requests! And you pay for requests and NOT servers!

#### Are all serverless services really serverless?

Here are some of the key serverless features for me:
- 1: Zero worry about infrastructure, scaling and availability
- 2: Zero invocations => Zero Cost (Can you scale down to ZERO instances?)
- 3: Pay for invocations and NOT for instances (or nodes or servers)

When it comes to cloud services, I categorize them into:
- Serverless **Level 1**: Features (1 + 2)
- Serverless **Level 2**: Features (1 + 2 + 3)

When I refer to Serverless, I'm referring to Level 2.


However, cloud providers include managed services at Level 1 and Level 2 under the ambit of Serverless:
- **Level 1**: **Google App Engine** (Google Calls it "App Engine is a fully managed, serverless platform"), **AWS Fargate** (AWS calls it "serverless compute engine for containers"). You can scale down to ZERO instances when there is no load, **BUT** you pay for number (and type) of instances running!
- **Level 2**: **Google Functions, AWS Lambda, Azure Functions** etc. You pay for invocations.

## 4: What are the Google Cloud Compute Services?

Let's explore them one by one.

### 4.1: Google Compute Engine

Google Compute Engine is the IaaS compute offering in Google Cloud.

### 4.2: Google App Engine

Google App Engine is first cloud service introduced by Google Cloud (in 2008!).

App Engine is the **simplest way** to deploy and scale your applications in GCP. Provides end-to-end application management.

Here is a summary of important App Engine features:
- Go, Java, .NET, Node.js, PHP, Python, Ruby using pre-configured runtimes
- Use custom run-time and write code in any language
- Connect to variety of Google Cloud storage products (Cloud SQL etc)
- Automatic load balancing & Auto scaling
- Managed platform updates & Application health monitoring
- Application versioning
- Traffic splitting

#### Comparing Google Compute Engine and Google App Engine

##### **Compute Engine**

- IAAS
- MORE Flexibility
- MORE Responsibility for customer(Choosing Image, Installing Software, Choosing Hardware,  Fine grained Access/Permissions, Availability, Scaling)

##### **App Engine**

- PaaS
- Serverless
- LESSER Responsibility
- LOWER Flexibility

### 4.3: Google Kubernetes Engine

Earlier we talked about the most popular container orchestration platform - Kubernetes.

Google Kubernetes Engine is the managed Kubernetes service in Google Cloud.

It provides all the typical features expected of a container orchestration solution:
- **Auto Scaling**
- **Service Discovery**
- **Load Balancer**
- **Self Healing**
- **Zero Downtime Deployments**

I can put my neck out a bit and say "In my opinion, GKE is the best managed Kubernetes service out there".

### 4.4: Google Cloud Functions

Imagine you want to **execute some code when an event happens**?
- A file is uploaded in Cloud Storage 
- An error log is written to Cloud Logging
- A message arrives to Cloud Pub/Sub

In the cloud, Event handling is one of the best use cases for Serverless Function as a Service offerings.

Cloud Functions is the Google Serverless FaaS offering.

You can run code in response to events. Write your business logic in  Node.js, Python, Go, Java, .NET, and Ruby. **Don't worry** about servers or scaling or availability (only worry about your code).

**Pay only for what you use:**
- Number of invocations
- Compute Time of the invocations
- Amount of memory and CPU provisioned

### 4.5: Google Cloud Run

Goal of **Cloud Run** is "Container to Production in Seconds". It is built on top of an open standard - **Knative**. Cloud Run is a **Fully managed** serverless platform for containerized applications. 

Here are few of the important features:
- ZERO infrastructure management
- Pay-per-use (For used CPU, Memory, Requests and Networking)
- Easily portable because of **container** based architecture

### 4.6: Google Cloud Anthos

A number of enterprises are looking to use a mix of cloud platforms and their own data center to host their applications. (multi-cloud, poly-cloud, hybrid-cloud - whatever, you want to call it!)

Goal of **Anthos** is help you run Kubernetes clusters anywhere - Cloud, Multi Cloud and On-Premise.

You can manage multiple Kubernetes deployments centrally using Anthos.

## 5: Here is a Quick Summary

| Service | Details | Category|
|--|:--|
|Compute Engine | High-performance and general purpose VMs that scale globally | IaaS|
| App Engine  | Build highly scalable applications on a fully managed platform using open and familiar languages and tools |PaaS (CaaS, Serverless)|
| Cloud Functions  | Build event driven applications using simple, single-purpose functions |FaaS, Serverless|
| Cloud Run  | Develop and deploy highly scalable containerized applications. <BR/>Does NOT need a cluster!|CaaS (Serverless)|
| Google Kubernetes Engine  | Orchestrate containerized microservices on Kubernetes <BR/>Needs advanced cluster configuration and monitoring | Container Orchestration|
|Anthos| Run Kubernetes Clusters anywhere | Multi Cloud Container Orchestration|
