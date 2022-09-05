---
layout:     post
title:      Amazon S3 Storage Classes - Standard vs Standard-IA vs One Zone vs Intelligent-Tiering vs Glacier - AWS Certification Cheat Sheet
date:       2020-07-03 12:31:19
summary:    Let's get a quick overview of Amazon S3 Storage Classes from an AWS certification perspective. We will look at important certification questions regarding Amazon S3 Storage Classes. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-amazon-s3-storage-classes
---

Let's get a quick overview of Amazon S3 Storage Classes from an AWS certification perspective. We will look at important certification questions regarding Amazon S3 Storage Classes.

## You will learn

- What are the different Amazon S3 Storage Classes?
- Why are Amazon S3 Storage Classes important?
- When do we use Amazon S3 Storage Classes?
- Differences and Comparison of Amazon S3 Storage Classes - Standard vs Intelligent Tiering vs Standard IA vs One Zone IA vs Glacier vs Glacier Deep Archive


## Amazon S3 Storage Classes - Introduction

**Different kinds of data** can be stored in Amazon S3
- Media files and archives
- Application packages and logs
- Backups of your databases or storage devices
- Long term archives

There are Huge variations in **access patterns**. So, you have to **Trade-off** between access time and cost.

**S3 storage classes** help to optimize your costs while meeting access time needs. They are designed for durability of **99.999999999%(11 9’s)**.

## Amazon S3 Storage Classes - Types

Here are the important S3 Storage Classes:

|Storage Class|Scenario|AZs|
|--|:--|:--|
|Standard|Frequently accessed data|>=3|
|Standard-IA|Long-lived, infrequently accessed data (backups for disaster recovery)|>=3|
|One Zone-IA|Long-lived, infrequently accessed, non-critical data (Easily re-creatable data - thumbnails for images)|1|
|Intelligent-Tiering|Long-lived data with changing or unknown access patterns|>=3|
|Glacier|Archive data with retrieval times ranging from minutes to hours|>=3|
|Glacier Deep Archive|Archive data that rarely, if ever, needs to be accessed with retrieval times in hours|>=3|
|Reduced Redundancy (Not recommended)|Frequently accessed, non-critical data|>=3|

## Amazon S3 Storage Classes - Comparison

Here is the comparison between different S3 Storage Classes:

| Feature |Standard | Intelligent Tiering | Standard IA| One Zone IA | Glacier | Glacier Deep Archive |
|--|--|--|--|--|--|--|
|Availability (Designed)|99.99%|99.9%|99.9%|99.5%|99.99%|99.99%|
|Availability (SLA)|99.9%|99%|99%|99%|99.9%|99.9%|
|Replication AZs|>=3|>=3|>=3|1|>=3|>=3|
|First byte: ms (milliseconds)|ms|ms|ms|ms|minutes or hours|few hours|
|Min object size (for billing)|NA|NA|128KB|128KB|40KB|40KB|
|Min storage days (for billing)|NA|30|30|30|90|180|
|Per GB Cost (varies)| $0.025 | varies | $0.018 | $0.0144 | $0.005|$0.002|
|Encryption|Optional|Optional|Optional|Optional|Mandatory|Mandatory|
