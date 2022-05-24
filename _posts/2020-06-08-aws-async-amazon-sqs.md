---
layout:     post
title:      Amazon SQS - Simple Queuing Service - FIFO vs Standard Queue - AWS Certification Cheat Sheet
date:       2020-06-10 12:31:19
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
- What are the steps involved in processing a message from Amazon SQS queue?
- How do you implement auto scaling with CloudWatch Alarms for SQS Queue?

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>

## Simple Queuing Service

Simple Queuing Service is a highly reliable, scalable, fully-managed message queuing service.

Here are some of the important features:
- High availability
- Unlimited scaling
	- Auto scale to process billions of messages per day
- Low cost (Pay for use)

![](/images/aws/02-Queuing/2-sqs.png)


## Two Types of Simple Queuing Service Queues

There are Two Types of Simple Queuing Service Queues:
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

Choose between Two Types of Simple Queuing Service Queues
- Standard SQS queue if throughput is important
- FIFO Queue if order of events is important

## Sending and receiving a SQS Message - Best case scenario

![](/images/aws/02-Queuing/sqs-simple-flow.png)

Let's see the steps involved in sending and receiving a message on the SQS queue:
- Step I: Producer places message on queue 
	- Receives globally unique message ID ABCDEFGHIJ (used to track the message)
- Step II: Consumer polls for messages 
	- Receives the message ABCDEFGHIJ along with a receipt handle XYZ
- Step III: Message remains in the queue while the consumer processes the message
	- Other consumers will not receive ABCDEFGHIJ even if they poll for messages
- Step IV: Consumer processes the message successfully 
	- Calls delete message (using receipt handle XYZ)
	- Message is removed from the queue

## Simple Queuing Service Lifecycle of a message

The picture below shows the service lifecycle of a message

![](/images/aws/02-Queuing/4-Queuing-LifeCycle.png)

When a message is sent to queue, it is redundantly distributed among SQS servers

## SQS - Auto Scaling

You can also implement auto scaling for your SQS queue using CloudWatch based on number of messages in the queue.

![](/images/aws/00-icons/sqs.png)
![](/images/arrow.png)
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

Recommendations:
- Use target tracking scaling policy 
- Use a SQS metric like ApproximateNumberOfMessages

## SQS Queue - Important configuration
 
The table below shows some of the important SQS queue configuration:

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

Here are the important things to consider about security of the SQS queue:
- You can provide access to other AWS resources to access SQS using IAM roles (EC2 -> SQS)
- By default only the queue owner is allowed to use the queue
	- Configure SQS Queue Access Policy to provide access to other AWS accounts

## SQS - Certification and Interview Questions

Let's look a few scenarios regarding SQS.

|Scenario | Result |
|--|:--|
|Consumer takes more than visibility timeout to process the message | Message is visible on queue after visibility timeout and another consumer might receive the message|
|Consumer calls ChangeMessageVisibility before visibility timeout | Visibility timeout is extended to requested time|
|DelaySeconds is configured on the queue| Message is delayed for DelaySeconds before it is available|
|Receiver wants to decide how to handle the message without looking at message body | Configure Message Attributes|
|How to reduce number of API calls to SQS?|Use Long Polling - When looking for messages, you can specify a WaitTimeSeconds upto 20 seconds|
|Your receive messages and start processing them after a week. You see that some messages are not processed at all!| Exceeded message retention period. Default message retention period is 4 days. Max 14 days.|
|Give high priority to premium customers| Create separate queues for free and premium customers|