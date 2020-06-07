---
layout:     post
title:      Elastic Block Storage vs Instance Store - EBS - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Block Storage options in AWS - Elastic Block Storage - EBS and Instance Store. We will look at important certification questions regarding EBS vs Instance Store. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-ebs-vs-instance-store-ebs
---

Let's get a quick overview of Block Storage options in AWS - Elastic Block Storage - EBS and Instance Store. We will look at important certification questions regarding EBS vs Instance Store.

## You will learn
- What is Elastic Block Storage (EBS)?
- What is an Instance Store?
- When do you use EBS vs Instance Store?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## EC2 - Block Storage

![](/images/aws/001-basic-drawings/02-storage-types.png)
- Two popular types of block storage can be attached to EC2 instances:
	- **Elastic Block Storage (EBS)**
	- **Instance Store** 
- **Instance Stores** are physically attached to the EC2 instance
	- Temporary data
	- Lifecycle tied to EC2 instance
- **Elastic Block Storage (EBS)** is network storage
	- More durable
	- Lifecycle NOT tied to EC2 instance

## Instance Store

![](/images/aws/001-basic-drawings/03-storage-types.png)
- **Physically attached** to your EC2 instance
- **Ephemeral storage** 
	- Temporary data. 
	- Data is lost when hardware fails or an instance is terminated.
	- Use case: cache or scratch files
- **Lifecycle is tied** to EC2 instance
- Data is **NOT lost** on instance reboot
- Only some of the EC2 instance types support **Instance Store**

## Instance Store - Advantages and Disadvantages

![](/images/aws/001-basic-drawings/03-storage-types.png)

- **Advantages**
	- Very Fast I/O (2-100X of EBS)
	- (Cost Effective) **No extra cost**. Cost is included in the cost of EC2 instance
	- Ideal for storing **temporary information** - cache, scratch files etc
- **Disadvantages**
	- **Slow boot up** (up to 5 minutes)
	- **Ephemeral storage** (data is lost when hardware fails or instance is terminated)
	- **CANNOT take a snapshot** or restore from snapshot
	- Fixed size based on instance type
	- You cannot detach and attach it to another EC2 instance

## Amazon Elastic Block Storage (EBS)

![](/images/aws/001-basic-drawings/04-ebs.png)
- **Network block storage** attached to your EC2 instance
- **Provisioned capacity**
- Very flexible. 
	- **Increase size when you need it** - when attached to EC2 instance
- Independent lifecycle from EC2 instance
	- Attach/Detach from one EC2 instance to another
- 10X more durable compared to an usual hard disk (annual failure rate of 0.1% - 0.2%)
- *99.999% Availability* & replicated within the same AZ
- **Use case** : Run your custom database

## Amazon EBS vs Instance Store

|Feature|Elastic Block Storage (EBS)|Instance Store|
|--|:--|:--|
|Attachment to EC2 instance|As a network drive|Physically attached|
|Lifecycle|Separate from EC2 instance|Tied with EC2 instance|
|Cost| Depends on provisioned size|Zero (Included in EC2 instance cost)|
|Flexibility| Increase size| Fixed size|
|I/O Speed| Lower (network latency) | 2-100X of EBS|
|Snapshots| Supported | Not Supported|
|Use case| Permanent storage| Ephemeral storage|
|Boot up time| Low| High|
