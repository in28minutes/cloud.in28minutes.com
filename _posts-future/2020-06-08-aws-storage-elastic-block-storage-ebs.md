---
layout:     post
title:      Elastic Block Storage Fundamentals - EBS - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Elastic Block Storage from an AWS certification perspective. We will look at important certification questions regarding Elastic Block Storage. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-elastic-block-storage-ebs
---

Let's get a quick overview of Elastic Block Storage from an AWS certification perspective. We will look at important certification questions regarding Elastic Block Storage.

## You will learn
- What is Elastic Block Storage?
- Why do we need Elastic Block Storage?
- When do we use Elastic Block Storage?
- Important EBS features - Snapshots, AMIs etc

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## EC2 - Block Storage

![](/images/aws/001-basic-drawings/02-storage-types.png)
- Two popular types of block storage can be attached to EC2 instances:
	- **Elastic Block Store (EBS)**
	- **Instance Store** 
- **Instance Stores** are physically attached to the EC2 instance
	- Temporary data
	- Lifecycle tied to EC2 instance
- **Elastic Block Store (EBS)** is network storage
	- More durable
	- Lifecycle NOT tied to EC2 instance

## Amazon Elastic Block Store (EBS)

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

## Amazon Elastic Block Store (EBS)
![](/images/aws/00-icons/volume.png)
![](/images/arrow.png)
![](/images/aws/00-icons/snapshot.png)

- Supports **live changes to volumes** without service interruptions
	- Increase size
	- Change type 
	- Increase IOPS capacity
- Take **point-in-time snapshots** of EBS volumes (stored in Amazon S3)
	- **Asynchronous process** - reduces performance but EBS volume is available
	- Snapshots cannot be accessed directly from S3
	- Use EC2 APIs to restore them to EBS volumes

## Amazon EBS Snapshots
- Snapshots are **incremental**
	- BUT you don't lose data by deleting older snapshots
	- Deleting a snapshot **only deletes data which is NOT needed** by other snapshots
	- Do not hesitate to delete unnecessary snapshots
	- All information needed to restore the active snapshots will be retained
- **Can be shared** with other AWS accounts
	- To share an encrypted snapshot, you would need to share (give permissions) to encryption keys also
- Constrained to the **created region**
	- To use in other regions, copy it
- **Fast Snapshot Restore** speeds up the process of creating volumes from snapshots
	- **Eliminates need for pre-warming** volumes created from snapshots

## Amazon EBS Encryption
![](/images/aws/00-icons/ebs.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/kms.png)
- Encryption (AES-256) is done *transparently* using **master keys from KMS**
- Turning on Encryption **automatically encrypts**:
	- **Data at rest**
		- Data volumes, boot volumes 
		- Snapshots
	- **Data in transit**
		- Between EC2 instances and EBS volume
		- Between EBS volume and EBS snapshots

## Faster I/O performance between EC2 and EBS

![](/images/aws/00-icons/ec2.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ebs.png)

 
| Option | Description  | 
|--|:--|
| Launch EC2 instances as **EBS optimized Instances**| Available on select instances <BR/> Default and free for a few instance types <BR/> Hourly fee for other instance types|
|**Enhanced networking** through Elastic Network Adapter (ENA)|Increases throughput(PPS) <BR/>Needs custom configuration|
|Use **Elastic Fabric Adapter (EFA)**|Available on select instances <BR/>NOT available on Windows EC2 instances<BR/> EFA = ENA + OS-bypass<BR/>**Ideal for** High Performance Computing (HPC) applications like weather modeling|

## EC2 Instance Lifecycle

![](/images/aws/instance_lifecycle.png)
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html

- Only EBS backend instances can be **stopped or hibernated**
- When you terminate an EC2 instance, **everything** on root device (EBS or instance store) is lost
- Hibernating **preserves RAM memory** in root EBS volume
	- Provides **quick restarts** for use cases with either long running processes or slow boot up times
- Hibernating can be done for a **max of 60 days**

