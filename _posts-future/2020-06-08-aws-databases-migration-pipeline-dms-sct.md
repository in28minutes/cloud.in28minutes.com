---
layout:     post
title:      Migrating databases in AWS - Data Pipeline vs DMS vs SCT - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of different options in migrating databases from/to AWS - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-migrating-databases-in-aws-data-pipeline-vs-dms-vs-sct
---

Let's get a quick overview of different options in migrating databases from/to AWS - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT.

## You will learn
- What is different options in migrating databases from/to AWS?
- Comparison - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT
- When to use - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## AWS Data Pipeline
![](/images/aws/01-S3/9-datapipeline.png)
- Process and move data (ETL) between S3, RDS, DynamoDB, EMR, On-premise data sources
- Create complex data processing workloads that are fault tolerant, repeatable, and highly available
- Launches required resources and tear them down after execution
- REMEMBER : NOT for streaming data!

## AWS Database Migration Service
![](/images/aws/00-icons/datacenter.png)
![](/images/arrow.png)
![](/images/aws/00-icons/aws.png)

- Migrate databases to AWS while keeping source databases operational
	- Homogeneous Migrations (ex: Oracle to Oracle)
	- Heterogeneous Migrations (ex: Oracle to Amazon Aurora, MySQL to Amazon Aurora)
- Free for first 6 months when migrating to  Aurora,  Redshift or  DynamoDB
- (AFTER MIGRATION) Keep databases in sync and pick right moment to switch
- (Use case) Consolidate multiple databases into a single target database
- (Use case) Continuous Data Replication can be used for Disaster Recovery

## AWS Schema Conversion Tool

![](/images/aws/00-icons/database.png) 

- Migrate data from commercial databases and data warehouses to open source or AWS services
	- Preferred option for migrating data warehouse data to Amazon Redshift
- Migrate database schema (views, stored procedures, and functions) to compatible targets
- Features:
	- SCT assessment report 
		- Analyze a database to determine the conversion complexity
	- Update source code (update embedded SQL in code)
	- Fan-in (multiple sources - single target) 
	- Fan-out (single source - multiple targets)

## Database Migration Service VS Schema Conversion Tool
![](/images/aws/00-icons/datacenter.png)
![](/images/arrow.png)
![](/images/aws/00-icons/aws.png)
- (Remember) SCT is part of DMS service
- DMS is preferred for homogeneous migrations
- SCT is preferred when schema conversion are involved
- DMS is for smaller workloads (less than 10 TB) 
- SCT preferred for large data warehouse workloads
	- Prefer SCT for migrations to Amazon Redshift
- Only DMS provides continuous data replication after migration