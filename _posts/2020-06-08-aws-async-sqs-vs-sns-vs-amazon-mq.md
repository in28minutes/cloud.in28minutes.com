---
layout:     post
title:      SQS vs SNS vs Amazon MQ - Comparison - AWS Certification Cheat Sheet
date:       2020-06-11 12:31:19
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

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>

## Synchronous Communication

Lets take an example of synchronous communication and the challenges with synchronous communication:

Applications on your web server make synchronous calls to the logging service.

![](/images/aws/02-Queuing/0-SQS-00.png)

Consider these situations:
- What if your logging service goes down?
	- Will you applications go down too?
- What if all of sudden, there is high load and there are lot of logs coming in?
	- Log Service is not able to handle the load and goes down very often

Two major concerns with the synchronous communications are:
- Tight Coupling
- Performance bottleneck & Inability to scale

## Asynchronous Communication - Decoupled

What is the best approach to solve these coupling and scaling issues? How about going asynchronous?
- Create a queue or a topic
- Your applications put the logs on the queue
- They would be picked up when the logging service is ready
- Good example of decoupling!

![](/images/aws/02-Queuing/0-SQS-01.png)

## Asynchronous Communication - Scale up

Amazing thing about the asynchronous communication is that it enables you scale up very easily.

You can have multiple logging service instances reading from the queue!

![](/images/aws/02-Queuing/0-SQS-02.png)

## Asynchronous Communication - Models
In asynchronous communication there are two possible models
- Pull Model - Consumers have to pull messages from the queue/topic
- Push Model - Messages are pushed to the various interested consumers

### Asynchronous Communication - Pull Model

Quick overview of the pull model:
- Producers put messages on the queue
- Consumers poll on the queue
	- Only one of the consumers will successfully process a given message

Here are the advantages of using SQS:
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

SQS is based on pull model. Here are some of the important features:
- Reliable, scalable, fully-managed message queuing service
- High availability
- Unlimited scaling
	- Auto scale to process billions of messages per day
- Low cost (Pay for use)

## Asynchronous Communication - Push Model - SNS

Here's a quick overview of the SNS approach:
- Subscribers subscribe to a topic
- Producers send notifications to a topic
	- Notification sent out to all subscribers

Here are the advantages of using SNS:
- Decoupling
	- Producers don't care about who is listening
- Availability
	- Producer up even if a subscriber is down

![](/images/aws/02-Queuing/3-SNS.png)

## Amazon Simple Notification Service(SNS)

SNS is based on push model. Here are some of the important features:
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

Amazon MQ is a managed message broker service for Apache ActiveMQ.

Here are some of the important features:
- (Functionally) Amazon MQ = Amazon SQS (Queues) + Amazon SNS (Topics)
	- BUT with restricted scalability
- Supports traditional APIs (JMS) and protocols (AMQP, MQTT, OpenWire, and STOMP)
	- Easy to migrate on-premise applications using traditional message brokers
	- Start with Amazon MQ as first step and slowly re-design apps to use Amazon SQS and/or SNS
- Scenario: An enterprise uses AMQP (standard message broker protocol). They want to migrate to AWS without making code changes 
	- Recommend Amazon MQ
