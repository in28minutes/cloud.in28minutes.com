---
layout:     post
title:      Google Cloud For Beginners - How to choose a Database Service?
date:       2022-10-22 12:31:19
summary:    Google Cloud offer multiple database options. How to choose between them?
categories:  GCP_CLOUD
permalink:  /google-cloud-for-beginners-choosing-database
---

Managing databases is a pain. Ensuring high availability, high durability and a host of other needs for your databases is a big challenge. Cloud platforms provide you with varied range of database services. 

How do you choose a database service in Google Cloud?

Let's find out!

![](/gcpimages/02-architecture/database-fundamentals-3-single-db-snapshot-transaction.png)

<!-- MarkdownTOC -->

- 1: Is choosing a database easy?
- 2: What are the different categories of databases?
	- 2.1: What are Relational Databases?
		- Relational Databases - OLTP - Online Transaction Processing
			- Cloud SQL
			- Cloud Spanner
			- Cloud SQL vs Cloud Spanner
		- Relational Database - OLAP - Online Analytics Processing
			- BigQuery - Modern Data warehouse
	- 2.2: What are NoSQL Databases?
		- Cloud Datastore and Firestore
		- Cloud BigTable
		- Choosing between Cloud Firestore, Datastore vs Cloud BigTable
	- 2.3: What are In-memory Databases?
- 3: Let's get a quick summary

<!-- /MarkdownTOC -->


## 1: Is choosing a database easy?

**Choosing a database** for your use case is not easy. A few factors you would need to consider:
- 1: Do you want a **fixed schema**? Do you want flexibility in defining and changing your schema? Do you want to go schemaless?
- 2: What level of **transaction properties** do you need? (atomicity and consistency)
- 3: What kind of **latency** do you want? (seconds, milliseconds or microseconds)
- 4: **How many transactions** do you expect? (hundreds or thousands or millions of transactions per second)
- 5: **How much data** will be stored? (MBs or GBs or TBs or PBs)

Before we get into the details, let's explore the different categories of databases:

## 2: What are the different categories of databases?

There are **several categories** of databases: Relational (OLTP and OLAP), Document, Key Value, Graph, In Memory among others

### 2.1: What are Relational Databases?

Most **popular (or unpopular)** type of databases. These have **Predefined schema** with tables and relationships. Relational database provide very **strong transactional** capabilities.

![](/gcpimages/02-architecture/database-fundamentals-relational-schema.png)

#### Relational Databases - OLTP - Online Transaction Processing

Let's start with applications where a large number of users make a large number of small transactions ( small reads & updates). Typical use cases include CRM, e-commerce, and banking applications. The most popular databases are MySQL, Oracle, SQL Server, etc.

Recommended GCP Services are:
- **Cloud SQL**: Supports PostgreSQL, MySQL, and SQL Server for regional relational databases (up to a few TBs)
- **Cloud Spanner**: Unlimited scale (multiple PBs) and 99.999% availability for global applications with horizontal scaling

##### Cloud SQL

Cloud SQL is a **Fully Managed Relational Database** service.

Here are some of the important features:
- Supports MySQL, PostgreSQL, and SQL Server
- Regional Service providing High Availability (99.95%)
- Option to use SSDs or HDDs (For best performance: use SSDs)
- Automatic encryption (tables/backups), maintenance and updates
- High availability and failover: Create a Standby with automatic failover
- Read replicas for read workloads - Options: Cross-zone, Cross-region and External (NON Cloud SQL DB)
- Automatic storage increase without downtime (for newer versions)
- Point-in-time recovery: Enable binary logging
- Backups (Automated and on-demand backups)

##### Cloud Spanner

Cloud Spanner is a **fully managed, mission critical, relational(SQL), globally distributed database** with VERY high availability. It provides strong transactional consistency at **global scale**. It can **scales to petabytes of data** with automatic sharding.

Here are some of the important features:
- **Scales horizontally for reads and writes**: In comparison, Cloud SQL provides read replicas BUT you cannot horizontally scale write operations with Cloud SQL!
- Regional and Multi-Regional configurations
- **Expensive** (compared to Cloud SQL): You pay for nodes & storage


##### Cloud SQL vs Cloud Spanner

Use Cloud Spanner(Expensive $$$$) instead of Cloud SQL for relational transactional applications if: 
- You have huge volumes of relational data (TBs) OR 
- You need infinite scaling for a growing application (to TBs) OR 
- You need a Global (distributed across multiple regions) Database OR
- You need higher availability (99.999%)