## RAID
![](/images/aws/001-basic-drawings/05-raid-0.png)
- Need **higher durability** than one EBS volume? 
	- Use **RAID 1** structure
	- Same performance and storage capacity BUT **higher fault tolerance**
- Need **higher IOPS or storage** than one EBS volume?
	- Use **RAID 0** structure
	- Double the storage, IOPS and throughput BUT data lost even if one disk fails
	- Use this when **I/O performance is more important than fault tolerance**. Ex: Replicated Database

## EBS Snapshots and AMIs
![](/images/aws/00-icons/ebs.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/snapshot.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ami.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/ec2.png)
- You **can create**:
	- Snapshot from EBS volume and vice versa
	- AMI from EC2 instance and vice versa
	- AMI from root EBS volume snapshots

## Using an AMI from different AWS account or region
![](/images/aws/00-icons/ami.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ami.png)
- Scenario : You want to use an AMI belonging to a different AWS account or a different region
	- REMEMBER : AMI are restricted to a region
	- Step I (Optional) : Owner of AMI provides read permission to the AMI
	- Step II(Optional) : For encrypted AMI, owner should share the encryption keys
	- Step III : Copy the AMI into your region
	- If you do not have permission to copy an AMI but you have permission to use an AMI:
		- Create an EC2 instances from AMI
		- Create a new AMI from EC2 instance

## Amazon EBS Certification and Interview Questions - with EC2

| Scenario | Solution  | 
|--|:--|
|Can I attach an EBS volume in us-east-1a to EC2 instance in us-east-1b?|No. EBS volumes should in the same AZ as your EC2 instance|
|Can I attach multiple EBS volumes to EC2 instance?|Yes|
|Can I attach an EBS volume with two EC2 instances?|No|
|Can I switch EBS volume from EC2 instance to another?|Yes|
|Will an EBS volume be immediately available when attached to an EC2 instance?|Yes. However, by default, data is lazily loaded|
|How do you ensure that an EBS volume is deleted when EC2 instance is terminated?|Enable **Delete on Termination** on EC2 instance|
|How do you retain EBS volume even if an EBS backed EC2 instance fails?|Remember : On termination of EC2 instance all data on root volume is lost (even if it is EBS backed) <BR/>Detach the EBS volume before terminating the instance<BR/>Recover data by connecting the EBS volume to another EC2 instance|

## Amazon EBS Certification and Interview Questions - Snapshots

| Scenario | Solution  | 
|--|:--|
|How do you create an EBS volume from an EBS volume in a different AZ?|Take a snapshot <BR/> Create EBS volume from snapshot|
|How do you create an EBS volume from EBS volume in a different region?|Take a snapshot <BR/> Copy the snapshot to second region <BR/> Create EBS volume from snapshot in second region|
|What is the lowest cost option to maintain snapshots with EBS?|Store just the latest snapshot. Other snapshots can be deleted without a problem|
|How do you encrypt an unencrypted EBS volume?|Take a snapshot <BR/> Encrypt the snapshot <BR/> Create new encrypted volume from snapshot|
|How do you automate the complete lifecycle (creation, retention, and deletion) of Amazon EBS snapshots?|Use **Amazon Data Lifecycle Manager** <BR/> Reduces costs and maintenance effort|

## Amazon EBS - Summary

![](/images/aws/00-icons/ebs.png) 
- Amazon EBS vs instance store
- **Features**:
	- Highly available and durable (within the same AZ)
	- Supports live changes to volumes without service interruptions
	- Transparent encryption integration with KMS
- **Types**:
	- **Cold HDD**: Infrequent access usecases (minimum cost)
	- **Throughput Optimized HDD**: Frequently accessed, large sequential operations with high throughput (cost sensitive)
	- **General Purpose SSD**: System boot volumes and transactional workloads
	- **Provisioned IOPS SSD**: Transactional workloads needing very high IOPS
- EBS volume <-> Snapshot -> AMI
