---
layout:     post
title:      Amazon RedShift vs RedShift Spectrum vs Amazon EMR - A comparison - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of the big data options in AWS - Amazon RedShift vs RedShift Spectrum vs Amazon EMR. We will look at important certification questions regarding Amazon RedShift vs RedShift Spectrum vs Amazon EMR. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-amazon-redshift-vs-redshift-spectrum-vs-amazon-emr
---

Let's get a quick overview of the big data options in AWS - Amazon RedShift vs RedShift Spectrum vs Amazon EMR. We will look at important certification questions regarding Amazon RedShift vs RedShift Spectrum vs Amazon EMR.

## You will learn
- What are big data options in AWS?
- How do you choose - Amazon RedShift vs RedShift Spectrum vs Amazon EMR?
- Comparison - Amazon RedShift vs RedShift Spectrum vs Amazon EMR

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
- Three important characteristics of Redshift:
	- Massively parallel processing (MPP) - storage and processing can be split across multiple nodes
	- Columnar data storage
	- High data compression

## Amazon Redshift Spectrum

![](/images/aws/001-basic-drawings/redshift-spectrum.png)
- Run SQL queries against datasets in Amazon S3 
	- Does need for any intermediate data stores
- Auto scales based on your queries
- Scale storage and compute independently
- Metadata defined in Amazon Redshift
	- Avro, CSV, Ion, JSON, ORC, Parquet formats supported
- Eliminate expensive data transfers from S3 to data warehousing solutions (Cost effective)
- Integrates with Amazon Athena
- Query against Amazon EMR (as well)

## Amazon EMR - Elastic MapReduce
- Managed Hadoop service with high availability and durability
- EMR gives access to underlying OS => You can SSH into it
- Important tools in Hadoop eco system are natively supported:
	- Examples: Pig, Hive, Spark or Presto
- Install others using bootstrap actions
- Use cases 
	- Log processing for insights
	- Click stream analysis for advertisers
	- Genomic and life science dataset processing

## Amazon EMR - Storage Types
 
| Feature |Hadoop Distributed File System (HDFS)  | EMR File System (EMRFS) | 
|--|:--|:--|
|  Standard for Hadoop  |   ✓    |    X     |
|  Data Storage   |   EBS or instance storage     |    S3    |
|  Data Survival on cluster shutdown| Yes for EBS. No for Instance Storage| Yes|
|Persistent Clusters running 24 X 7 analysis| ✓ (low latency on instance storage)||
|Transient Clusters running Infrequent big data jobs||✓(Run MapReduce jobs against S3 bucket)|

## Comparison and Certification Questions - Amazon Redshift and EMR 

| Alternative | Scenario  | 
|--|:--|
| Amazon EMR | For big data frameworks like Apache Spark, Hadoop, Presto, or Hbase to do large scale data processing that needs high customization <BR/> For example: machine learning, graph analytics etc|
| Amazon Redshift | Run complex queries against data warehouse - housing structured and unstructured data pulled in from a variety of sources |
| Amazon Redshift Spectrum | Run queries directly against S3 without worrying about loading entire data from S3 into a data warehouse|
| Amazon Athena | Quick ad-hoc queries without worrying about provisioning a compute cluster (serverless) <BR/> Amazon Redshift Spectrum is recommended if you are executing queries frequently against structured data|
