---
layout:     post
title:      Amazon DynamoDB - DAX and RDS - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon DynamoDB from an AWS certification perspective. We will look at important certification questions regarding Amazon DynamoDB. We will compare DynamoDB with RDS. We will also look at when you will use DAX with DynamoDB.
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-amazon-dynamodb-vs-rds
---

Let's get a quick overview of Amazon DynamoDB from an AWS certification perspective. We will look at important certification questions regarding Amazon DynamoDB. We will compare DynamoDB with RDS. We will also look at when you will use DAX with DynamoDB.

## You will learn

- What is Amazon DynamoDB?
- When do we use Amazon DynamoDB?
- How is Amazon DynamoDB different from Amazon RDS?
- When do you DAX with Amazon DynamoDB?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Amazon DynamoDB 

![](/images/aws/00-icons/dynamodb.png) 
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

![](/images/aws/document-database-example.png)
- Hierarchy : Table > item(s) > attribute (key value pair)
- Mandatory primary key
- Other than the primary key, tables are schemaless
	- No need to define the other attributes or types
	- Each item in a table can have distinct attributes
- Max 400 KB per item in table
	- Use S3 for large objects and DynamoDB for smaller objects

## DynamoDB - Keys

![](/images/aws/rds-diagrams/xx-rds-dynamodb-partition.png)

- Two parts:
	- (Mandatory) Partition key
	- (Optional) Sort key
- Primary key should be unique
- Partition key decides the partition (input to hash function)
- Same partition key items stored together (sorted by sort key)

## DynamoDB - Indexes

![](/images/aws/rds-diagrams/xx-rds-dynamodb-partition.png)
- (Optional) Secondary indexes to query on keys other than primary key
- Local secondary index 
	- Same partition key as primary key but different sort key
	- Should be created at the table creation
- Global secondary index 
	- Partition and sort key different from primary key
	- Can be added and removed at any point in time
	- Stored separately from the original table

## DynamoDB Query vs Scan

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

![](/images/aws/00-icons/dynamodb.png) 

- By default, eventually consistent (lag of about a second)
- Request for strongly consistent reads 
	- Set `ConsistentRead` to true
	- Slow and more expensive
- Supports transactions
	- All-or-nothing changes to multiple items both within and across tables
	- Twice the cost

## DynamoDB Read/Write Capacity Modes

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

![](/images/aws/00-icons/dynamodb.png) 

- Performance Monitoring - CloudWatch
- Alerts on RCU, WCU and Throttle Requests - CloudWatch Alarms
- Migrate data from RDS or MongoDB to DynamoDB - AWS Database Migration Service
- (Feature) Enable point-in-time recovery (max 35 days)
- Use Time to Live (TTL) to automatically expire items

## DynamoDB - IAM and Encryption

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

|Feature  | DynamoDB  | RDS|
|--|:--|:--|
| Scenario   |  Millisecond latency with millions of TPS    | Stronger consistency (schema) and transactional capabilities|
| Schema| Schemaless (needs only a primary key - Great for use cases where your schema is evolving)| Well-defined schema with relationships|
|Data Access|Using REST API provided by AWS using AWS SDKs or AWS Management Console or AWS CLI|SQL queries|
|Complex Data Queries Involving Multiple Tables|Difficult to run| Run complex relational queries with multiple entities|
|Scaling| No upper limits| 64 TB |
|Consistency| Typically lower consistency | Typically higher consistency|

## DynamoDB Accelerator (DAX)
![](/images/aws/03-serverless/07-lamdba-dax.png)
- In-memory caching for DynamoDB providing microsecond response times
	- Typical DynamoDB response times - single-digit milliseconds
- Very few changes needed to connect to DAX
	- Can reduce your costs by saving your read capacity units
- Not recommended 
	- If you need strongly consistent reads or 
	- Your application is write-intensive with very few reads
