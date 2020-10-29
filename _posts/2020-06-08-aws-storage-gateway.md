---
layout:     post
title:      AWS Storage Gateway - File vs Tape vs Volume - Stored vs Cached - AWS Certification Cheat Sheet
date:       2020-09-21 00:31:19
summary:    Let's get a quick overview of AWS Storage Gateway from an AWS certification perspective. We will look at important certification questions regarding AWS Storage Gateway. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-aws-storage-gateway
---

Let's get a quick overview of AWS Storage Gateway from an AWS certification perspective. We will look at important certification questions regarding AWS Storage Gateway.


## You will learn
- What is AWS Storage Gateway?
- Why do we need AWS Storage Gateway?
- How is AWS Storage Gateway different from?
- Compare Storage Gateway Options - AWS Storage File Gateway vs  AWS Storage Tape Gateway vs  AWS Storage Volume Gateway

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## AWS Storage Gateway

![](/images/aws/01-S3/5-Storage-Gateway.png)

- **Hybrid storage** (cloud + on premise)
- Unlimited cloud storage for on-premise software applications and users with good performance
- (Remember) Storage Gateway and S3 Glacier **encrypt data** by default
- **Three Options**
	- AWS Storage File Gateway
	- AWS Storage Tape Gateway
	- AWS Storage Volume Gateway
- VM image with AWS Storage Gateway software deployed on-premises

## AWS Storage File Gateway

![](/images/aws/storage-gateway-file-gateway.png)

- **Problem Statement**: Large on-premise file share with terabytes of data
	- Users put files into file share and applications use the files
	- Managing it is becoming expensive
	- Move the file share to cloud without performance impact
- AWS Storage File Gateway provides cloud storage for your file shares
	- Files **stored** in **Amazon S3 & Glacier**
	- Supports **Network File System (NFS)** and **Server Message Block (SMB)**

## AWS Storage File Gateway

![](/images/aws/01-S3/6-FileGateway.png)

- File gateway **deployed as virtual machine** on-premises 
	- Maintains a local cache with most recently used objects
- Benefits from **S3 features**
	- High durability, low-cost, lifecycle management and cross-region replication
- Benefits from **S3 integrations** 
	- Data analytics and machine learning applications using Amazon EMR or Amazon Athena
- Each file gateway supports **up to 10 bucket shares**

## AWS Storage Tape Gateway

![](/images/aws/storage-gateway-tape-gateway.png)

- Tape backups used in enterprises (archives)
	- Stored off-site - expensive, physical wear and tear
- **AWS Storage Tape Gateway** - Avoid physical tape backups 
- **No change needed** for tape backup infrastructure
- Backup data to virtual tapes (actually, Amazon S3 & Glacier)
- Benefit from S3 features
	- encryption, high durability, low-cost, and cross-region replication
- Use **S3 lifecycle management**
	- move data to S3 Glacier and S3 Glacier Deep Archive

## AWS Storage Volume Gateway

![](/images/aws/01-S3/7-volume-gateway.png)

- **Volume Gateway** : Move block storage to cloud
- Supports iSCSI protocol
- Reduce costs 
- Automate backup and disaster recovery
- Use AWS Backup for backup and restore
- Use cases
	- Backup and disaster recovery
	- Migration of application data

## AWS Storage Volume Gateway - Cached and Stored

![](/images/aws/storage-gateway-cached-volume-gateway.png)
![](/images/aws/storage-gateway-stored-volume-gateway.png)

- **Cached** (Gateway Cached Volumes):
	- Primary Data Store - **AWS - Amazon S3**
	- **On-premise cache** stores frequently accessed data
	- Data in S3 CANNOT be accessed directly
		- Take EBS snapshots from cached volumes
- **Stored** (Gateway Stored Volumes): 
	- Primary Data Store - **On-Premises**
	- Asynchronous copy to AWS
	- Stored as EBS snapshots
		- For disaster recovery, restore to EBS volumes

## AWS Storage Gateway - Summary

- Key to look for : **Hybrid storage** (cloud + on premise)
	- File share (NFS or SMB) + Looking for S3 features and integrations => **AWS Storage File Gateway**
	- Tapes on cloud => **AWS Storage Tape Gateway**
	- Volumes on cloud (Block Storage) => **AWS Storage Volume Gateway**
		- High performance => **Stored**
		- Otherwise => **Cached**
- Needs additional setup on-premises
	- **VM image** with AWS Storage Gateway **software** deployed on-premises or on EC2 instance

