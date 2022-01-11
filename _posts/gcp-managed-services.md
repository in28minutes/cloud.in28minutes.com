---
layout:     post
title:      Managed Services in Google Cloud Platform - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Managed Services in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Managed Services in Google Cloud Platform.
categories:  GCP_General GCP_Computing_Services
permalink:  /gcp-managed-services
---
Let's get a quick overview of Managed Services in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Managed Services in Google Cloud Platform.


## You will learn

- Managed Services
- IAAS (Infrastructure as a Service)
- PAAS (Platform as a Service)
- Microservices
- Containers - Docker
- Container Orchestration
- Serverless
- GCP Managed Services for Compute


## Managed Services

![cloud](https://user-images.githubusercontent.com/57451228/148976458-b2a967e2-ffaa-4e7b-90d4-d1fee9787b5a.png)


- Do you want to continue **running applications in the cloud, the same way you run them in your data center?**
- OR **are there OTHER approaches?**
- You should **understand some terminology** used with cloud services:
  - **IaaS** (Infrastructure as a Service)
  - **PaaS** (Platform as a Service)
  - **FaaS** (Function as a Service)
  - **CaaS** (Container as a Service)
  - **Serverless**
- Let's get on a quick **journey** to understand these!


## IAAS (Infrastructure as a Service)

![cloud-0-IAAS](https://user-images.githubusercontent.com/57451228/148976626-6aa5cd7d-60d4-4d93-ae26-26ff45fe9218.png)


- Use **only infrastructure** from cloud provider
- E**xample:** Using VM to deploy your applications or databases
- You are responsible for:
  - Application Code and Runtime
  - Configuring load balancing
  - Auto scaling
  - OS upgrades and patches
  - Availability
  - etc.. ( and a lot of things!)


## PAAS (Platform as a Service)

![cloud-2-PAAS](https://user-images.githubusercontent.com/57451228/148976826-942c9485-b41c-4530-92ee-9de16fe45e38.png)



- Use a platform provided by cloud
- **Cloud provider** is responsible for:
  - OS (incl. upgrades and patches)
  - Application Runtime
  - Auto scaling, Availability & Load balancing etc..
- **You** are responsible for:
  - Configuration (of Application and Services)
  - Application code (if needed)
- Varieties:
  - **CAAS (Container as a Service):** Containers instead of Apps
  - **FAAS (Function as a Service):** Functions instead of Apps
  - Databases - Relational & NoSQL (Amazon RDS, Google Cloud SQL, Azure SQL Database etc), Queues, AI, ML, Operations etc!

## Microservices

![microservices](https://user-images.githubusercontent.com/57451228/148977045-5dfc6b40-9247-42f6-aafa-96f3304ee1db.png)


- Enterprises are heading towards microservices architectures
  - Build small focused microservices
  - **Flexibility to innovat**e and build applications in different programming languages (Go, Java, Python, JavaScript, etc)
- BUT **deployments become complex!**
- How can we have **one way of deploying** Go, Java, Python or JavaScript .. microservices?
  - Enter **containers**!


## Containers - Docker

![docker](https://user-images.githubusercontent.com/57451228/148977327-db435b47-4c63-488d-8577-dbaed5a396cf.png)


- Create **Docker images** for each microservice
- Docker image **has all needs of a microservice:**
  - Application Runtime (JDK or Python or NodeJS)
  - Application code and Dependencies
- Runs **the same way **on any infrastructure:
  - Your local machine
  - Corporate data center
  - Cloud
- Advantages
  - Docker containers are **light weight**
     - Compared to Virtual Machines as they do not have a Guest OS
  - Docker provides **isolation** for containers
  - Docker is **cloud neutral**

## Container Orchestration

![container-orchestration](https://user-images.githubusercontent.com/57451228/148977506-9804a1e6-0bf7-4904-b98c-3ab0525e5d12.png)


- **Requirement** : I want 10 instances of Microservice A container, 15 instances of Microservice B container and ....
- Typical Features:
  - **Auto Scaling** - Scale containers based on demand
  - **Service Discovery** - Help microservices find one another
  - **Load Balancer** - Distribute load among multiple instances of a microservice
  - **Self Healing** - Do health checks and replace failing instances
  - **Zero Downtime Deployments** - Release new versions without downtime

## Serverless
- What do we think about when we develop an application?
  - Where to deploy? What kind of server? What OS?
  - How do we take care of scaling and availability of the application?
- **What if you don't need to worry about servers and focus on your code?**
  - Enter **Serverless**
     - Remember: Serverless does NOT mean "No Servers"
- **Serverless for me:**
  - You **don't worry** about infrastructure (ZERO visibility into infrastructure)
     - Flexible scaling and automated high availability
  - Most Important: **Pay for use**
     - Ideally ZERO REQUESTS => ZERO COST
- **You focus on code** and the cloud managed service takes care of all that is needed to scale your code to serve millions of requests!
  - And you pay for requests and NOT servers!

## Serverless - My Perspective!
- Serverless - Important Features:
  - 1: Zero worry about infrastructure, scaling and availability
  - 2: Zero invocations => Zero Cost (Can you scale down to ZERO instances?)
  - 3: Pay for invocations and NOT for instances (or nodes or servers)
  - Serverless Level 1: Features (1 + 2)
  - Serverless Level 2: Features (1 + 2 + 3)
- When I refer to Serverless, I'm referring to Level 2
- HOWEVER cloud providers include managed services at Level 1 and Level 2:
  - **Level 1: Google App Engine (Google Calls it "App Engine is a fully managed, serverless platform"), AWS Fargate (AWS calls it "serverless compute engine for containers")**
     - Scale down to ZERO instances when there is no load, BUT you pay for number (and type) of instances running!
  - **Level 2: Google Functions, AWS Lambda, Azure Functions etc**
     - You pay for invocations

## GCP Managed Services for Compute
   
![compute-engine](https://user-images.githubusercontent.com/57451228/148978442-9e1831cc-f0be-4045-8ed4-fbe033c6dc30.png) &emsp; &emsp; ![container-engine](https://user-images.githubusercontent.com/57451228/148978450-e2352c46-408e-4d5f-8f74-e5d9dd667289.png) &emsp; &emsp; ![app-engine](https://user-images.githubusercontent.com/57451228/148978467-e15e20c3-7171-44d5-835b-c3e25623a5c8.png) &emsp; &emsp; ![functions](https://user-images.githubusercontent.com/57451228/148978484-0ff75fcf-109f-4242-b87c-1675e72c978b.png)

|Service	|Details	|Category|
|:--:|--|:--:|
|Compute Engine|	High-performance and general purpose VMs that scale globally	|IaaS|
|Google Kubernetes Engine	|Orchestrate containerized microservices on Kubernetes Needs advanced cluster configuration and monitoring|	CaaS|
|App Engine	|Build highly scalable applications on a fully managed platform using open and familiar languages and tools	|PaaS (CaaS, Serverless)|
|Cloud Functions	|Build event driven applications using simple, single-purpose functions	|FaaS, Serverless|
|Cloud Run|	Develop and deploy highly scalable containerized applications. Does NOT need a cluster!	|CaaS (Serverless)|



<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
