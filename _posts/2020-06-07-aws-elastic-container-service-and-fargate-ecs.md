---
layout:     post
title:      Amazon Elastic Container Service and Fargate - ECS - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon Elastic Container Service and Fargate from an AWS certification perspective. We will look at important certification questions regarding AWS Elastic Container Service and Fargate. 
categories:  AWS_CLOUD AWS_COMPUTE
permalink:  /aws-certification-aws-elastic-container-service-and-fargate-ecs
---

Let's get a quick overview of AWS Elastic Container Service and Fargate from an AWS certification perspective. We will look at important certification questions regarding AWS Elastic Container Service and Fargate.

## You will learn
- What is AWS Elastic Container Service 
- What is Amazon Fargate?
- What is the difference between Amazon Elastic Container Service and Amazon Fargate?
- What is Docker?
- When do you use Containers?
- Why do we need Container Orchestration?
- What are the different options to run containers in AWS?
- When do you use Elastic Beanstalk, Amazon ECS, Amazon Fargate and Amazon EKS to run Docker Containers?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## Microservices

Elastic Container Services are ideal to run Microservices. 

Let's first understand what is a microservice.

Enterprises are heading towards microservices architectures. 

Microservices architecture focus on building small focused microservices

Advantages of microservices:
- **Flexibility to innovate** and build applications in different programming languages (Go, Java, Python, JavaScript,  etc)


![](/images/aws/microservices.png)


However **deployments become complex**!

How can we have **one way of deploying** Go, Java, Python or JavaScript .. microservices?
- Enter **containers**!

## Docker

You can create **Docker images** for each microservice.

Docker image **contains everything a microservice needs** to run:
- Application Runtime (JDK or Python or NodeJS)
- Application code
- Dependencies 

![](/images/aws/docker.png)

You can run these docker containers **the same way** on any infrastructure:
- Your local machine
- Corporate data center
- Cloud

## Docker - Advantages

Let's look at some of the advantages that Docker provides:
- Docker containers are **light weight** (compared to Virtual Machines)
- Docker provides **isolation** for containers
- Docker is **cloud neutral**


As we build more an more Docker images for our microservices, a new challenge emerges.

How do you manage 1000's of containers belonging to multiple microservices?
- Enter **Container Orchestration**!

## Container Orchestration

**Requirement** : I want 10 instances of Microservice A container, 15 instances of Microservice B container and ....

![](/images/aws/container-orchestration.png) 

Typical Features of Container Orchestrator:
- **Auto Scaling** - Scale containers based on demand
- **Service Discovery** - Help microservices find one another
- **Load Balancer** - Distribute load among multiple instances of a microservice
- **Self Healing** - Do health checks and replace failing instances
- **Zero Downtime Deployments** - Release new versions without downtime

## Container Orchestration Options
Let's look at the different options for container orchestration.

Let's start with the **Cloud Neutral** option Kubernetes. 
- AWS service - AWS Elastic Kubernetes Service (EKS)

Note: EKS does not have a free tier

**AWS Specific** options include
- AWS Elastic Container Service (ECS) 
- AWS Fargate : Serverless version of AWS ECS

Note: AWS Fargate does not have a free tier

## Amazon Elastic Container Service (Amazon ECS)

Amazon Elastic Container Service (Amazon ECS) is a fully managed service for container orchestration.

**AWS Fargate** is a serverless option.

![](/images/aws/ecs.png) 

Use cases include:
- Microservices Architectures - Create containers for your microservices and orchestrate them using ECS or Fargate
- Batch Processing. Run batch workloads on ECS using AWS Batch

## Amazon ECS - Task Definition

To manage containers using Amazon ECS, you need Tasks. 

Tasks contain **Container Definition(s)**
- What is the image you want to use? 
- What resources does the container use (memory, CPU and ports)?

![](/images/aws/ecs-concepts.png) 

Two important task related configuration to remember:
- **Task Role** (Optional): If you need access to AWS services (Amazon RDS etc)
- **Task execution IAM role**: Provides permissions to pull container images and publish container logs to Amazon CloudWatch

## Amazon ECS - Terminology

Here is the important terminology used in ECS
- **Service**:  Allows you to run and **maintain** a specified number (the "desired count") of tasks
- **ECS cluster**: Grouping of one or more container instances (EC2 instances) where you run your tasks
- **Container Instance** - EC2 instance in the cluster running a **container agent** (helps it communicate with the cluster)
	- AWS provides ECS ready AMIs with container agents pre-installed.


## Amazon Elastic Container Service - Remember

Here are a few important things to remember:
- AWS Fargate does NOT give you visibility into the EC2 instances in the cluster.
- You can use On-Demand instances or Spot instances to create your cluster.
- You can load balance using Application Load Balancers
- Two features of ALB are important for ECS:
	- **Dynamic host port mapping**: Multiple tasks from the same service are allowed per EC2 (container) instance
	- **Path-based routing**: Multiple services can use the same listener port on same ALB and be routed based on path (www.app.com/microservice-a and www.app.com/microservice-b)

## **Amazon ECR** (Elastic Container Registry)

You've created docker images for your microservices. **Where do you store them?**

You need a **Container Registry**.

**Amazon ECR** is a Fully-managed Docker container registry provided by AWS. Its an alternative to Docker Hub.

## Additional Resources for Containers

Here are a few recommended videos to watch
- Docker: https://www.youtube.com/watch?v=Rt5G5Gj7RP0
- Kubernetes: https://www.youtube.com/watch?v=rTNR7vDQDD8
- AWS Fargate and ECS: https://www.youtube.com/watch?v=2oXVYxIPs88


## AWS Elastic Container Service and Fargate - AWS Certification Questions

When do you use these services to run Docker Containers in AWS?

**Elastic Beanstalk** 
- Single container or multiple containers in same EC2 instance
- Recommended for simple web applications

**Amazon ECS** 
- AWS specific solution for container orchestration
- Ideal for microservices

**Amazon Fargate** 
- Serverless version of Amazon ECS
- You want to run microservices and you don't want to manage the cluster

**Amazon EKS** 
- AWS managed service for Kubernetes
- Recommended if you are already using Kubernetes and would want to move the workload to AWS