---
layout:     post
title:      EC2 - For Architects - Certified Associate - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of EC2 from an AWS Architects certification perspective. We will look at important certification questions regarding EC2 Architecture. 
categories:  AWS_CLOUD EC2
permalink:  /aws-certification-ec2-architects
---

Let's get a quick overview of EC2 from an AWS Architects certification perspective. We will look at important certification questions regarding EC2 Architecture. 

## You will learn
- What are the important factors about EC2 from an architecture stand point?
- How do you scale EC2 instances?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target="_blank"}


## EC2 & ELB for Architects

> It is not sufficient to get things working. We want more!

- High Availability
- High Scalability
- Improve Performance
- Improve Security
- Low Costs
- and .....

## Availability

- Are the applications available **when the users need them**?
- **Percentage of time** an application provides the operations expected of it
- **Example**: 99.99% availability. Also called four 9's availability

##### Availability Table

| Availability | Downtime (in a month)  | Comment |
|--|--|--|
| 99.95% | 22 minutes||
| 99.99% (four 9's)| 4 and 1/2 minutes | Most online apps aim for 99.99% (four 9's)|
| 99.999% (five 9's) | 26 seconds| Achieving 5 9's availability is tough|

## Availability Basics - EC2 and ELB

![](/images/aws/ec2/3-elb-crosszone-lb.png)
- Deploy to multiple AZs
- Use **Cross Zone** Load Balancing
- Deploy to multiple regions
- Configure proper EC2 and ELB **health checks**

## Scalability
- A system is handling 1000 transactions per second. Load is expected to increase 10 times in the next month
	- Can we handle a **growth in users, traffic, or data size** without any drop in performance?
	- Does ability to serve more growth increase **proportionally** with resources?
- Ability to **adapt** to changes in demand (users, data)
- What are the options that can be considered?
	- Deploy to a bigger instance with bigger CPU and more memory
	- Increase the number of application instances and setup a load balancer
	- And a lot more.

## Vertical Scaling

![](/images/vertical-scaling.png) 
- Deploying application/database to **bigger instance**: 
	- A larger hard drive 
	- A faster CPU
	- More RAM, CPU, I/O, or networking capabilities
- There are limits to vertical scaling

## Vertical Scaling for EC2
![](/images/aws/ec2-vertical-scaling.png) 
- Increasing **EC2 instance size**:
	- *t2.micro* to *t2.small* or 
	- *t2.small* to *t2.2xlarge* or 
	-  ...

## Horizontal Scaling
![](/images/horizontal-scaling.png) 
- Deploying multiple instances of application/database
- (Typically but not always) Horizontal Scaling is preferred to Vertical Scaling:
	- Vertical scaling has limits
	- Vertical scaling can be expensive
	- Horizontal scaling increases availability
- (BUT) Horizontal Scaling needs additional infrastructure:
	- Load Balancers etc.

## Horizontal Scaling for EC2
![](/images/aws/ec2/3-elb-crosszone-lb.png)

- Distribute EC2 instances 
	- in a single AZ
	- in multiple AZs in single region
	- in multiple AZs in multiple regions
- **Auto scale**: Auto Scaling Group
- **Distribute load** : Elastic Load Balancer, Route53
