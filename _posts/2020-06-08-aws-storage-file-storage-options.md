---
layout:     post
title:      Amazon EFS vs FSx for Lustre vs FSx Windows File Servers - File Storage - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of File Storage options in AWS - Amazon EFS vs FSx for Lustre vs FSx Windows File Servers. We will look at important certification questions regarding Amazon EFS vs FSx for Lustre vs FSx Windows File Servers. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-file-storage-amazon-efs-vs-fsx-for-lustre-vs-fsx-windows
---

Let's get a quick overview of File Storage options in AWS - Amazon EFS vs FSx for Lustre vs FSx Windows File Servers. We will look at important certification questions regarding Amazon EFS vs FSx for Lustre vs FSx Windows File Servers. 

## You will learn
- What is file storage?
- What are the file storage options in AWS?
- How do these compare - Amazon EFS vs FSx for Lustre vs FSx Windows File Servers?
- Why do we use -  Amazon EFS vs FSx for Lustre vs FSx Windows File Servers?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target="_blank"}

## File Storage	
![](/images/aws/001-basic-drawings/02-storage-types-file.png)
- Media workflows need huge shared storage for supporting processes like video editing
- Enterprise users need a quick way to share files in a secure and organized way
- These file shares are shared by several virtual servers

## AWS  File Storage
![](/images/aws/00-icons/efs.png)
- **File Storage**:
	- Amazon EFS (for Linux instances)
	- Amazon FSx Windows File Servers 
	- Amazon FSx for Lustre (high performance use cases)

## Amazon EFS

![](/images/aws/001-basic-drawings/efs.png)
- **Petabyte scale, Auto scaling** shared file storage
	- POSIX compliant
	- Supports **NFS v4.0** and **v4.1** protocols
- Pay for use 
- High availability and durability across AZs in one region
- Compatible with Amazon EC2 Linux-based instances
	- Share with thousands of Amazon EC2 instances
	- Use **Max I/O Mode** for higher throughput (with a small increase in latency for all file operations)
- **Use cases** :  home directories, file share, media workflows and content management

## Amazon FSx for Lustre
- File system **optimized for performance**
	- For high performance computing (HPC), machine learning, and media processing use cases
	- Sub-millisecond latencies, up to hundreds of gigabytes per second of throughput, and up to millions of IOPS
- Integrates with Amazon S3 
	- Process data sets directly stored in S3
- POSIX-compliant 
	- Connect Linux-based applications without having to make any changes
- File system data is automatically encrypted at-rest and in-transit

## Amazon FSx Windows File Servers
- Fully managed Windows file servers 
- Uses Service Message Block (SMB) protocol
- Accessible from Windows, Linux and MacOS instances
- Integrates with Microsoft Active Directory (AD) to support Windows-based environments and enterprises.
- Offers single-AZ and multi-AZ deployment options, SSD and HDD storage options, and provides fully managed backups.
- File system data is automatically encrypted at rest and in transit.
- (Remember) All File Sharing options are accessible on AWS or on premises

## Review of storage options

| Type    | Examples                            | Latency         | Throughput | Shareable |
|--|--|--|--|
|  Block  |  EBS, Instance Store                |  Lowest         | Single  | Attached to one instance at a time. Take snapshots to share.|
|  File   |  EFS, FSx Windows, FSx for Lustre   | Low             | Multiple | Yes |
|  Object | S3                                  |  Low            | Web Scale | Yes|
|  Archival| Glacier                            | Minutes to hours| High | No|
