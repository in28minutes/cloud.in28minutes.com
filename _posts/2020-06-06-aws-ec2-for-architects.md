---
layout:     post
title:      EC2 Elastic Compute Cloud - For Architects - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of EC2 from an AWS Architects certification perspective. We will look at important certification questions regarding EC2 Architecture. 
categories:  AWS_CLOUD EC2
permalink:  /aws-certification-ec2-architects
---

Let's get a quick overview of EC2 from an AWS Architects certification perspective. We will look at important certification questions regarding EC2 Architecture. 

## You will learn
- What are the important factors about EC2 from an architecture stand point?
- How do you scale EC2 instances?

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>


## EC2 & ELB for Architects

It is not sufficient to get things working. We want more!

- High Availability
- High Scalability
- Improve Performance
- Improve Security
- Low Costs
- and .....

We want all these for our architectures using EC2 and ELB services.

Let's start with understanding the basics of Availability.

## Availability

Availability is all about this question - Are the applications available **when the users need them**?

It is the **Percentage of time** an application provides the operations expected of it

**Example**: 99.99% availability. Also called four 9's availability

### Availability Table

Here's a table showing availability and the downtime mapping:

| Availability | Downtime (in a month)  | Comment |
|--|--|--|
| 99.95% | 22 minutes||
| 99.99% (four 9's)| 4 and 1/2 minutes | Most online apps aim for 99.99% (four 9's)|
| 99.999% (five 9's) | 26 seconds| Achieving 5 9's availability is tough|

### Availability Basics - EC2 and ELB

Here are some of the options to make EC2 instances highly available:
- Deploy to multiple AZs
- Use **Cross Zone** Load Balancing
- Deploy to multiple regions
- Configure proper EC2 and ELB **health checks**

The diagram below shows a simple example.

![](/images/aws/ec2/3-elb-crosszone-lb.png)


## Scalability

Let's consider a scenario: A system is handling 1000 transactions per second. Load is expected to increase 10 times in the next month. 

Two important questions to ask
- Can we handle a **growth in users, traffic, or data size** without any drop in performance?
- Does ability to serve more growth increase **proportionally** with resources?

> Scalability is the ability to **adapt** to changes in demand (users, data).

For EC2 instances, we can:
- Deploy to a bigger instance with bigger CPU and more memory
- Increase the number of application instances and setup a load balancer

Let's look at the two types of scalability:
- Vertical Scalability
- Horizontal Scalability

### Vertical Scaling

Vertical Scaling is all about deploying application/database to **bigger instance**: 
- A larger hard drive 
- A faster CPU
- More RAM, CPU, I/O, or networking capabilities

![](/images/vertical-scaling.png) 

There are limits to what you can achieve with vertical scaling.

#### Vertical Scaling for EC2

What does Vertical Scaling for EC2 instances look like?
- Increasing **EC2 instance size**:
	- *t2.micro* to *t2.small* or 
	- *t2.small* to *t2.2xlarge* or 
	-  ...

![](/images/aws/ec2-vertical-scaling.png) 

### Horizontal Scaling

Horizontal Scaling is all about deploying multiple instances of application/database.

![](/images/horizontal-scaling.png) 

Horizontal Scaling is preferred to Vertical Scaling due to following reasons:
- Vertical scaling has limits
- Vertical scaling can be expensive
- Horizontal scaling increases availability

However, Horizontal Scaling needs additional infrastructure:
	- Load Balancers etc.

#### Horizontal Scaling for EC2

How can you implement Horizontal Scaling for EC2 instances?

Here are some of the options:
- Distribute EC2 instances 
	- in a single AZ
	- in multiple AZs in single region
	- in multiple AZs in multiple regions
- **Auto scale**: Auto Scaling Group
- **Distribute load** : Elastic Load Balancer, Route53

![](/images/aws/ec2/3-elb-crosszone-lb.png)

## Architecture Considerations for EC2 and ELB (Certification Exam)

Here are some the Architecture Considerations for EC2 and ELB:

##### Security
- Use **Security Groups** to restrict traffic
- Place EC2 instances in **private subnets**
- Use **Dedicated Hosts** when you have regulatory needs

##### Performance
- Choose right **instance family** (Optimized combination of compute, memory, disk (storage) and networking)
- Use appropriate placement groups
- Prefer creating an **custom AMI** to installing software using userdata

##### Cost Efficiency
- Have optimal **number and type** of EC2 instances running
- Use the **right mix** of:
	- Savings Plans
	- Reserved Instances
	- On demand Instances
	- Spot Instances

##### Resiliency
- Configure the right **health checks**
- Use CloudWatch for monitoring
- **(Disaster recovery)** Upto date AMI copied to multiple regions