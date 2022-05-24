---
layout:     post
title:      Amazon RedShift vs RedShift Spectrum vs Amazon EMR - A comparison - AWS Certification Cheat Sheet
date:       2020-07-15 12:31:19
summary:    Let's get a quick overview of the big data options in AWS - Amazon RedShift vs RedShift Spectrum vs Amazon EMR. We will look at important certification questions regarding Amazon RedShift vs RedShift Spectrum vs Amazon EMR. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-amazon-redshift-vs-redshift-spectrum-vs-amazon-emr
---

Let's get a quick overview of the big data options in AWS - Amazon RedShift vs RedShift Spectrum vs Amazon EMR. We will look at important certification questions regarding Amazon RedShift vs RedShift Spectrum vs Amazon EMR.

## You will learn
- What are big data options in AWS?
- How do you choose - Amazon RedShift vs RedShift Spectrum vs Amazon EMR?
- Comparison - Amazon RedShift vs RedShift Spectrum vs Amazon EMR

## Table of Contents
- [Amazon Redshift](#amazon-redshift)
- [Amazon Redshift Spectrum](#amazon-redshift-spectrum)
- [Amazon EMR - Elastic MapReduce](#amazon-emr---elastic-mapreduce)
- [Amazon EMR - Storage Types](#amazon-emr---storage-types)
- [Comparison and Certification Questions - Amazon Redshift and EMR](#comparison-and-certification-questions---amazon-redshift-and-emr)

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>

## Amazon Redshift

Redshift is a relational database ( tables and relationships). 

What is the need for another relational database? 

RDS is optimized for online transaction processing. It is optimized to provide a balance between both reads and write operations. OLAP workloads have exponentially larger reads on the databases compared to writes.

The questions are:
- Can we use a different approach to design the database? 
- How about creating a cluster and splitting the execution of the same query across several nodes? 

Redshift is a **petabyte-scale distributed data ware house** based on PostgreSQL

Three important characteristics of Redshift:
- Massively parallel processing (MPP) - storage and processing can be split across multiple nodes
- Columnar data storage
- High data compression

## Amazon Redshift Spectrum

Amazon Redshift Spectrum helps you run SQL queries against datasets in Amazon S3. It does need for any intermediate data stores.

Here are some of the important characteristics:
- Auto scales based on your queries
- Scale storage and compute independently
- Metadata defined in Amazon Redshift
	- Avro, CSV, Ion, JSON, ORC, Parquet formats supported
- Eliminate expensive data transfers from S3 to data warehousing solutions (Cost effective)
- Integrates with Amazon Athena
- Query against Amazon EMR (as well)

## Amazon EMR - Elastic MapReduce

Amazon EMR is a managed Hadoop service with high availability and durability.

Here are some of the important characteristics:
- EMR gives access to underlying OS => You can SSH into it
- Important tools in Hadoop eco system are natively supported:
	- Examples: Pig, Hive, Spark or Presto
- Install others using bootstrap actions

Here are some of the important Use cases of Amazon EMR:
- Log processing for insights
- Click stream analysis for advertisers
- Genomic and life science dataset processing

## Amazon EMR - Storage Types

The table below shows the different Storage Types in EMR and the differences between them.

| Feature |Hadoop Distributed File System (HDFS)  | EMR File System (EMRFS) | 
|--|:--|:--|
|  Standard for Hadoop  |   ✓    |    X     |
|  Data Storage   |   EBS or instance storage     |    S3    |
|  Data Survival on cluster shutdown| Yes for EBS. No for Instance Storage| Yes|
|Persistent Clusters running 24 X 7 analysis| ✓ (low latency on instance storage)||
|Transient Clusters running Infrequent big data jobs||✓(Run MapReduce jobs against S3 bucket)|

## Comparison and Certification Questions - Amazon Redshift and EMR 

When do you use EMR? When do you use Redshift? 

Let's look at a quick table:

| Alternative | Scenario  | 
|--|:--|
| Amazon EMR | For big data frameworks like Apache Spark, Hadoop, Presto, or Hbase to do large scale data processing that needs high customization <BR/> For example: machine learning, graph analytics etc|
| Amazon Redshift | Run complex queries against data warehouse - housing structured and unstructured data pulled in from a variety of sources |
| Amazon Redshift Spectrum | Run queries directly against S3 without worrying about loading entire data from S3 into a data warehouse|
| Amazon Athena | Quick ad-hoc queries without worrying about provisioning a compute cluster (serverless) <BR/> Amazon Redshift Spectrum is recommended if you are executing queries frequently against structured data|
