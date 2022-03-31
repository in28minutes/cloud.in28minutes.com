---
layout:     post
title:      GCP Kubernetes Engine - GCP Certification Cheat Sheet
date:       2022-03-31 00:00:00
summary:    Let's get a quick overview of Google Cloud Functions & Cloud Run
categories:  GCP_CLOUD General
permalink:  /gcp-certification-google-cloud-functions-cloud-run
---

Let's get a quick overview of Google Cloud Functions & Google Cloud Run from an GCP certification perspective. We will look at important certification questions regarding <> 

## You will learn
- What is Cloud Functions & Cloud Run?
- Why it is important and how to set it up?
- Commands Cheatsheet

## GCP Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

# Google Cloud Functions

## Cloud Functions
![](./images/00-icons/gcp/functions.png)
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
![](./images/00-icons/gcp/functions.png)
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

![](./images/00-icons/gcp/functions.png)
- No Server Management: You dont need to worry about scaling or availability of your function
- Cloud Functions automatically spin up and back down in response to events
	- They scale horizontally!
- Cloud Functions are recommended for responding to events:
	- Cloud Functions are NOT ideal for long running processes
		- **Time Bound** - Default 1 min and MAX 9 minutes(540 seconds)

## Cloud Run & Cloud Run for Anthos
![](./images/gcp/cloud-run.png)
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

---
Question: You have a application that should process the messages comes from the Pub/Sub and update the CloudSQL DB. You would like to run this as Cloud Run application. To integrate with Pub/Sub what is the best possible solution from the given options?
1. Integrate Cloud Run directly with Pub/Sub. Run the command **gcloud pubsub subscriptions create myRunSubscription --topic myRunTopic --push-endpoint=SERVICE-URL**. This creates a subscription and whenever message is received, it automatically published to the SERICE-URL your application is exposing.
2. Create a Cloud Function which gets triggered whenever message received in the Pub/Sub. Write a logic in the Cloud Function which invokes the SERVICE-URL with the contents of the message
3. Create a Service Account. Assign the role roles/run.invoker to this Service Account for this Cloud Run application. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the Service Account.
4. Create a Service Account. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the Service Account.

Ans Option 3: Create a service account. Assign the role roles/run.invoker to this service account for this Cloud Run application. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the service account. is the correct answer. For the integration to work, the best way to do this is through a service account and assigning the run.invoker role for the service sccount. More details are here https://cloud.google.com/run/docs/tutorials/pubsub#integrating-pubsub.
Option 4 Create a Service Account. Also allow Pub/Sub to create authentication tokens on the project of the Cloud Run application. Create the Pub/Sub subscription with the service account. is not correct as this solution missing the assignment of roles/run.invoker to the service account.
Option 1 Integrate Cloud Run directly with Pub/Sub. Run the command **gcloud pubsub subscriptions create myRunSubscription --topic myRunTopic --push-endpoint=SERVICE-URL**. This creates a subscription and whenever message is received, it automatically published to the SERICE-URL your application is exposing. is not correct. This gcloud command has an option to specific service account which needs to be created as explained in the option 3. 
---
Question: You are creating an application as Cloud Function which creates a Thumbnail for the images uploaded in the Cloud Storage. You notice that, for some of the bigger images were not processed correctly. What could be the cause of the problems?
1. The timeout settings for the Cloud Function is too low to process larget images
2. Copying larger images takes more time so the trigger function is not correctly working
3. To process larger images, the role roles/function.processLargeImage should be assigned to the function
4. The Cloud Function has a defect when processing larger images which cause the processing to fail.

Ans: **Option 1: The timeout settings for the Cloud Function is too low to process large images** is the correct answer. 
Option 2: Copying larger images takes more time so the trigger function is not correctly working is not correct as triggering will happen irrespective of size of the file. 
Option 3: To process larger images, the role roles/function.processLargeImage should be assigned to the function is not correct as there is no role called roles/function.processLargeImage
Option 4: The Cloud Function has a defect when processing larger images which cause the processing to fail. is not correct
---
Question: What is the default timeout settings for the Cloud Funtion?
1. 1 minute
2. 10 minute
3. 5 minute
4. 9 minute

Ans Option 1: 1 minute is the default timeout settings for the Cloud Function. 9 minute is the maximum
All other options are invalid.
---
Question: What is the maximum timeout settings for the Cloud Funtion?
1. 1 minute
2. 10 minute
3. 5 minute
4. 9 minute

Ans Option 4: 9 minute is the maximum timeout settings for the Cloud Function. 1 minute is the default timeout settings.
All other options are invalid.
---
Question: Which one of the following GCP resources can NOT generate events that can trigger a Cloud Function?
1. Cloud Pub/Sub
2. Cloud Logging
3. Cloud Storage
4. Cloud SQL

