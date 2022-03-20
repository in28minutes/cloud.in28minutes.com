---
layout:     post
title:      Google cloud pubsub - For Architects - Google cloud certification
date:       2022-02-18 21:06:00
summary:    Let's understand the google cloud pubsub with the help of a sample application
categories:  GOOGLE_CLOUD PUBSUB
permalink:  /google-cloud-certification-pubsub-sendreceive
---

In this tutorial, you'll learn how to create a simple python flask application and integrate it with a cloud pubsub (publisher and subscriber).

![](/images/googlecloud/cloud_pubsub.png)

# Requirements

- Python, Flask
- Google cloud account
- [Google cloud sdk](https://cloud.google.com/sdk/docs/install)
- [Google Cheat Sheet](https://cloud.google.com/sdk/docs/images/gcloud-cheat-sheet.pdf)

# Example Code

This tutorial is accompanied by a working code example [on Github](https://github.com/in28minutes/cloud.in28minutes.com/tree/master/projects/google-cloud-content/pubsub-sendreceive). The application exposes the 2 endpoints with the help of the flask framework to send a message to the topic and receive messages from the subscription attached to a topic. 

# Getting Started

## 1. Create Python application

- Create a folder named `PythonAppWithPubsub` on your desired drive. You will be storing all the files in this folder
- I would recommend using the [Community version PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=windows) for the development of the application

### 1.1 requirements.txt

Let us start creating the application by installing the required dependencies. Run the following command - <code>pip install -r requirements.txt</code> in your terminal shell to download the required dependencies

```plain
Flask
google-cloud
google-api-core
google-api-python-client
google-cloud-core
google-cloud-pubsub
```

### 1.2 Pre-requisite

To work with this tutorial one needs to have a topic and a subscription attached to this topic. You can either create a topic and subscription via the Google cloud console or can programmatically create them by referring to this tutorial.

### 1.3 sendreceive.py

Create a file responsible to interact with the cloud pubsub and perform the required operations. The file exposes 2 different endpoints that will help to send a message to the topic and receive the message from the subscription attached to that topic. Remember to update the topic and subscription name with the ones created in step1.2 in the below file. For the simplicity of this tutorial, I am not taking any input from the user to send to the queue but you're free to change it to HTTP post endpoint and make the necessary changes to the code. Similarly, the other HTTP get endpoint when triggered is responsible to pull the messages from the subscription and print it on the console.

```python
import logging
import os
import random

import google.cloud.pubsub_v1
from flask import Flask

# [logging config
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
# logging config]

app = Flask(__name__)
app.secret_key = 'somesecretkey'

topic_path = 'MY_TOPIC_PATH_HERE'
subscription_path = 'MY_SUBSCRIPTION_PATH_HERE'


# http://localhost:5000/send
@app.route('/send', methods=['GET'])
def send():
    """Send"""
    logging.info('Sending message to topic [%s]', topic_path)
    num = random.random()
    data = 'Hello world ' + str(num)
    data = data.encode('utf-8')

    publisher = google.cloud.pubsub_v1.PublisherClient()
    future = publisher.publish(topic_path, data)
    logging.info('Message sent')
    return {
        'status': 'ok',
        'msg': future.result()
    }


# http://localhost:5000/receive
@app.route('/receive', methods=['GET'])
def receive():
    """Receive message from pull subscription"""
    logging.info('Listening messages from subscription [%s]', subscription_path)
    subscriber = google.cloud.pubsub_v1.SubscriberClient()
    pull = subscriber.subscribe(subscription_path, callback)
    with subscriber:  # wrap subscriber 'with' block to automatically call close() when done
        try:
            pull.result(timeout=5)  # block with a timeout
        except TimeoutError:
            pull.cancel()  # trigger the shutdown
            pull.result()  # block until shutdown is complete


def callback(message):
    logging.info('Received message [%s]', message)
    logging.info('Data [%s]', message.data)
    message.ack()


# driver code
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5000')
    app.run(debug=False, port=server_port, host='0.0.0.0')
```

## 2. Run the application

After successfully developing the application let us start the application by running the <code>sendreceive.py</code> file. Once the application is started successfully head over to the browser of your choice and enter the following endpoint - `http://localhost:5000` to play with the application.

"If you feel like something needs to add or changed feel free to connect with us with the slack community or drop us an email at - support@in28minutes.com"
