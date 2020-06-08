---
layout:     post
title:      Elastic Block Storage Types - General Purpose SSD vs Provisioned IOPS SSD vs Throughput Optimized HDD vs Cold HDD - EBS - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Elastic Block Storage Types - General Purpose SSD vs Provisioned IOPS SSD vs Throughput Optimized HDD vs Cold HDD. We will look at important certification questions regarding Elastic Block Storage Types. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-elastic-block-storage-types
---

Let's get a quick overview of Elastic Block Storage Types - General Purpose SSD vs Provisioned IOPS SSD vs Throughput Optimized HDD vs Cold HDD from an AWS certification perspective. We will look at important certification questions regarding Elastic Block Storage Types - General Purpose SSD vs Provisioned IOPS SSD vs Throughput Optimized HDD vs Cold HDD.

## You will learn
- What are the different Elastic Block Storage Types?
- How do these compare - General Purpose SSD vs Provisioned IOPS SSD vs Throughput Optimized HDD vs Cold HDD?
- When do you use HDD?
- When do you use SSD?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


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

## Hard Disk Drive vs Solid State Drive

> Amazon EBS offers HDD and SSD options! <BR/>How do you choose between them?

|Feature|HDD(Hard Disk Drive)|SSD(Solid State Drive)|
|--|:--|:--|
|Performance - IOPS| Low | High|
|Throughput| High | High|
|Great at| Large sequential I/O operations |Small, Random I/O operations &<BR/> Sequential I/O|
|Recommended for| Large streaming or big data workloads| Transactional workloads|
|Cost| Low| Expensive|
|Boot Volumes|Not Recommended| Recommended|

## Amazon Elastic Block Store (EBS) SSD Types

##### General Purpose SSD (gp2) ($$$)
- I/O performance **increases with size** - 3 IOPS/GB (min 100) upto 16,000 IOPS
- **Balance price & performance** for transactional workloads (Cost sensitive)
- **Use cases** : small/medium databases, dev/test environments, & boot volumes
- **Burst** up to 3,000 IOPS above the baseline

##### Provisioned IOPS SSD (io1) ($$$$)
- Provision IOPS you need
- Designed for **low latency transactional** workloads
- Delivers consistent performance for **random and sequential** access
- **Use cases** : large relational or NoSQL databases

## Amazon Elastic Block Store (EBS) HDD Types

![](/images/aws/00-icons/ebs.png) 

##### Throughput Optimized HDD (st1) ($$)
- For **frequently accessed, throughput-intensive sequential** workloads
- **Use cases** : MapReduce, Kafka, log processing, data warehouse, and ETL

##### Cold HDD (sc1) ($)
- Lowest Cost
- **Use cases** : infrequent data access - very low transaction databases

## Amazon Elastic Block Store (EBS) Types
|                       | Provisioned IOPS SSD | General Purpose SSD | Throughput Optimized HDD | Cold HDD |
|--|:--|:--|:--|:--|
| Volume Size           | 4 GB - 16 TB         | 1 GB - 16 TB        | 500 GB - 16 TB           | 500 GB - 16 TB |
| Max IOPS/Volume       | 64,000               | 16,000              | 500                      | 250            |
| Max Throughput/Volume | 1,000 MB/s           | 250 MB/s            | 500 MB/s                 | 250 MB/s       |
| Boot Volume | ✓          | ✓           |         X        |   X     |

## Amazon EBS Types - Summary

![](/images/aws/00-icons/ebs.png) 
- **Cold HDD**: Infrequent access usecases (minimum cost)
- **Throughput Optimized HDD**: Frequently accessed, large sequential operations with high throughput (cost sensitive)
- **General Purpose SSD**: System boot volumes and transactional workloads
- **Provisioned IOPS SSD**: Transactional workloads needing very high IOPS
