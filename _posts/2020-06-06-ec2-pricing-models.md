---
layout:     post
title:      EC2 - Pricing Models - On Demand vs Spot vs Reserved vs Savings Plans - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of EC2 Pricing Models from an AWS certification perspective. We will look at important certification questions regarding EC2 Pricing Models - On Demand vs Spot vs Reserved vs Savings Plans. 
categories:  AWS_CLOUD EC2
permalink:  /aws-certification-ec2-pricing-models
---

Let's get a quick overview of EC2 Pricing Models from an AWS certification perspective. We will look at important certification questions regarding EC2 Pricing Models - On Demand vs Spot vs Reserved vs Savings Plans.

## You will learn
- Why is pricing of EC2 instances important?
- What are the different EC2 pricing models offered by AWS?
- How do they compare - On Demand vs Spot vs Reserved vs Savings Plans?
- How do you choose - On Demand vs Spot vs Reserved vs Savings Plans?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>



## EC2 Pricing Models Overview

| Pricing Model | Description  | Details|
|--|--|--|
| On Demand | Request when you want it | Flexible and Most Expensive|
| Spot      | Quote the maximum price  | Cheapest (upto 90% off) BUT NO Guarantees |
| Reserved  | Reserve ahead of time  | Upto 75% off. 1 or 3 years reservation. |
| Savings Plans | Commit spending $X per hour on (EC2 or AWS Fargate or Lambda)| Upto 66% off. No restrictions. 1 or 3 years reservation.|

## EC2 On-Demand

![](/images/aws/ec2-host.png) 
![](/images/aws/ec2-host.png) 
- On demand resource provisioning - **Use and Throw**!
- Highest cost and highest flexibility
- This is what we have been using until now in this course
- **Ideal for**:
	- A web application which receives spiky traffic
	- A batch program which has unpredictable runtime and cannot be interrupted
	- A batch program being moved from on-premises to cloud for the first time

## EC2 Spot instances
- **(Old Model)** Bid a price. Highest bidder wins
- **(New Model)** Quote your maximum price. Prices decided by long term trends. 
- Up to 90% off (compared to On-Demand)
- Can be terminated with a **2 minute** notice
- Ideal for **Non time-critical workloads** that can **tolerate interruptions** (fault-tolerant)
	- A batch program that does not have a strict deadline AND can be stopped at short notice and re-started
- (Best Practice) Stop or Hibernate EC2 instance on receiving interruption notice

## EC2 Spot Block and Spot Fleet

##### Spot Block 
- Request Spot instances for a **specific duration** (1 or 2 or .. or 6 hours) 
- For jobs that take finite time to complete

##### Spot Fleet 
- Request spot instances across a **range of instance types**
- The more instance types that you specify, the better your chances of having your target capacity fulfilled

## EC2 Linux Spot Instances - Pricing
- ZERO charge if terminated or stopped by Amazon EC2 in the first instance hour
- Otherwise you are charged by second
- Examples:
	- If EC2 terminates spot instance after 50 minutes, you pay ZERO
	- If you terminate spot instance after 50 minutes, you pay for 50 minutes
	- If either EC2 or you yourselves terminate spot instance after 70 minutes, you pay for 70 minutes

## EC2 Spot Instances - Remember
- Spot instances can be terminated, stopped, or hibernated when interrupted
	- Default - terminated
	- Use **maintain option** while creating spot request for stop and hibernate options
	- Hibernating a Spot instance allows you to save state of EC2 instances and **quickly start up**
- To **completely close** a spot request:
	- Step 1. Cancel Spot Request
	- Step 2. Terminate all Spot Instances
	- **(Remember)** Canceling a spot request might not terminate active spot instances

## EC2 Reserved Instances
- Reserve EC2 instances ahead of time!
- **Three types** of reserved instances:
	- Standard
	- Convertible
	- Scheduled
- **Payment models**:
	- No Upfront - $0 upfront. Pay monthly installment. 
	- Partial Upfront - $XYZ upfront. Pay monthly installment
	- All Upfront - Full amount upfront. $0 monthly installment. 
	- **Cost wise** : Earlier you pay, more the discount. All Upfront <  Partial Upfront < No Upfront
	- A difference upto 5%

## EC2 Standard Reserved Instances
- **Commitment** : (In a region) I reserve an EC2 instance with a **specific platform**(for example, Linux), a **specific instance type**(for example, t2.micro) for a term of **1 year** or **3 years**
- You can switch to other instance sizes within the same instance family (t2.large to t2.xlarge)
- You can switch Availability Zones
- You **CANNOT** change instance families, operating systems, or tenancies (default or dedicated)

## EC2 Convertible Reserved Instances
- **Commitment** : (In a region) I reserve an EC2 instance for a term of **1 year** or **3 years**
- You **can change** instance families, operating systems, or tenancies (default or dedicated)
- You can switch Availability Zones and instance size

## EC2 Scheduled Reserved Instances
- Commitment : (In a region) I reserve an EC2 instance part-time for a year - **X hours every month/week/day** at a specific time ZZ:ZZ
- (Restriction) Only available for a **few instance types** (ex: C3, C4, M4, R3) **in a few regions** (ex: US East (N. Virginia), US West (Oregon), Europe (Ireland))
- (Use case) Bills are generated on the first day of the month
- (Use case) A batch program runs for a few hours every day
- (Use case) Weekend batch program runs for a few hours every week

## EC2 Reserved Instances - Summary
- Standard: Commit for a EC2 platform and instance family for 1 year or 3 years. (Up to 75% off)
- Convertible: Standard + **flexibility** to change EC2 platform and instance family. (Up to 54% off)
- Scheduled: Reserve for **specific time period** in a day. (5% to 10% off)
- You can **sell reserved instances** on the AWS Reserved instance marketplace if you do not want to use your reservation

## EC2 Compute Savings Plans
- **Commitment** : I would spend X dollars per hour on AWS compute resources (Amazon EC2 instances, AWS Fargate and/or AWS Lambda) for a 1 or 3 year period
- Up to 66% off (compared to on demand instances)
- Provides **complete flexibility**: 
	- You can change instance family, size, OS, tenancy or AWS Region of your Amazon EC2 instances
	- You can switch between Amazon EC2, AWS Fargate and/or AWS Lambda

## EC2 Instance Savings Plans 
- **Commitment** : I would spend X dollars per hour on Amazon EC2 instances of a specific instance family (General Purpose, for example) within a specific region (us-east-1, for example)
- Up to 72% off (compared to on demand instances)
- You can switch operating systems (Windows to Linux, for example)

## EC2 Pricing Models - Quick Review for Certification Exam
> https://www.ec2instances.info/

| Pricing Model | Usecases  | 
|--|--|
| On Demand | Spiky workloads. | 
| Spot      | Cost sensitive, Fault tolerant, Non immediate workloads. | 
| Reserved  | Constant workloads that run all the time. |
| Savings Plans | Constant workloads that run all the time and you want more flexibility.| 
