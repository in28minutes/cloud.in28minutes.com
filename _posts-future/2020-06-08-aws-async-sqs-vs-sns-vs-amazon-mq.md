---
layout:     post
title:      SQS vs SNS vs Amazon MQ - Comparison - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of comparison between SQS vs SNS vs Amazon MQ.
categories:  AWS_CLOUD AWS_ASYNCHRONOUS
permalink:  /aws-certification-sqs-vs-sns-vs-amazon-mq
---

Let's get a quick overview of comparison between SQS vs SNS vs Amazon MQ. 

## You will learn
- Why do we need asynchronous communication?
- What are the different asynchronous communication options provided by AWS?
- What is SQS ?
- What is SNS?
- What is Amazon MQ?
- When do you use SQS vs SNS vs Amazon MQ?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## Synchronous Communication
Lets take an example of synchronous communication.
- Applications on your web server make synchronous calls to the logging service
- What if your logging service goes down?
	- Will you applications go down too?
- What if all of sudden, there is high load and there are lot of logs coming in?
	- Log Service is not able to handle the load and goes down very often
![](/images/aws/02-Queuing/0-SQS-00.png)

## Asynchronous Communication - Decoupled
How can we address the issue of synchronous communication?
- Create a queue or a topic
- Your applications put the logs on the queue
- They would be picked up when the logging service is ready
- Good example of decoupling!
![](/images/aws/02-Queuing/0-SQS-01.png)
## Asynchronous Communication - Scale up
![](/images/aws/02-Queuing/0-SQS-02.png)
- You can have multiple logging service instances reading from the queue!
## Asynchronous Communication - Pull Model - SQS
SQS is based on pull model. Lets look at the possibilities.
- Producers put messages on the queue
- Consumers poll on the queue
	- Only one of the consumers will successfully process a given message
- Scalability
	- Scale consumer instances under high load
- Availability
	- Producer up even if a consumer is down
- Reliability
	- Work is not lost due to insufficient resources
- Decoupling
	- Make changes to consumers without effect on producers worrying about them
![](/images/aws/02-Queuing/2-sqs.png)

## Simple Queuing Service
![](/images/aws/02-Queuing/2-sqs.png)
- Reliable, scalable, fully-managed message queuing service
- High availability
- Unlimited scaling
	- Auto scale to process billions of messages per day
- Low cost (Pay for use)

## Asynchronous Communication - Push Model - SNS
SNS is based on push model. Lets look how this works.
- Subscribers subscribe to a topic
- Producers send notifications to a topic
	- Notification sent out to all subscribers
- Decoupling
	- Producers don't care about who is listening
- Availability
	- Producer up even if a subscriber is down
![](/images/aws/02-Queuing/3-SNS.png)

## Amazon Simple Notification Service(SNS)
![](/images/aws/02-Queuing/3-SNS.png)
- Publish-Subscribe (pub-sub) paradigm
- Broadcast asynchronous event notifications
- Simple process
	- Create an SNS Topic
	- Subscribers can register for a Topic
	- When an SNS Topic receives an event notification (from publisher), it is broadcast to all Subscribers
- Use Cases : Monitoring Apps, workflow systems, mobile apps
- Provides mobile and enterprise messaging web services
	- Push notifications to Apple, Android, FireOS, Windows devices
	- Send SMS to mobile users
	- Send Emails
- REMEMBER : SNS does not need SQS or a Queue
- You can allow access to other AWS accounts using AWS SNS generated policy

## Amazon MQ
- Managed message broker service for Apache ActiveMQ
- (Functionally) Amazon MQ = Amazon SQS (Queues) + Amazon SNS (Topics)
	- BUT with restricted scalability
- Supports traditional APIs (JMS) and protocols (AMQP, MQTT, OpenWire, and STOMP)
	- Easy to migrate on-premise applications using traditional message brokers
	- Start with Amazon MQ as first step and slowly re-design apps to use Amazon SQS and/or SNS
- Scenario: An enterprise uses AMQP (standard message broker protocol). They want to migrate to AWS without making code changes 
	- Recommend Amazon MQ
