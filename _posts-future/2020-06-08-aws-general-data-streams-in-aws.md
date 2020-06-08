---
layout:     post
title:      Data Streams in AWS - Amazon Kinesis vs S3 Notifications vs DynamoDB Streams - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of options to handle Data Streams in AWS - Amazon Kinesis vs S3 Notifications vs DynamoDB Streams. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-data-streams-in-aws
---

Let's get a quick overview of options to handle Data Streams in AWS - Amazon Kinesis vs S3 Notifications vs DynamoDB Streams. 

## You will learn
- What are options to handle Data Streams in AWS?
- Understand the options - Amazon Kinesis vs S3 Notifications vs DynamoDB Streams

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## Streaming Data

![](/images/datastream.png) 
- Imagine implementing analytics for a website:
	- You have a continuous stream of data (page views, link clicks etc)
- Characteristics of streaming data:
	- Continuously generated
	- Small pieces of data
	- Sequenced - mostly associated with time
- How do your process continuous streaming data originating from application logs, social media applications?

## Amazon Kinesis

![](/images/datastream.png) 
- Handle streaming data
	- NOT recommended for ETL Batch Jobs
- Amazon Kinesis Data Streams
	- Process Data Streams
- Amazon Kinesis Firehose
	- Data ingestion for streaming data : S3, Elasticsearch etc
- Amazon Kinesis Analytics
	- Run queries against streaming data
- Amazon Kinesis Video Streams
	- Monitor video streams

## S3 Notifications

![](/images/aws/00-icons/s3bucket.png)
![](/images/arrow.png)
![](/images/aws/00-icons/lambdafunction.png)
- Send notifications to SNS, SQS, trigger lambda functions on 
	- creation, deletion or update of an S3 object
- Setup at bucket level
	- You can use prefix and suffix to configure
- Cost efficient for simple use cases
	- S3 notification -> Lambda
	- Almost negligible cost (storage for file + invocation)

## DynamoDB Streams
![](/images/aws/001-basic-drawings/dynamodbstreams.png)
- Each event from DynamoDB (in time sequenced order) is buffered in a stream near real-time
- Can be enabled or disabled
- Use case - Send email when user registers
	- Tie a Lambda function to DynamoDB Streams
- Stream allow iteration through records (**last 24 hours**)