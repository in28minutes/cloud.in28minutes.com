---
layout:     post
title:      Choosing AWS Databases - RDS vs DynamoDB vs Redshift - AWS Certification Cheat Sheet
date:       2020-09-20 12:31:19
summary:    Let's get a quick overview of how you can choose between different AWS Databases. How do you choose RDS vs DynamoDB vs Redshift?
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-choosing-aws-databases
---

Let's get a quick overview of how you can choose between different AWS Databases. How do you choose RDS vs DynamoDB vs Redshift?

## You will learn
- What are the different types of databases?
- How can you choose the right AWS database for your scenario?
- What are the differences between RDS vs DynamoDB vs Redshift?
- When do you use RDS vs DynamoDB vs Redshift?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Database Categories

![](/images/aws/00-icons/rds.png)
![](/images/aws/00-icons/elasticache.png) 
![](/images/aws/00-icons/dynamodb.png)
![](/images/aws/00-icons/redshift.png)
- There are **several categories** of databases:
	- Relational (OLTP and OLAP), Document, Key Value, Graph, In Memory among others
- **Choosing type of database** for your use case is not easy. A few factors:
	- Do you want a **fixed schema**?
		- Do you want flexibility in defining and changing your schema? (schemaless)
	- What level of **transaction properties** do you need? (atomicity and consistency)
	- What kind of **latency** do you want? (seconds, milliseconds or microseconds)
	- **How many transactions** do you expect? (hundreds or thousands or millions of transactions per second)
	- **How much data** will be stored? (MBs or GBs or TBs or PBs)
	- and a lot more...

## Relational Databases

![Database](/images/aws/relational-schema.png)
- This was the **only option** until a decade back!
- Most **popular (or unpopular)** type of databases
- **Predefined schema** with tables and relationships
- Very **strong transactional** capabilities
- Used for 
	- OLTP (Online Transaction Processing) use cases and
	- OLAP (Online Analytics Processing) use cases

## Relational Database - OLTP (Online Transaction Processing)

![](/images/aws/00-icons/rds.png) 
- Applications where **large number of users make large number of small transactions** 
	- small data reads, updates and deletes
- **Use cases**:
	- Most traditional applications, ERP, CRM, e-commerce, banking applications
- **Popular databases**:
	- MySQL, Oracle, SQL Server etc
- Recommended AWS Managed Service: 
	- **Amazon RDS**
	- Supports Amazon Aurora, PostgreSQL, MySQL, MariaDB (Enhanced MySQL), Oracle Database, and SQL Server

## Relational Database - OLAP (Online Analytics Processing)

![](/images/aws/00-icons/redshift.png) 
- Applications allowing users to **analyze petabytes of data**
	- **Examples** : Reporting applications, Data ware houses, Business intelligence applications, Analytics systems
	- **Sample application** : Decide insurance premiums analyzing data from last hundred years
	- Data is consolidated from multiple (transactional) databases
- Recommended AWS Managed Service 
	- **Amazon Redshift**
	- **Petabyte-scale** distributed data ware house based on PostgreSQL

## Relational Databases - OLAP vs OLTP

![Database](/images/aws/database-columnar-storage.png)
![Database](/images/aws/database-columnar-storage-2.png)

- OLAP and OLTP use **similar data structures**
- BUT **very different approach in how data is stored**
- **OLTP databases** use row storage 
	- Each table row is stored together
	- Efficient for processing small transactions
- **OLAP databases** use columnar storage
	- Each table column is stored together
	- **High compression** - store petabytes of data efficiently
	- **Distribute data** - one table in multiple cluster nodes 
	- **Execute single query across multiple nodes** - Complex queries can be executed efficiently

## Document Database

![](/images/aws/database-document.png)
![](/images/aws/document-database-example.png)

- Structure data **the way your application needs it**
- Create **one table instead of dozens**!
- **Quickly evolving** semi structured data (**schema-less**)
- **Use cases** : Content management, catalogs, user profiles
- **Advantages** : (Horizontally) Scalable to **terabytes of data** with **millisecond responses** upto **millions of transactions per second**
- Recommended AWS Managed Service 
	- **Amazon DynamoDB**

## Key-value
![Database](/images/aws/database-key-value.png)
![Database](/images/aws/database-session-store.png)
- Use a **simple key-value pair** to store data. Key is a unique identifier.
- Values can be objects, compound objects or simple data values
- **Advantages** : (Horizontally) Scalable to **terabytes of data** with **millisecond responses** upto **millions of transactions per second**
- Recommended AWS Managed Service - **Amazon DynamoDB** again
- **Use cases** : shopping carts, session stores, gaming applications and very high traffic web apps

## Graph
![Database](/images/aws/graph.png)
- **Store and navigate** data with complex relationships
- **Use cases** : Social Networking Data (Twitter, Facebook), Fraud Detection
- Recommended AWS Managed Service - **Amazon Neptune**

## In-memory Databases

![](/images/aws/00-icons/elasticache.png) 
- **Retrieving data from memory is much faster from retrieving data from disk**
- In-memory databases like Redis deliver microsecond latency by storing **persistent data in memory**
- Recommended AWS Managed Service 
	- **Amazon ElastiCache**
	- Supports Redis and Memcached
		- Redis is recommended for persistent data
		- Memcached is recommended for simple caches
- **Use cases** : Caching, session management, gaming leader boards, geospatial applications

## AWS Databases - Summary

| Database Type | AWS Service  | Description |
|--|:--|:--|
| Relational OLTP databases   |  Amazon RDS     |  Row storage <BR/>Transactional usecases needing **predefined schema** and very **strong transactional** capabilities       |
|Relational OLAP databases|Amazon Redshift|Columnar storage <BR/>Reporting, analytics & intelligence apps needing **predefined schema**|
|Document & Key Databases|Amazon DynamoDB|Apps needing **quickly evolving** semi structured data (**schema-less**) <BR/> Scale to **terabytes of data** with **millisecond responses** upto **millions of TPS**<BR/>Content management, catalogs, user profiles, shopping carts, session stores and gaming applications|
|Graph Databases|Amazon Neptune|Store and navigate data with **complex relationships**<BR/>Social Networking Data (Twitter, Facebook), Fraud Detection|
|In memory databases/caches|Amazon ElastiCache|Applications needing **microsecond** responses<BR/>**Redis** - persistent data<BR/>**Memcached** - simple caches|

## AWS Databases - Interview and Certification Questions

| Scenario | Solution  | 
|--|:--|
|A start up with quickly evolving tables  |   DynamoDB    |
|Transaction application needing to process million transactions per second  |   DynamoDB    |
|Very high consistency of data is needed while processing thousands of transactions per second| RDS |
|Cache data from database for a web application| Amazon ElastiCache |
|Relational database for analytics processing of petabytes of data| Amazon Redshift |
