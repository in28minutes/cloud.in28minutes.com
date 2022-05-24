---
layout:     post
title:      GCP PubSub - GCP Certification Cheat Sheet
date:       2022-05-06 00:00:00
summary:    Let's get a quick overview of Google Cloud PubSub
categories:  GCP_CLOUD
permalink:  /gcp-certification-google-cloud-pubsub
---


Let's get a quick overview of Google Cloud PubSub from an GCP certification perspective. We will look at important certification questions related to PubSub and how it enables asynchronous message processing in GCP. 

## You will learn
- What is PubSub?
- What are the features of PubSub and important concepts
- Commands Cheatsheet

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>

# Decoupling Applications <BR/>with Pub/Sub


## Need for Asynchronous Communication
- Why do we need asynchronous communication?


## Synchronous Communication
![](./gcpimages/02-Queuing/0-SQS-00.png)
- Applications on your web server make synchronous calls to the logging service
- What if your logging service goes down?
	- Will you applications go down too?
- What if all of sudden, there is high load and there are lot of logs coming in?
	- Log Service is not able to handle the load and goes down very often


## Asynchronous Communication - Decoupled
![](./gcpimages/02-Architecture/0-SQS-1.png)
- Create a topic and have your applications put log messages on the topic
- Logging service picks them up for processing when ready
- Advantages:
	- Decoupling: Publisher (Apps) don't care about who is listening
	- Availability: Publisher (Apps)  up even if a subscriber (Logging Service) is down
	- Scalability: Scale consumer instances (Logging Service) under high load
	- Durability: Message is not lost even if subscriber (Logging Service) is down


## Pub/Sub

![](./gcpimages/00-icons/gcp/pub-sub.png)
- Reliable, scalable, fully-managed asynchronous messaging service
- Backbone for **Highly Available** and **Highly Scalable** Solutions
	- Auto scale to process billions of messages per day
	- Low cost (Pay for use)
- Usecases: Event ingestion and delivery for streaming analytics pipelines
- Supports push and pull message deliveries


## Pub/Sub - How does it work?

![](./gcpimages/02-architecture/00-pubsub-usecases.png)
- **Publisher** - Sender of a message
	- Publishers send messages by making HTTPS requests to pubsub.googleapis.com
- **Subscriber** - Receiver of the message
	- **Pull** - Subscriber pulls messages when ready
		- Subscriber makes HTTPS requests to pubsub.googleapis.com
	- **Push** - Messages are sent to subscribers
		- Subscribers provide a web hook endpoint at the time of registration
		- When a message is received on the topic, A HTTPS POST request is sent to the web hook endpoints
- **Very Flexible** Publisher(s) and Subscriber(s) Relationships: One to Many, Many to One, Many to Many


## Pub/Sub - Getting Ready with Topic and Subscriptions

![](./gcpimages/02-architecture/00-pubsub-usecases.png)
- Step 1 : Topic is created
- Step 2 : Subscription(s) are created 
	- Subscribers register to the topic
	- Each Subscription represents discrete pull of messages from a topic:
		- Multiple clients pull same subscription => messages split between clients
		- Multiple clients create a subscription each => each client will get every message


## Pub/Sub - Sending and Receiving a Message

![](./gcpimages/02-Architecture/00-pubsub-messageflow.png)
- Publisher sends a message to Topic
- Message **individually** delivered to each and every subscription
	- Subscribers can receive message either by:
		- Push: Pub/Sub sends the message to Subscriber
		- Pull: Subscribers poll for messages
- Subscribers send acknowledgement(s)
- Message(s) are removed from subscriptions message queue
	- Pub/Sub ensures the message is retained **per subscription** until it is acknowledged


## Managing Pub/Sub

![](./gcpimages/00-icons/gcp/pub-sub.png)
- Pub/Sub **pubsub**
	- *gcloud pubsub **topics create** my-topic*
	- *gcloud pubsub **subscriptions create** my-subscription --topic=my-topic*
		- **--enable-message-ordering** - ordered message delivery
		- **--ack-deadline** - how long to wait for acknowledgment?
		- **--message-filter** - criteria to filter messages
	- *gcloud pubsub **subscriptions pull** my-subscription*
		- *--auto-ack --limit*
	- *gcloud pubsub **subscriptions ack** my-subscription --ack-ids=[ACK_ID,…]*
	- Topic: ***gcloud pubsub topics***
		- *gcloud pubsub topics **delete** my-topic*
		- *gcloud pubsub topics **list***
		- *gcloud pubsub topics **list-subscriptions** my-topic*