Ans Option 4: is the correct answer. The Cloud Functions supports events from the following providers
HTTP
Cloud Storage
Cloud Pub/Sub
Cloud Firestore
Firebase (Realtime Database, Storage, Analytics, Auth)
Cloud Logging—forward log entries to a Pub/Sub topic by creating a sink. You can then trigger the function.
So Cloud SQL is the only resource that is not supported.
---
Question: You are a GCP architect working for a major retail customer. Many of your applications use Cloud Spanner as the backend DB. However Cloud Spanner does not automatically adjust the size of the instance when the workload changes. You are tasked with designing the solution for this problem. What would be the best solution?
1. Use a Cloud Scheduler to monitor the metrics of the Cloud Spanner instances. Use the same scheduler to adjust the instance size accordingly.
2. Use Cloud Monitor to monitor the metrics of the various Cloud Spanner instances. Send email to the operations team when threshold exceeds to let them handle the sizing accordingly.
3. Using Cloud Function query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Function to send request to Cloud Spanner to scale up or down.
4. Use Cloud Run to query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Run to send request to Cloud Spanner to scale up or down.
Ans Option 4: Using Cloud Function query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Function to send request to Cloud Spanner to scale up or down. is correct and little bit better compared to other options. An architecture note on the Google Architecture Center explains this architecture https://cloud.google.com/architecture/autoscaling-cloud-spanner
Option 1: Use a Cloud Scheduler to monitor the metrics of the Cloud Spanner instances. Use the same scheduler to adjust the instance size accordingly. is not correct. 
Option 2: Use Cloud Monitor to monitor the metrics of the various Cloud Spanner instances. Send email to the operations team when threshold exceeds to let them handle the sizing accordingly. is not correct as sending e-mails to the operations team is not efficient as this is manual.
Option 4: Use Cloud Run to query the Cloud Monitoring metrics of the Cloud Spanner instances. Use this Cloud Run to send request to Cloud Spanner to scale up or down. is not correct because in this architecture, Cloud Run has to continuously run all the time. In case of Cloud Functions, it can run on a predetermined interval to check the metrics and act accordingly. 
---
Question: You would like to create Cloud Function which reads the file contents as soon as it gets uploaded in the Cloud Storage. You would like to start the process only after the file gets completely uploaded becasue some files could be big. Which Cloud Storage trigger you should use to start the process?
1. google.storage.object.finalize
2. google.storage.object.complete
3. google.storage.object.upload
4. google.storage.object.finalized
Ans Option 1: google.storage.object.finalize is the correct option. This event is sent when a new object is created. 
There are only 4 valid events for the Cloud Storage. 
google.storage.object.finalize (default)
google.storage.object.delete - This event is sent when an object is permanently deleted
google.storage.object.archive - This event is sent when a live version of an object is archived or deleted.
google.storage.object.metadataUpdate - This event is sent when the metadata of an existing object changes.
All other options are invalid.
---
Question: You are using Cloud Storage to store employees identification documents. You would like to create a Cloud Function based on the event that the document gets deleted or updated for some reason. The versioning on the bucket is not enabled. Which Cloud Storage trigger you should use to start the process?
1. google.storage.object.finalize
2. google.storage.object.delete
3. google.storage.object.archive
4. google.storage.object.metadataUpdate
Ans Option 2: google.storage.object.delete is the correct option. This event is sent when an object is permanently deleted. 
There are only 4 valid events for the Cloud Storage. 
google.storage.object.finalize (default)
google.storage.object.delete - This event is sent when an object is permanently deleted. However this depends on the versioning setting for the bucket.
Depending on the object versioning setting for a bucket this means:
For versioning buckets, this is only sent when a version is permanently deleted (but not when an object is archived).
For non-versioning buckets, this is sent when an object is deleted or overwritten.
Option 3 google.storage.object.archive is not correct- This event is sent when a live version of an object is archived or deleted. This event is only sent for versioning buckets.
Option 4 google.storage.object.metadataUpdate is not correct - This event is sent when the metadata of an existing object changes. This event is sent when the metadata of an existing object changes.
---
Question: You are using Cloud Storage to store employees identification documents. You would like to create a Cloud Function based on the event that the live version of the document gets archived or deleted for some reason. The versioning on the bucket is enabled. Which Cloud Storage trigger you should use to start the process?
1. google.storage.object.finalize
2. google.storage.object.delete
3. google.storage.object.archive
4. google.storage.object.metadataUpdate
Ans Option 3: google.storage.object.archive is the correct option. This event is sent when an object is permanently deleted. 
There are only 4 valid events for the Cloud Storage. 
google.storage.object.finalize (default)
google.storage.object.delete - This event is sent when an object is permanently deleted. However this depends on the versioning setting for the bucket.
Depending on the object versioning setting for a bucket this means:
For versioning buckets, this is only sent when a version is permanently deleted (but not when an object is archived).
For non-versioning buckets, this is sent when an object is deleted or overwritten.
Option 3 google.storage.object.archive is not correct- This event is sent when a live version of an object is archived or deleted. This event is only sent for versioning buckets.
Option 4 google.storage.object.metadataUpdate is not correct - This event is sent when the metadata of an existing object changes. This event is sent when the metadata of an existing object changes.
----