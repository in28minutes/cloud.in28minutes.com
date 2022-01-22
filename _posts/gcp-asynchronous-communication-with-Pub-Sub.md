---
layout:     post
title:      Decoupling Applications with Pub/Sub - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Decoupling Applications with Pub/Sub in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Decoupling Applications with Pub/Sub in Google Cloud Platform.
categories:  GCP_General GCP_Pub_Sub
permalink:  /gcp-decoupling-applications-with-pub-sub
---
Let's get a quick overview of Decoupling Applications with Pub/Sub in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Decoupling Applications with Pub/Sub in Google Cloud Platform.


## You will learn

- Need for Asynchronous Communication
- Synchronous Communication
- Asynchronous Communication - Decoupled
- What is Pub/Sub
- Pub/Sub - How does it work?
- Pub/Sub - Getting Ready with Topic and Subscriptions
- Pub/Sub - Sending and Receiving a Message
- Managing Pub/Sub


## Synchronous Communication

![0-SQS-00](https://user-images.githubusercontent.com/57451228/150635817-181e3a94-cd75-44c8-99ba-42024971418d.png)



- Applications on your web server make synchronous calls to the logging service
- What if your logging service goes down?
  - Will you applications go down too?
- What if all of sudden, there is high load and there are lot of logs coming in?
  - Log Service is not able to handle the load and goes down very often


## Asynchronous Communication - Decoupled

![0-SQS-1](https://user-images.githubusercontent.com/57451228/150635826-8fd3336d-bb8f-444a-b329-fff28a6ac5eb.png)


- Create a topic and have your applications put log messages on the topic
- Logging service picks them up for processing when ready
- Advantages:
  - Decoupling: Publisher (Apps) don't care about who is listening
  - Availability: Publisher (Apps) up even if a subscriber (Logging Service) is down
  - Scalability: Scale consumer instances (Logging Service) under high load
  - Durability: Message is not lost even if subscriber (Logging Service) is down

## Pub/Sub

![pub-sub](https://user-images.githubusercontent.com/57451228/150635845-03b25e68-1057-4448-802d-f2ce97792b60.png)

- Reliable, scalable, fully-managed asynchronous messaging service
- Backbone for **Highly Available** and **Highly Scalable Solutions**
  - Auto scale to process billions of messages per day
  - Low cost (Pay for use)
- Usecases: Event ingestion and delivery for streaming analytics pipelines
- Supports push and pull message deliveries


## Pub/Sub - How does it work?

![00-pubsub-usecases-1](https://user-images.githubusercontent.com/57451228/150636086-9cefd8b2-e75b-4a9d-a488-a73542b253c6.png)



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

![00-pubsub-usecases](https://user-images.githubusercontent.com/57451228/150636048-383c014a-9745-416f-b9fb-59516c0065cf.png)



- Step 1 : Topic is created
- Step 2 : Subscription(s) are created
  - Subscribers register to the topic
  - Each Subscription represents discrete pull of messages from a topic:
     - Multiple clients pull same subscription => messages split between clients
     - Multiple clients create a subscription each => each client will get every message



## Pub/Sub - Sending and Receiving a Message

![00-pubsub-messageflow](https://user-images.githubusercontent.com/57451228/150635984-a1836913-2224-4955-9e70-30dcb22f93e7.png)




- Publisher sends a message to Topic
- Message **individually** delivered to each and every subscription
  - Subscribers can receive message either by:
     - Push: Pub/Sub sends the message to Subscriber
     - Pull: Subscribers poll for messages
- Subscribers send acknowledgement(s)
- Message(s) are removed from subscriptions message queue
  - Pub/Sub ensures the message is retained **per subscription** until it is acknowledged


## Managing Pub/Sub

- Pub/Sub **pubsub**
  - gcloud pubsub **topics create** my-topic
  - gcloud pubsub **subscriptions create** my-subscription --topic=my-topic
     - **--enable-message-ordering **- ordered message delivery
     - **--ack-deadline** - how long to wait for acknowledgment?
     - **--message-filter** - criteria to filter messages
  - gcloud pubsub subscriptions pull my-subscription
     - --auto-ack --limit
  - gcloud pubsub **subscriptions ack** my-subscription --ack-ids=[ACK_ID,…]
  - Topic: gcloud pubsub topics
     - gcloud pubsub topics **delete** my-topic
     - gcloud pubsub topics **list**
     - gcloud pubsub topics **list-subscriptions** my-topic




<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
