---
layout:     post
title:      Amazon DynamoDB - DAX and RDS - AWS Certification Cheat Sheet
date:       2020-06-17 12:31:19
summary:    Let's get a quick overview of Amazon DynamoDB from an AWS certification perspective. We will look at important certification questions regarding Amazon DynamoDB. We will compare DynamoDB with RDS. We will also look at when you will use DAX with DynamoDB.
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-amazon-dynamodb-vs-rds
---

Let's get a quick overview of Amazon DynamoDB from an AWS certification perspective. We will look at important certification questions regarding Amazon DynamoDB. We will compare DynamoDB with RDS. We will also look at when you will use DAX with DynamoDB.

## You will learn

- What is Amazon DynamoDB?
- When do we use Amazon DynamoDB?
- How is Amazon DynamoDB different from Amazon RDS?
- When do you use DAX with Amazon DynamoDB?

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>


## Amazon DynamoDB 
Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. 
It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. 
DynamoDB can handle more than 10 trillion requests per day and can support peaks of more than 20 million requests per second.

![](/images/aws/00-icons/dynamodb.png) 

Lets look at the key features of DynamoDB.
- Fast, scalable, distributed for any scale
- Flexible NoSQL Key-value & document database (schemaless) 
- Single-digit millisecond responses for million of TPS
- Do not worry about scaling, availability or durability
	- Automatically partitions data as it grows
	- Maintains 3 replicas within the same region
- No need to provision a database 
	- Create a table and configure read and write capacity (RCU and WCU)
	- Automatically scales to meet your RCU and WCU
- Provides an expensive serverless mode
- Use cases: User profiles, shopping carts, high volume read write applications

## DynamoDB Tables
In DynamoDB, tables, items, and attributes are the core concepts you use. 
A table is a collection of items, and each item contains one or more attributes.
Like other database systems, DynamoDB stores records/items in tables.

![](/images/aws/document-database-example.png)

- Hierarchy : Table > item(s) > attribute (key value pair)
- Mandatory primary key
- Other than the primary key, tables are schemaless
	- No need to define the other attributes or types
	- Each item in a table can have distinct attributes
- Max 400 KB per item in table
	- Use S3 for large objects and DynamoDB for smaller objects

## DynamoDB - Keys
When we create DynamoDB tables we need to also mention a primary key.

![](/images/aws/rds-diagrams/xx-rds-dynamodb-partition.png)

- Two parts:
	- (Mandatory) Partition key
	- (Optional) Sort key
- Primary key should be unique
- Partition key decides the partition (input to hash function)
- Same partition key items stored together (sorted by sort key)

## DynamoDB - Indexes
DynamoDB supports one or more secondary indexes on a table.

- (Optional) Secondary indexes to query on keys other than primary key
- Local secondary index 
	- Same partition key as primary key but different sort key
	- Should be created at the table creation
- Global secondary index 
	- Partition and sort key different from primary key
	- Can be added and removed at any point in time
	- Stored separately from the original table

## DynamoDB Query vs Scan
DynamoDB provides the following operations for reading data.

![](/images/aws/00-icons/dynamodb.png) 

- Query 
	- Search using a partition key attribute and a distinct value to search
	- Optional - sort key and filters
	- Results are sorted by primary key
	- Max 1 MB
- Scan 
	- Reads every item in a table
	- Expensive compared to query
	- Returns all attributes by default
	- Supports paging above 1 MB
	- Filter items using expressions

## DynamoDB Consistency Levels
DynamoDB stores data across multiple regions and availability zones. When the applications writes or updates data
it receives http status 200. This means the write is successful and durable. However it may take sometime before data
is available across all storage locations.

![](/images/aws/00-icons/dynamodb.png) 

- By default, eventually consistent (lag of about a second)
- Request for strongly consistent reads 
	- Set `ConsistentRead` to true
	- Slow and more expensive
- Supports transactions
	- All-or-nothing changes to multiple items both within and across tables
	- Twice the cost

