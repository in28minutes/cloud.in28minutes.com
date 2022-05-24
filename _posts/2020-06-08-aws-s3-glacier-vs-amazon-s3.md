---
layout:     post
title:      Amazon S3 Glacier - vs Amazon S3 - AWS Certification Cheat Sheet
date:       2020-07-03 12:31:19
summary:    Let's get a quick overview of Amazon S3 Glacier from an AWS certification perspective. We will look at important certification questions regarding Amazon S3 Glacier. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-amazon-s3-glacier-vs-amazon-s3
---

Let's get a quick overview of Amazon S3 Glacier from an AWS certification perspective. We will look at important certification questions regarding Amazon S3 Glacier and compare it with Amazon S3.

## You will learn
- What is Amazon S3 Glacier?
- When do we use Amazon S3 Glacier?
- How is Amazon S3 Glacier different from Amazon S3?

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>


## Amazon S3 Glacier
![](/images/aws/00-icons/glacier.png)

In addition to existing as a S3 Storage Class, S3 Glacier is a separate AWS Service on it own!

Here are some of the important features:
- **Extremely low cost storage** for archives and long-term backups:
	- Old media content
	- Archives to meet regulatory requirements (old patient records etc)
	- As a replacement for magnetic tapes
- High durability (11 9s - 99.999999999%)
- High scalability (unlimited storage)
- High security (**encrypted** at rest and in transfer)

You cannot upload objects to Glacier using Management Console
- Use REST API, AWS CLI, AWS SDK

## Amazon S3 vs S3 Glacier

Let's compare Amazon S3 vs S3 Glacier. 

| Feature |Amazon S3 | S3 Glacier | 
|--|:--|:--|
| Terminology   |  Objects (files) are stored in Buckets (containers)     |    Archives (files) are stored in Vaults (containers)     |
|Keys|Objects keys are user defined|Archive keys are system generated identifiers|
|Mutability|(Default) Allows uploading new content to object|After an archive is created, it cannot be updated <BR/>(Perfect for regulatory compliance)|
|Max size|Each object can be upto 5TB|Each archive can be upto 40TB|
|Management Console|Almost all bucket and object operations supported|Only vault operations are supported. You cannot upload/delete/update archives.|
|Encryption|Optional| Mandatory using AWS managed keys and AES-256. <BR/>You can use client side encryption on top of this.|
|WORM Write Once Read Many Times| Enable Object Lock Policy|Enable Vault lock policy| 

## Retrieving archives from S3 Glacier

Retrieving archives from S3 Glacier is an **Asynchronous two step process** (Use REST API, AWS CLI or SDK)
- 1: Initiate a archive retrieval
- 2: (After archive is available) Download the archive


You can reduce S3 Glacier costs by :
- **Optionally specify a range, or portion,** of the archive to retrieve.
- **Requesting longer access times**. Here are some of the retrieval options:
	- Amazon S3 Glacier:
		- Expedited (1 – 5 minutes)
		- Standard (3 – 5 hours)
		- Bulk retrievals (5–12 hours) 
	- Amazon S3 Glacier Deep Archive:
		- Standard retrieval (upto 12 hours)
		- Bulk retrieval (upto 48 hours)
