---
layout:     post
title:      Google Cloud Functions - GCP Certification Cheat Sheet
date:       2021-12-06 11:13:00
summary:    Let's get a quick overview of Google Cloud Functions from an GCP certification perspective. We will look at important certification questions regarding Google Cloud Functions.
categories:  GCP_General
permalink:  /gcp-cloud-functions
---

Let's get a quick overview of Google Cloud Functions from an GCP certification perspective. We will look at important certification questions regarding Google Cloud Functions.

![functions](https://user-images.githubusercontent.com/57451228/144843382-f39261ea-fb00-4657-8d98-84b1ca983493.png)


## You will learn
- What is a Google Cloud Functions?
- Why do we need Google Cloud Functions?
- Advantage Google Cloud Functions?

## Google Cloud Functions - Need

Why do we need Google Cloud Functions?
Let's first understand that with a simple scenario.

Imagine you want to **execute some code when an event happens?**
- A file is uploaded in Cloud Storage
- An error log is written to Cloud Logging
- A message arrives to Cloud Pub/Sub

## Enter Cloud Functions
- **Run code in response to events**
  - Write your business logic in Node.js, Python, Go, Java, .NET, and Ruby
  - Don't worry about servers or scaling or availability (only worry about your code)
- Pay only for what you use
  - Number of invocations
  - Compute Time of the invocations
  - Amount of memory and CPU provisioned
- **Time Bound** - Default 1 min and MAX 9 minutes(540 seconds)
- **Each execution runs in a separate instance**
  - No direct sharing between invocations

## Cloud Functions - Concepts

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

```sh
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

```sh
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
## Cloud Functions - Images
<BR/>

![Screenshot 2021-12-06 at 5 38 18 PM](https://user-images.githubusercontent.com/57451228/144843637-cbcadf25-a3f7-438d-9951-9e254c281828.png)

<BR/>


![Screenshot 2021-12-06 at 5 38 48 PM](https://user-images.githubusercontent.com/57451228/144843655-fc252fd5-8d17-4091-a158-321e3313fd48.png)

<BR/>

## Cloud Functions - Advantages

- No Server Management: You dont need to worry about scaling or availability of your function
- Cloud Functions automatically spin up and back down in response to events
  - They scale horizontally!
- Cloud Functions are recommended for responding to events:
  - Cloud Functions are NOT ideal for long running processes
    - Time Bound - Default 1 min and MAX 9 minutes(540 seconds)

<BR/>


<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