#### Relational Database - OLAP - Online Analytics Processing

OLAP Applications allow users to analyze petabytes of data. Examples include Reporting applications, Data warehouses, Business intelligence applications, and Analytics systems.

Recommended GCP Managed Service is **BigQuery**.

##### BigQuery - Modern Data warehouse
BigQuery is one of most popular cloud data warehouses. It can handle exabytes of data with ease. It combines traditional data warehouse elements (Huge storage + compute) with modern elements (Realtime + Serverless).

![](/gcpimages/02-architecture/database-columnar-storage.png)


### 2.2: What are NoSQL Databases?

NoSQL represents a new approach (actually NOT so new!) to building your databases.

NoSQL stands for "not only SQL". You would use NoSQL databases when you need flexible schema - structure data the way your application needs it and you want to let the schema evolve with time.

Most NoSQL databases can scale horizontally to petabytes of data with millions of TPS.

Google Managed Services are **Cloud Firestore (Datastore)** &  **Cloud BigTable**.

![](/gcpimages/02-architecture/database-document.png)


#### Cloud Datastore and Firestore

**Datastore** is a highly scalable NoSQL Document Database. It automatically scales and partitions data as it grows. Recommended for use cases needing flexible schema with transactions. Examples: User Profile and Product Catalogs. Datastore can handle upto a few terabytes of data.

Here are some of the important features:
- Supports Transactions, Indexes and SQL like queries (GQL)
- Does NOT support Joins or Aggregate (sum or count) operations

**Firestore** is the new version of Datastore. I call it Datastore++. It is optimized for multi device access. It provides an offline mode and data synchronization across multiple devices - mobile, IOT etc.

#### Cloud BigTable

Cloud BigTable is a HBase API compatible **Petabyte scale, wide column** NoSQL DB. It is designed to handle huge volumes of analytical and operational data. For example: IOT Streams, Analytics, Time Series Data etc.

Some of the important features include:
- Handle millions of read/write TPS at very low latency
- Single row transactions (multi row transactions NOT supported)
- Scale horizontally with multiple nodes (No downtime for cluster resizing)
- **NOT serverless**: You need to create a server instance

#### Choosing between Cloud Firestore, Datastore vs Cloud BigTable

Cloud Datastore is managed serverless NoSQL document database. It provides ACID transactions, SQL-like queries, and indexes. It is designed for transactional mobile and web applications.

Firestore is the next version of Datastore with additional capabilities like Strong consistency and Mobile and Web client libraries.

Firestore and Datastore are recommended for small to medium databases (0 to a few Terabytes).

Cloud BigTable on the other hand, is a managed, scalable NoSQL wide column database. It is NOT serverless (You need to create instances). 

BigTable is recommended for data sizes greater than 10 terabytes. It is usually used for large analytical and operational workloads.

BigTable is NOT recommended for transactional workloads. It does NOT support multi-row transactions - supports ONLY single-row transactions.

### 2.3: What are In-memory Databases?

Retrieving data from memory is much faster than retrieving data from disk. In-memory databases like Redis deliver microsecond latency by storing persistent data in memory.

Recommended GCP Managed Service is Memorystore.

## 3: Let's get a quick summary

| Database Type | GCP Services  | Description |
|--|:--|:--|
|Relational OLTP databases|Cloud SQL, Cloud Spanner|Transactional usecases needing **predefined schema** and very **strong transactional** capabilities (Row storage) <BR/> **Cloud SQL**: MySQL, PostgreSQL, SQL server DBs <BR/> **Cloud Spanner**: Unlimited scale and 99.999% availability for global applications with horizontal scaling|
|Relational OLAP databases|BigQuery|Columnar storage with predefined schema. Datawarehousing & BigData workloads|
|NoSQL Databases|Cloud Firestore (Datastore) , Cloud BigTable|Apps needing **quickly evolving** structure (**schema-less**)<BR/>**Cloud Firestore** -  Serverless transactional document DB supporting mobile & web apps. Small to medium DBs (0 - few TBs)<BR/> **Cloud BigTable** - Large databases(10 TB - PBs). Streaming (IOT), analytical & operational workloads. NOT serverless.|
|In memory databases/caches|Cloud Memorystore|Applications needing **microsecond** responses|