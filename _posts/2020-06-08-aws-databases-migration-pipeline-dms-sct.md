---
layout:     post
title:      Migrating databases in AWS - Data Pipeline vs DMS vs SCT - AWS Certification Cheat Sheet
date:       2020-07-15 12:31:19
summary:    Let's get a quick overview of different options in migrating databases from/to AWS - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-migrating-databases-in-aws-data-pipeline-vs-dms-vs-sct
---

Let's get a quick overview of different options in migrating databases from/to AWS - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT.

## You will learn
- What is different options in migrating databases from/to AWS?
- Comparison - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT
- When to use - Data Pipeline vs Database Migration Service DMS vs Schema Conversion Tool SCT

## Table of Contents

- [AWS Data Pipeline](#aws-data-pipeline)
- [AWS Database Migration Service](#aws-database-migration-service)
- [AWS Schema Conversion Tool](#aws-schema-conversion-tool)
- [Database Migration Service VS Schema Conversion Tool](#database-migration-service-vs-schema-conversion-tool)

## AWS Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## AWS Data Pipeline
AWS Data Pipeline helps you to process and move data (ETL) between S3, RDS, DynamoDB, EMR, On-premise data sources.

Here are few important things to remember:
- AWS Data Pipeline can create complex data processing workloads that are fault tolerant, repeatable, and highly available
- AWS Data Pipeline launches required resources and tear them down after execution
- REMEMBER : AWS Data Pipeline is NOT for streaming data!

## AWS Database Migration Service
AWS Database Migration Service is used to migrate databases to AWS while keeping source databases operational.

Two types of migrations:
- Homogeneous Migrations (ex: Oracle to Oracle)
- Heterogeneous Migrations (ex: Oracle to Amazon Aurora, MySQL to Amazon Aurora)

Here are some of the important characteristics:
- Free for first 6 months when migrating to  Aurora,  Redshift or  DynamoDB
- (AFTER MIGRATION) You can keep databases in sync and pick right moment to switch

Here are some the important use cases:
- Consolidate multiple databases into a single target database
- Continuous Data Replication can be used for Disaster Recovery

## AWS Schema Conversion Tool

AWS Schema Conversion Tool is used to migrate data from commercial databases and data warehouses to open source or AWS services.

AWS Schema Conversion Tool is preferred option for migrating data warehouse data to Amazon Redshift.

You can migrate database schema (views, stored procedures, and functions) to compatible targets.

Here are some of the important features:
- SCT assessment report 
	- Analyze a database to determine the conversion complexity
- Update source code (update embedded SQL in code)
- Fan-in (multiple sources - single target) 
- Fan-out (single source - multiple targets)

## Database Migration Service VS Schema Conversion Tool
Remember that SCT is part of DMS service.

Here are some of the important recommendations:
- DMS is preferred for homogeneous migrations
- SCT is preferred when schema conversion are involved
- DMS is for smaller workloads (less than 10 TB) 
- SCT preferred for large data warehouse workloads
	- Prefer SCT for migrations to Amazon Redshift
- Only DMS provides continuous data replication after migration