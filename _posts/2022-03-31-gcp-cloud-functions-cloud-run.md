---
layout:     post
title:      GCP Cloud Functions and Cloud Run - GCP Certification Cheat Sheet
date:       2022-03-31 00:00:00
summary:    Let's get a quick overview of Google Cloud Functions & Cloud Run
categories:  GCP_COMPUTE
permalink:  /gcp-certification-google-cloud-functions-cloud-run
---

Let's get a quick overview of Google Cloud Functions & Google Cloud Run from an GCP certification perspective. We will look at important certification questions regarding Cloud Functions and Cloud Run 

## You will learn
- What is Cloud Functions & Cloud Run?
- Why it is important and how to set it up?
- Commands Cheatsheet

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>

# Google Cloud Functions

## Cloud Functions
![](./gcpimages/00-icons/gcp/functions.png)
- Imagine you want to **execute some code when an event happens**?
	- A file is uploaded in Cloud Storage 
	- An error log is written to Cloud Logging
	- A message arrives to Cloud Pub/Sub
- Enter **Cloud Functions**
    - **Serverless compute service** offered by GCP
	- **Run code in response to events**
		- Write your business logic in  Node.js, Python, Go, Java, .NET, and Ruby
		- **Don't worry** about servers or scaling or availability (only worry about your code)
	- **Pay only for what you use**
		- Number of invocations
		- Compute Time of the invocations
		- Amount of memory and CPU provisioned
	- **Time Bound** - Default 1 min and MAX 9 minutes(540 seconds)
	- **Each execution runs in a separate instance**
		- No direct sharing between invocations

## AppEngine vs Cloud Functions 

- Both are **Serverless compute services**
- App Engine is best suited for 
    - An application consists of multiple services/components
    - Like Web UI, Rest API's, Business Logic Services
    - These components together make up an Application
    - Helps to treat such applications as **single unit**
- Cloud Functions is best suited for
    - An action to happen based on some events in GCP
    - These actions are individual actions and should be managed independent
    - **Cloud Functions** allows to decouple events handling    

## Cloud Functions - Concepts
![](./gcpimages/00-icons/gcp/functions.png)
- **Event** : Upload object to cloud storage
- **Trigger**: Respond to event with a Function call
	- **Trigger** - Which function to trigger when an event happens?
	- **Functions** - Take event data and perform action?
- Events are **triggered from**
	- Cloud Storage
	- Cloud Pub/Sub
	- HTTP POST/GET/DELETE/PUT/OPTIONS
	- Firebase
	- Cloud Firestore
	- Stack driver logging

## Example Cloud Function - HTTP - Node.js

```
const escapeHtml = require('escape-html');

/**
 * HTTP Cloud Function.
 *
 * @param {Object} req Cloud Function request context.
 *                     More info: https://expressjs.com/en/api.html#req
 * @param {Object} res Cloud Function response context.
 *                     More info: https://expressjs.com/en/api.html#res
 */
exports.helloHttp = (req, res) => {
  res.send(`Hello ${escapeHtml(req.query.name || req.body.name || 'World')}!`);
};
```

## Example Cloud Function - Pub/Sub - Node.js

```
/**
 * Background Cloud Function to be triggered by Pub/Sub.
 * This function is exported by index.js, and executed when
 * the trigger topic receives a message.
 *
 * @param {object} message The Pub/Sub message.
 * @param {object} context The event metadata.
 */
exports.helloPubSub = (message, context) => {
  const name = message.data
    ? Buffer.from(message.data, 'base64').toString()
    : 'World';

  console.log(`Hello, ${name}!`);
};
```

## Cloud Functions - From the Command Line

| Description | Command |
|:--|:--|
|Deploy a new Cloud Funtion|*gcloud **functions deploy** FUNCTION_NAME --runtime python37 --trigger-resource TRIGGER_RESOURCE --trigger-event TRIGGER_EVENT|
|List available events|gcloud **functions event-types** list|
|Call a function|gcloud **functions call** FUNCTION_NAME  --data='{"message":"test"}'|
|Delete a function in a given region|gcloud **functions delete** FUNCTION_NAME  --region=REGION|

## Cloud Functions - Remember

![](./gcpimages/00-icons/gcp/functions.png)
- No Server Management: You dont need to worry about scaling or availability of your function
- Cloud Functions automatically spin up and back down in response to events
	- They scale horizontally!
- Cloud Functions are recommended for responding to events:
	- Cloud Functions are NOT ideal for long running processes
		- **Time Bound** - Default 1 min and MAX 9 minutes(540 seconds)

## Cloud Run & Cloud Run for Anthos
![](./gcpimages/gcp/cloud-run.png)
- **Cloud Run** - "Container to Production in Seconds"
	- Built on top of an open standard - **Knative**
	- **Fully managed** serverless platform for containerized applications
		- ZERO infrastructure management
		- Pay-per-use (For used CPU, Memory, Requests and Networking)
- Fully integrated **end-to-end developer experience**:
	- **No limitations** in languages, binaries and dependencies
	- Easily portable because of **container** based architecture
	- Cloud Code, Cloud Build, Cloud Monitoring & Cloud Logging Integrations
- **Anthos** -  Run Kubernetes clusters anywhere
	- Cloud, Multi Cloud and On-Premise
- **Cloud Run for Anthos**: Deploy your workloads to Anthos clusters running on-premises or on Google Cloud
	- Leverage your existing Kubernetes investment to quickly run serverless workloads

## Cloud Run - From the Command Line

| Description | Command |
|:--|:--|
|Deploy a new container|*gcloud **run deploy** SERVICE_NAME --image IMAGE_URL --revision-suffix v1*<BR/> First deployment creates a service and first revision <BR/> Next deployments for the same service create new revisions|
|List available revisions|gcloud **run revisions** list|
|Adjust traffic assignments|gcloud **run services update-traffic** myservice  --to-revisions=v2=10,v1=90|