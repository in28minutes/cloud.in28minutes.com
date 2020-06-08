---
layout:     post
title:      Amazon Kinesis - Data Streams, Firehose, Analytics and Video Streams - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon Kinesis - Data Streams, Firehose, Analytics and Video Streams. We will look at important certification questions regarding Amazon Kinesis - Data Streams, Firehose, Analytics and Video Streams. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-amazon-kinesis-data-streams-firehose-analytics-and-video-streams
---

Let's get a quick overview of Amazon Kinesis - Data Streams, Firehose, Analytics and Video Streams. We will look at important certification questions regarding Amazon Kinesis - Data Streams, Firehose, Analytics and Video Streams. 

## You will learn
- How do you handle streaming data in AWS?
- What is Amazon Kinesis?
- What are the different Amazon Kinesis Options - Data Streams, Firehose, Analytics and Video Streams?
- When do you use - Amazon Kinesis Data Streams vs Amazon Kinesis Firehose vs Amazon Kinesis Analytics vs Amazon Kinesis Video Streams?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}

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

## Amazon Kinesis Data Streams

![](/images/aws/02-Queuing/4-kinesis-streams.png)
- Limitless Real time stream processing 
	- Sub second processing latency
- Alternative for Kafka
- Supports multiple clients
	- Each client can track their stream position
- Retain and replay data (max 7 days & default 1 day)

## Amazon Kinesis Data Streams - Integrations

![](/images/aws/02-Queuing/4-kinesis-streams.png)
	
- Use application integrations to generate streams
	- Toolkits : AWS SDK, AWS Mobile SDK, Kinesis Agent
	- Service Integrations : AWS IOT, CloudWatch Events and Logs
- Process streams using Kinesis Stream Applications 
	- Run on EC2 instances
	- Written using Kinesis Data Streams APIs

## Amazon Kinesis Data Firehose

![](/images/aws/02-Queuing/5-kinesis-firehose.png)
- Data ingestion for streaming data
	- Receive
	- Process ( transform - Lambda, compress, encrypt ) 
	- Store stream data to S3, Elasticsearch, Redshift and Splunk
- Use existing analytics tools based on S3, Redshift and Elasticsearch
- Pay for volume of data ingested (Serverless)

## Amazon Kinesis Analytics
![](/images/aws/02-Queuing/5-kinesis-analytics.png)
- You want to continuously find active number of users on a website in the last 5 minutes based on streaming website data
- With Amazon Kinesis Analytics, you can write SQL queries and build Java applications to continuously analyze your streaming data

## Amazon Kinesis Video Streams
![](/images/aws/02-Queuing/5-kinesis-video-streams.png)
- Monitor video streams from web-cams 
- Examples: traffic lights, shopping malls, homes etc
- Integrate with machine learning frameworks to get intelligence