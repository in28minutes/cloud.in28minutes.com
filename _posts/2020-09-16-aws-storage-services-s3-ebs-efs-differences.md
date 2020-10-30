---
layout:     post
title:      AWS Storage Services - A Comparison - AWS Certification
date:       2020-09-16 22:25:00
summary:    Let us understand the differences between different AWS storage services.
categories:  AWS_CLOUD AWS_STORAGE_SERVICES
permalink:  /aws-storage-services-s3-ebs-efs-differences
---

# Difference between AWS Storage Services

Greetings from [in28minutes.com](https://courses.in28minutes.com/). 

In this read, we will take a good look at some of the differences between different AWS Storage Services i.e. S3, EBS, and EFS. Let's get started.


| Attributes |Amazon S3  | Amazon EBS| Amazon EFS |
|--|--|--|--|
|  |Stands for *Simple storage service*  |Stands for *Elastic block store*|Stands for *Elastic file system* |
| **Storage type**  |Object storage that can store any kind of data in any format  |Persistent block-level storage for the EC2 instances|POSIX compliant file storage system for the EC2 instances |
|**Feature(s)**  |Accessible to anyone or any service with the rightful permissions  |Best for workloads that require lowest latency data access from the single EC2 instance|Provides a file system interface and concurrent accessible storage for the multiple EC2 instances |
| **Maximum storage size** | Unlimited  | 16 TiB for single volumne|Unlimited system size |
| **Maximum file size** | Single S3 object can range in size from a minimum of 0 bytes to a maximum of 5 TB  |Equivalent to the maximum size of the volumes|47.9 TiB for a single file |
| **Scalability** |Highly scalable  |Can manually increase or decrease the memory size. We can attach and detach additional volumes to and from EC2 instances to offer scalability|Elastic in nature and can automatically increase or decrease as we add or remove files |
|**Availability**  |S3 standard - 99.99%, S3 standard IA - 99.9%, S3 OneZone IA - 99.5% |Has an availability of 99.99%|Offers no service level agreement and runs in multiple availability zones |
| **Encryption methods** |Supports SSL end-points using HTTPS, Client-side and Service side encryption (such as SSE-S3, SSE-C, or SSE-KMS)  |Encryptes both data at rest and in transit through the EBS encryption that uses AWS Key management service - Client management keys|Encryptes both data at rest by using AWS key management service and in transit by using TLS 1.2 |
|**Durability**  |Stored across multiple availability zones and offers the durability of 99.999999999%  |Stored in a single availability zone|Stored in multiple availability zones |
|**Access control**  |Uses bucket policies and IAM user policies. Has the *Block Public Access* feature to manage the global access to the bucket object(s)  |IAM roles, policies, or Security groups|Resources that can access the mount point can access the file system |
|**Backup and restoration**  |Offers to version or cross-region replication  |Offers durable snapshot capabilities|Offer EFS to EFS replication through AWS DataSync service or any third party tools |
| **Real-time example(s)** |Best for web serving and content management media, backups, data lake, or big-data analytics  |Suitable for boot volumes, transaction and NoSQL databases, data warehousing, and ETL operations| Best for database backups, containers, storage sets, web serving, etc.|
| **Pricing** |Based on the S3 bucket location  |We pay a per-GB month of provisioned storage| We pay based on the amount of file system storage per month|

Good luck and Happy learning! 

Feel free to share it with your friends/colleagues.
