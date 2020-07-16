---
layout:     post
title:      Multi-AZ vs Multi-Region vs Read replicas - Amazon RDS - AWS Certification
date:       2020-07-15 12:31:19
summary:    Let's get a quick overview of Multi-AZ vs Multi-Region vs Read replicas for Amazon RDS from an AWS certification perspective. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-multi-az-vs-multi-region-vs-read-replicas
---

Let's get a quick overview of Multi-AZ vs Multi-Region vs Read replicas for Amazon RDS from an AWS certification perspective.

## You will learn
- What are Multi-AZ Deployments?
- What are Read replicas?
- How do you choose between Multi-AZ deployments vs Multi-Region vs Same-Region Read replicas?


## Table of Contents
- [Multi-AZ Deployments](#multi-az-deployments)
- [Read Replicas](#read-replicas)
- [RDS Multi-AZ vs Multi-Region vs Read replicas - Certification Questions and Scenarios](#rds-multi-az-vs-multi-region-vs-read-replicas---certification-questions-and-scenarios)

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Multi-AZ Deployments

![](/images/aws/rds/7-multi-az-deployment.png)

- Standby created in a different AZ
- **Synchronous replication** (strong consistency)
- Enhances durability, availability and fault tolerance of your database
- Multi-AZ makes **maintenance easy**
	- Perform maintenance (patches) on standby
	- Promote standby to primary
	- Perform maintenance on (old) primary
- **Avoid I/O suspension** when data is backed up (snapshots are taken from standby)
- No downtime when database is converted to Multi AZ
	- Increased latency until standby is ready
- Not allowed to connect to standby database directly 
	- For example: Standby CANNOT be used to serve read traffic
	- Standby increases availability but does not improve scalability
- Automatic failover to standby if master has problems (compute, storage or networking)
	- CNAME record flipped to standby
	- Database performance issues (long running queries or deadlocks) will NOT cause a failover
- (Good Practice) Use DNS name of database in applications configuration

## Read Replicas

![](/images/aws/rds/8-read-replica-deployment.png)

- Support **read-heavy database workloads** - reporting and data warehousing 
- Can be in same or different AZ or different Region
- Your apps can connect to them
- Create read replica(s) of a read replica
- Uses **asynchronous replication**
	- Provides eventual consistency (from replica)
	- For higher consistency, read from master
- Need to be **explicitly deleted** (Not deleted when database is deleted)
- (Mandatory) Enable automatic backups before you can create read replicas
	- Set Backup Retention period to a value other than 0
- Reduce replication lag by using better compute and storage resources
- Maximum no of read replicas:
	- MySQL, MariaDB, PostgreSQL, and Oracle - 5
	- Aurora - 15
	- SQL Server does not support read replicas

## RDS Multi-AZ vs Multi-Region vs Read replicas - Certification Questions and Scenarios

|Feature|Multi-AZ deployments|Multi-Region Read Replicas|Multi-AZ Read replicas|
|--|:--|:--|:--|
|Main purpose|High availability|Disaster recovery and local performance|Scalability|
|Replication|Synchronous (except for Aurora - Asynchronous)|Asynchronous|Asynchronous|
|Active|Only master (For Aurora - all)|All read replicas|All read replicas|
