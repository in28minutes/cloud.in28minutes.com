---
layout:     post
title:      Managed Services - IAAS vs PAAS - Shared Responsibility - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Managed Services - IAAS and PAAS - from an AWS certification perspective. We will look at important certification questions regarding Managed Services - IAAS and PAAS. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-managed-services-iaas-paas
---

Let's get a quick overview of Managed Services - IAAS and PAAS - from an AWS certification perspective. We will look at important certification questions regarding Managed Services - IAAS and PAAS. 

## You will learn
- What is IAAS(Infrastructure as a Service) ?
- What is PAAS (Platform as a Service) ?
- What are the different Managed Services provided by AWS?
- What is Shared Responsibility Model?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## IAAS (Infrastructure as a Service) 

IAAS (Infrastructure as a Service) is all about using **only infrastructure** from cloud provider. It is also called "**Lift and Shift**". **Example**: Using EC2 to deploy your applications or databases

With IAAS, you are responsible for:
- Application Code and Runtime
- Configuring load balancing
- Auto scaling
- OS upgrades and patches
- Availability
- etc.. ( and a lot of things!)

![](/images/aws/cloud-0-IAAS.png)


## PAAS (Platform as a Service) 

PAAS (Platform as a Service) is all about using a platform provided by cloud

**Cloud provider** is responsible for:
- OS (incl. upgrades and patches)
- Application Runtime
- Auto scaling, Availability & Load balancing etc..

**You** are responsible for:
- Application code
- Configuration

![](/images/aws/cloud-2-PAAS.png)

Examples of PAAS
- **CAAS (Container as a Service)**: Containers instead of Applications
- **FAAS (Function as a Service)** or **Serverless**: Functions instead of Applications

## AWS Managed Service Offerings

Here are some of the AWS Managed Service Offerings:
- **Elastic Load Balancing** - Distribute incoming traffic across multiple targets
- **AWS Elastic Beanstalk** - Run and Manage Web Apps
- **Amazon Elastic Container Service (ECS)** - Containers orchestration on AWS
- **AWS Fargate** - Serverless compute for containers
- **Amazon Elastic Kubernetes Service (EKS)** - Run Kubernetes on AWS
- **Amazon RDS** - Relational Databases - MySQL, Oracle, SQL Server etc
- And a lot more...

![](/images/aws/00-icons/elb.png)
![](/images/aws/00-icons/ecs.png) 
![](/images/aws/00-icons/rds.png)

## Shared Responsibility Model

Security & Compliance is shared responsibility between AWS and customer

## Shared Responsibility Model - Amazon EC2
![](/images/aws/00-icons/ec2.png) 
![](/images/aws/00-icons/securitygroup.png) 
![](/images/aws/00-icons/ami.png) 
Amazon EC2 instances is Infrastructure as a Service (IaaS).

You are responsible for:
- Guest OS (incl. security patches)
- Application software installed
- Configuring Security Groups (or firewalls)

AWS is responsible for infrastructure layer only.

## Shared Responsibility Model - Managed Services

![](/images/aws/00-icons/s3.png) 
![](/images/aws/00-icons/dynamodb.png) 
Amazon S3 & DynamoDB are managed services.

AWS manages infrastructure layer, OS, and platform.

You are responsible for
- Managing your data 
- Managing security of data at rest(encryption) 
- Managing security of data in transit 
	- Mandating SSL/HTTPS 
	- Using the right network - AWS global network or dedicated private network when possible
- Managing access to the service
	- Configure right permissions (IAM users/roles/user policies/resource policies)
	- (FOR AWS RDS) Managing in database users 
	- Configuring the right security groups (control inbound and outbound traffic)
	- Disabling external access (public vs private)
