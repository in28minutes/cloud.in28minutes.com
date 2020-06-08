---
layout:     post
title:      Amazon RedShift - Big Data in AWS - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon RedShift from an AWS certification perspective. We will look at important certification questions regarding Amazon RedShift. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-amazon-redshift
---

Let's get a quick overview of Amazon RedShift from an AWS certification perspective. We will look at important certification questions regarding Amazon RedShift.

## You will learn
- What is Amazon RedShift?
- Why do we need Amazon RedShift?
- When do we use Amazon RedShift?
- How do you do Redshift Workload Management?
- How do you design Redshift Tables?
- How do you load data into Amazon Redshift?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}

## Amazon Redshift

![](/images/aws/00-icons/redshift.png) 

- Redshift is a relational database ( tables and relationships)
- What is the need for another relational database? 
	- RDS is optimized for online transaction processing
	- It is optimized to provide a balance between both reads and write operations
- OLAP workloads have exponentially larger reads on the databases compared to writes: 
	- Can we use a different approach to design the database? 
	- How about creating a cluster and splitting the execution of the same query across several nodes? 
- Redshift is a **petabyte-scale distributed data ware house** based on PostgreSQL

## Amazon Redshift 

![](/images/aws/00-icons/redshift.png) 

- Three important characteristics of Redshift:
	- Massively parallel processing (MPP) - storage and processing can be split across multiple nodes
	- Columnar data storage
	- High data compression
- As a result
	- A single row of data might be stored across multiple nodes
	- A query to Redshift leader node is distributed to multiple compute nodes for execution
- Start with a single node configuration and scale to multi node configuration
- You can dynamically add and remove nodes

## Amazon Redshift 

![](/images/aws/00-icons/redshift.png) 
- Used for traditional ETL(Extract, Transform, Load), OLAP and Business Intelligence (BI) use cases
	- Optimized for high-performance analysis and reporting of very large datasets
- Supports standard SQL 
- Integration with data loading, reporting, mining and analytics tools
- Provides high availability and durability:
	- Automatic replication (maintains 3 copies of your data)
	- Automated backups (to S3. Default retention - 1 day. Max - 35 days)
	- Automatic recovery from any node failures

## Redshift Cluster

![](/images/aws/Redshift-NodeRelationships.png) 
https://docs.aws.amazon.com/redshift/latest/dg/images/02-NodeRelationships.png 
- One leader node and multiple compute nodes
	- Add compute nodes for more performance
	- Create a cluster subnet group to use a VPC
- One or more databases in a cluster
- Clients communicate with leader node
	- Leader node divides the query execution between compute nodes
	- No direct access to compute nodes
	

## Redshift - Designing Tables

![](/images/aws/00-icons/redshift.png) 
- Compression Encoding (optional) 
	- Let Redshift choose or configure for each column
		- Examples : Raw, Bytedict, LZO, Runlength, Text255, Text32K
	- Find the right compression encoding by running tests
- Sort Keys (optional) 
	- Data is stored in sorted order (using sort key)
	- Increase efficiency of your queries
	- Example 1 : Columns used frequently in range (year > 1995 and year < 2005) or equal (year = 2015) conditions
	- Example 2 : Join columns with other tables 
	- Example 3 : Timestamp columns if you use the most recent data frequently

## Redshift - Designing Tables - Distribution Strategy

![](/images/aws/00-icons/redshift.png) 

- How are the rows of the table distributed across compute nodes? 
	- Aim to distribute data equally across nodes and minimize data movement during query execution
- EVEN (default) - data is uniformly distributed
- KEY - based on values of one column
	- Matching values are stored close together
	- Use join columns as KEY if you want matching columns to be co-located
- ALL - entire table on all nodes
	- Used for lookup tables

## Loading Data into Amazon Redshift

| Scenario | Solution  | 
|--|:--|
|Simple |Use SQL insert queries using ODBC or JDBC|
|Efficient|Use Amazon Redshift COPY command to load data from Amazon S3, Amazon DynamoDB, Amazon EMR etc|
|Data Pipelines |Load using AWS Data Pipeline|
|On-premises data|Use Storage Gateway or Import/Export to import data into S3. COPY data from S3|
|Other databases|AWS Database Migration Service : RDS, DynamoDB or another Amazon Redshift Database|
|Recommendation| Prefer COPY over INSERT for bulk operations as COPY is done in parallel|
|Recommendation| Prefer COPY from multiple files. Split large files into multiple small input files|

## Redshift Workload Management

![](/images/aws/rds-diagrams/xx-redshift-wlm.png)
- WLM can be configured to prioritize queues
- Create multiple queues with different concurrency level for different purposes
- One queue for long running queries with low concurrency
- One queue for short running queries with high concurrency (upto 50 concurrent queries)

## Redshift Security
![](/images/aws/00-icons/redshift.png)
![](/images/arrow.png)
![](/images/aws/00-icons/kms.png)
- Uses 4-tier, key-based architecture for encryption
	- master key (chosen from keys in KMS)
	- a cluster encryption key (CEK)
	- a database encryption key (DEK)
	- and data encryption keys
- Manage keys using AWS KMS or AWS Cloud HSM
- IAM to manage user permissions for cluster operations
	- Grant permissions on a per cluster basis instead of per table basis

## Redshift Operations
![](/images/aws/00-icons/redshift.png)
![](/images/aws/00-icons/cloudwatch.png)
- Add new columns by using ALTER TABLE
	- Existing columns cannot be modified
- SQL operations are logged
	- Use SQL queries to query against system tables or download to S3
- Monitor performance & queries with Cloud Watch and Redshift web console
- When deleting a Redshift cluster, take a final snapshot to Amazon S3

