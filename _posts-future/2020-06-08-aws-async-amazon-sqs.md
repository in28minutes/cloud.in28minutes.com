---
layout:     post
title:      Amazon SQS - Simple Queuing Service - FIFO vs Standard Queue - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon SQS from an AWS certification perspective. We will look at important certification questions regarding Amazon SQS. 
categories:  AWS_CLOUD AWS_ASYNCHRONOUS
permalink:  /aws-certification-amazon-sqs-simple-queuing-service
---

Let's get a quick overview of Amazon SQS from an AWS certification perspective. We will look at important certification questions regarding Amazon SQS.

## You will learn
- What is Amazon SQS?
- Why do we need Amazon SQS?
- When do we use Amazon SQS?
- What is difference between FIFO vs Standard Queue?
- How do you implement auto scaling with CloudWatch Alarms for SQS Queue?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## Simple Queuing Service

![](/images/aws/02-Queuing/2-sqs.png)
- Reliable, scalable, fully-managed message queuing service
- High availability
- Unlimited scaling
	- Auto scale to process billions of messages per day
- Low cost (Pay for use)

## Standard and FIFO Queues

![](/images/aws/00-icons/sqs.png)

- Standard Queue 
	- Unlimited throughput
	- BUT NO guarantee of ordering (Best-Effort Ordering) 
	- and NO guarantee of exactly-once processing
		- Guarantees at-least-once delivery (some messages can be processed twice)
- FIFO (first-in-first-out) Queue
	- First-In-First-out Delivery
	- Exactly-Once Processing
	- BUT throughput is lower 
		- Upto 300 messages per second (300 send, receive, or delete operations per second)
		- If you batch 10 messages per operation (maximum), up to 3,000 messages per second 
- Choose
	- Standard SQS queue if throughput is important
	- FIFO Queue if order of events is important

## Sending and receiving a SQS Message - Best case scenario

![](/images/aws/02-Queuing/sqs-simple-flow.png)
- Producer places message on queue 
	- Receives globally unique message ID ABCDEFGHIJ (used to track the message)
- Consumer polls for messages 
	- Receives the message ABCDEFGHIJ along with a receipt handle XYZ
- Message remains in the queue while the consumer processes the message
	- Other consumers will not receive ABCDEFGHIJ even if they poll for messages
- Consumer processes the message successfully 
	- Calls delete message (using receipt handle XYZ)
	- Message is removed from the queue

## Simple Queuing Service Lifecycle of a message
![](/images/aws/02-Queuing/4-Queuing-LifeCycle.png)

Note:
- When a message is sent to queue, it is redundantly distributed among SQS servers

## SQS - Auto Scaling

![](/images/aws/00-icons/sqs.png)
![](/images/arrow.png)
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

- Use target tracking scaling policy 
- Use a SQS metric like ApproximateNumberOfMessages

## SQS Queue - Important configuration
 
| Configuration | Description  | 
|--|:--|
|Visibility timeout| Other consumers will not receive a message being processed for the configured time period (default - 30 seconds, min - 0, max - 12 hours)  <BR/> Consumer processing a message can call ChangeMessageVisibility to increase visibility timeout of a message (before visibility timeout)|
| DelaySeconds   | Time period before a new message is visible on the queue <BR/>Delay Queue = Create Queue + Delay Seconds <BR/>default - 0, max - 15 minutes<BR/>Can be set at Queue creation or updated using SetQueueAttributes<BR/>Use message timers to configure a message specific DelaySeconds value      |
| Message retention period | Maximum period a message can be on the queue <BR/>Default - 4 days, Min - 60 seconds, Max - 14 days|
| MaxReceiveCount | Maximum number of failures in processing a message|

## Simple Queuing Service Security
![](/images/aws/00-icons/sqs.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/iam.png)

- You can provide access to other AWS resources to access SQS using IAM roles (EC2 -> SQS)
- By default only the queue owner is allowed to use the queue
	- Configure SQS Queue Access Policy to provide access to other AWS accounts

## SQS - Certification and Interview Questions

|Scenario | Result |
|--|:--|
|Consumer takes more than visibility timeout to process the message | Message is visible on queue after visibility timeout and another consumer might receive the message|
|Consumer calls ChangeMessageVisibility before visibility timeout | Visibility timeout is extended to requested time|
|DelaySeconds is configured on the queue| Message is delayed for DelaySeconds before it is available|
|Receiver wants to decide how to handle the message without looking at message body | Configure Message Attributes|
|How to reduce number of API calls to SQS?|Use Long Polling - When looking for messages, you can specify a WaitTimeSeconds upto 20 seconds|
|Your receive messages and start processing them after a week. You see that some messages are not processed at all!| Exceeded message retention period. Default message retention period is 4 days. Max 14 days.|
|Give high priority to premium customers| Create separate queues for free and premium customers|