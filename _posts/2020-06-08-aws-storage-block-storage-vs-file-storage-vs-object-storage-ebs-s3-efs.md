---
layout:     post
title:      Block Storage vs File Storage vs Object Storage - EBS, EFS and S3 - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Block Storage, File Storage and Object Storage options in AWS. We will look at important certification questions regarding Block Storage vs File Storage vs Object Storage. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-block-storage-vs-file-storage-vs-object-storage-ebs-s3-efs
---

Let's get a quick overview of Block Storage vs File Storage vs Object Storage from an AWS certification perspective. We will look at important certification questions regarding Block Storage vs File Storage vs Object Storage.

## You will learn
- What is Block Storage?
- What is File Storage?
- What is Object Storage?
- Compare Block Storage vs File Storage vs Object Storage

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}

## Object Storage - Key Value Example

![](/images/aws/s3-folder-structure.png)

| Key                 |         Value        |
|:--:|:--:|
| 2030/course0.png    | image-binary-content |
| 2030/10/course1.png | image-binary-content |
| 2030/10/course2.png | image-binary-content |
| 2030/11/course2.png | image-binary-content |
| 2030/11/course3.png | image-binary-content |


## Object Storage - Amazon S3 (Simple Storage Service)
![](/images/aws/00-icons/s3.png)
- **Most popular, very flexible & inexpensive** storage service
- Store large objects using a **key-value** approach
- Also called **Object Storage**
- Provides REST API to access and modify objects
- **Store all file types** - text, binary, backup & archives:
	- Media files and archives
	- Application packages and logs
	- Backups of your databases or storage devices
	- Staging data during on-premise to cloud database migration

## Storage Types - Block Storage and File Storage
![](/images/aws/001-basic-drawings/01-storage-types.png)
- What is the type of storage of your hard disk?
	- **Block Storage**
- You've created a file share to share a set of files with your colleagues in a enterprise. What type of storage are you using?
	- **File Storage**

## Block Storage

![](/images/aws/001-basic-drawings/02-storage-types-block.png)
- Use case: Harddisks attached to your computers
- Typically, ONE Block Storage device can be connected to ONE virtual server
- HOWEVER, you can connect multiple different block storage devices to one virtual server
- Used as:
	- **Direct-attached storage (DAS)** - Similar to a hard disk
	- **Storage Area Network (SAN)** - High-speed network connecting a pool of storage devices
		- Used by Databases - Oracle and Microsoft SQL Server

## File Storage	

![](/images/aws/001-basic-drawings/02-storage-types-file.png)
- Media workflows need huge shared storage for supporting processes like video editing
- Enterprise users need a quick way to share files in a secure and organized way
- These file shares are shared by several virtual servers

## AWS - Block Storage and File Storage
![](/images/aws/00-icons/efs.png)
![](/images/aws/00-icons/ebs.png) 
- **Block Storage**:
	- Amazon Elastic Block Store (EBS)
	- Instance store
- **File Storage**:
	- Amazon EFS (for Linux instances)
	- Amazon FSx Windows File Servers 
	- Amazon FSx for Lustre (high performance use cases)