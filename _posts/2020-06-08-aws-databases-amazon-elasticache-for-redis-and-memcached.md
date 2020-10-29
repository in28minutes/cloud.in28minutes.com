---
layout:     post
title:      Amazon ElastiCache for Redis and Memcached - AWS Certification Cheat Sheet
date:       2020-06-20 12:31:19
summary:    Let's get a quick overview of Amazon ElastiCache for Redis and Memcached from an AWS certification perspective. We will look at important certification questions regarding Amazon ElastiCache for Redis and Memcached. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-amazon-elasticache-for-redis-and-memcached
---

Let's get a quick overview of Amazon ElastiCache for Redis and Memcached from an AWS certification perspective. We will look at important certification questions regarding Amazon ElastiCache for Redis and Memcached.

## You will learn
- What is Amazon ElastiCache?
- What are the options that Amazon ElastiCache offers?
- When do we use Amazon ElastiCache for Redis vs Amazon ElastiCache for Memcached?
- How is Amazon ElastiCache for Redis different from Amazon ElastiCache for Memcached?

## AWS Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>



## Amazon ElastiCache 
Amazon ElastiCache allows you to seamlessly set up, run, and scale popular open-Source compatible in-memory data stores in the cloud. Build data-intensive apps or boost the performance of your existing databases by retrieving data from high throughput and low latency in-memory data stores. Amazon ElastiCache is a popular choice for real-time use cases like Caching, Session Stores, Gaming, Geospatial Services, Real-Time Analytics, and Queuing.

![](/images/aws/00-icons/elasticache.png) 
- Managed service providing highly scalable and low latency in-memory data store
- Used for distributed caching
- Two Options:
	- Redis
	- Memcached

## Amazon ElastiCache for Redis

- Highly scalable and low latency in-memory data store
- Can be used as a cache, database or message broker
- Automatic failover with Multi-AZ deployments (if enabled)
- Supports backup and restore
- Supports encryption at-rest (KMS) and in-transit
- Use cases:
	- Caching
	- Session Store
	- Chat and Messaging
	- Gaming Leader boards
	- Geospatial Apps (Ride hailing, restaurant recommendations)
	- Queues

## Amazon ElastiCache for Redis - Cluster

- Shard - collection of one or more nodes
- One node acts as read/write primary
- Other nodes act as read replicas (up to five read replicas)
- In case of failure:
	- Primary node is replaced
	- If Multi-AZ replication group is enabled, read replica is promoted to primary
	- DNS entry is updated

## ElastiCache Redis - Backup and Snapshot
![](/images/aws/00-icons/elasticache.png) 
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png)
- Uses native backup feature of Redis (stored to S3)
- Recommended to perform snapshot against read replicas
- You can schedule snapshots 
	- Configure backup window and 
	- Days of backup you want to store
- Manual snapshots are available until they are manually deleted

## Amazon ElastiCache for Memcached

- Simple caching layer intended for use in speeding up dynamic web applications
	- Pure cache
	- Non-persistent
	- Simple key-value storage
- Ideal front-end for data stores like RDS or DynamoDB
- Can be used as a transient session store
- Create upto 20 cache nodes
- Use Auto Discovery to discover cache nodes

## Amazon ElastiCache for Memcached - Limitations

- Backup and restore NOT supported
- Does not support encryption or replication
- Does not support snapshots
	- When a node fails, all data in the node is lost
	- Reduce impact of failure by using large number of small nodes

## ElastiCache Memcached vs Redis

- Use ElastiCache Memcached for
	- Low maintenance simple caching solution
	- Easy horizontal scaling with auto discovery
- Use ElastiCache Redis for
	- Persistence 
	- Publish subscribe messaging
	- Read replicas and failover
	- Encryption