## DynamoDB Read/Write Capacity Modes
DynamoDB has two read/write capacity modes for processing reads and writes on the tables.

![](/images/aws/00-icons/dynamodb.png) 

- Provisioned 
	- Provision read and write capacity 
	- Dynamically adjustable
	- Unused capacity can be used in bursts
	- You are billed for the provisioned capacity irrespective of whether you make use of it or not
- On Demand
	- Truly serverless and expensive
	- For unknown workloads or traffic with huge spikes
	- Use On Demand only when your  
		- Workloads are really spiky causing low utilization of Provisioned Capacity OR
		- Usage is very low (for example, in test environments) making manual adjustments expensive

## DynamoDB Read/Write Capacity Used
Lets look at how much read/write capacity is used for different types of reads & writes.

![](/images/aws/00-icons/dynamodb.png) 

- Capacity used depends on size of item, read consistency, transactions etc
- 1 capacity unit to read 4 KB or smaller (more for bigger items)
- 1 capacity unit to write 1 KB or smaller (more for bigger items)
- Twice the capacity for a strongly consistent or transactional requests
- On-demand RCU is almost 8 times the cost of Provisioned RCU
- Example: $0.2500 per million vs $0.0361 per million

Note:
- RCU vs WCU (RCU is cheaper than WCU. So, it is cheaper for read workloads.)

## DynamoDB - Operations
AWS provides various tools that can be used for monitoring & performing various operations on DynamoDB

![](/images/aws/00-icons/dynamodb.png) 

- Performance Monitoring - CloudWatch
- Alerts on RCU, WCU and Throttle Requests - CloudWatch Alarms
- Migrate data from RDS or MongoDB to DynamoDB - AWS Database Migration Service
- (Feature) Enable point-in-time recovery (max 35 days)
- Use Time to Live (TTL) to automatically expire items

## DynamoDB - IAM and Encryption
DynamoDB protects data stored in the tables through server side and client side encryptions.
Also through IAM we can authenticate and authorize the control the access to DynamoDB.

![](/images/aws/00-icons/dynamodb.png) 

- Server-side encryption in integration with keys from KMS
	- Always enabled
	- Automatically encrypts tables, DynamoDB streams, and backups
- Client-side encryption with DynamoDB Encryption Client
	- You can manage your keys with KMS or CloudHSM
- Use IAM roles to provide EC2 instances or AWS services access to DynamoDB tables
	- Predefined policies available for DynamoDB
		- AmazonDynamoDBReadOnlyAccess
		- AmazonDynamoDBFullAccess etc
	- Fine-grained control at the individual item level

##  DynamoDB vs RDS
Lets looks at DynamoDB & RDS and compare them for different features.
 
|Feature  | DynamoDB  | RDS|
|--|:--|:--|
| Scenario   |  Millisecond latency with millions of TPS    | Stronger consistency (schema) and transactional capabilities|
| Schema| Schemaless (needs only a primary key - Great for use cases where your schema is evolving)| Well-defined schema with relationships|
|Data Access|Using REST API provided by AWS using AWS SDKs or AWS Management Console or AWS CLI|SQL queries|
|Complex Data Queries Involving Multiple Tables|Difficult to run| Run complex relational queries with multiple entities|
|Scaling| No upper limits| 64 TB |
|Consistency| Typically lower consistency | Typically higher consistency|

## DynamoDB Accelerator (DAX)
DynamoDB Accelerator (DAX) delivers fast response times for accessing eventually consistent data. Certain usecases requires microseconds
response times

![](/images/aws/03-serverless/07-lamdba-dax.png)

- In-memory caching for DynamoDB providing microsecond response times
	- Typical DynamoDB response times - single-digit milliseconds
- Very few changes needed to connect to DAX
	- Can reduce your costs by saving your read capacity units
- Not recommended 
	- If you need strongly consistent reads or 
	- Your application is write-intensive with very few reads
