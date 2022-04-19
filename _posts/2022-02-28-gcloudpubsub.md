---
layout:     post
title:      Google cloud pubsub - For Architects - Google cloud certification
date:       2022-02-13 21:06:00
summary:    Let's understand the google cloud pubsub with the help of a sample application
categories:  GOOGLE_CLOUD PUBSUB
permalink:  /google-cloud-certification-pubsub
---

In this tutorial, you'll learn how to create a simple python flask application and integrate it with a cloud pubsub (publisher and subscriber).

![](/images/googlecloud/cloud_pubsub.png)

# Requirements

- Python, Flask
- Google cloud account
- [Google cloud sdk](https://cloud.google.com/sdk/docs/install)
- [Google Cheat Sheet](https://cloud.google.com/sdk/docs/images/gcloud-cheat-sheet.pdf)

# Example Code

This tutorial is accompanied by a working code example [on Github](https://github.com/in28minutes/cloud.in28minutes.com/tree/master/projects/google-cloud-content/pubsub). The application exposes the 2 endpoints with the help of the flask framework to create the topic and subscription and list the required details. For accepting the user inputs I will create different html pages as per the use case.

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

### 1.2 main.py

Create a file responsible to interact with the cloud pubsub and perform the required operations. The file exposes 2 different endpoints that correspond to an html page. The <code>/</code> endpoint is a get and post endpoint to return the form.html page responsible to accept the user input for creating the topic and subscription. Similarly, the <code>/list</code> endpoint is a get and post endpoint responsible to get the user's choice and display the result accordingly. You're free to change the application as per your wish

```python
import logging
import os

import google.api_core.exceptions
import google.cloud.pubsub_v1
import google.pubsub_v1
from flask import Flask, render_template, request, flash, redirect

# [logging config
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
# logging config]

app = Flask(__name__)
app.secret_key = 'somesecretkey'


# http://localhost:5000
@app.route('/', methods=['GET'])
def index():
    """Index."""
    logging.info('Showing index page')
    return render_template('form.html')


@app.route('/', methods=['POST'])
def create():
    """Create topic and subscription."""
    project_id = request.form.get('project')
    topic_id = request.form.get('topic')
    subscription_id = request.form.get('subscription')
    logging.info('Creating topic and subscription in project id= [%s]', project_id)

    if project_id == '' or topic_id == '' or subscription_id == '':
        logging.info('Topic or subscription cannot be blank')
        flash('Topic or subscription cannot be empty')
        return redirect(request.url)
    else:
        try:
            logging.info('Creating topic [%s]', topic_id)
            publisher = google.cloud.pubsub_v1.PublisherClient()
            topic_path = publisher.topic_path(project_id, topic_id)
            response = publisher.create_topic(request={'name': topic_path})
            # logging.info(response)
            logging.info('Topic created [%s]', response.name)

            logging.info('Creating subscription [%s]', subscription_id)
            subscriber = google.cloud.pubsub_v1.SubscriberClient()
            subscription_path = subscriber.subscription_path(project_id, subscription_id)
            with subscriber:
                api_request = {
                    'name': subscription_path,
                    'topic': topic_path
                }
                response1 = subscriber.create_subscription(request=api_request)
            # logging.info(response)
            logging.info('Subscription created [%s]', subscription_id)

            flash('Topic and subscription created successfully')
            return redirect('/')
        except google.api_core.exceptions.GoogleAPIError as err:
            logging.error(err)
            flash('Unable to create topic or error. Check application logs')
            return redirect(request.url)


# http://localhost:5000/list
@app.route('/list', methods=['GET'])
def fetch():
    """Index page to list topics or subscriptions."""
    logging.info('Showing index page to list topics or subscriptions')
    return render_template('list.html', data=[])


@app.route('/list', methods=['POST'])
def get():
    """Endpoint to list topics or subscriptions."""
    choice = request.form.get('choice_select')
    project_id = request.form.get('project')
    topic_id = request.form.get('topic')

    if choice == 'topics':
        logging.info('Listing topics in project [%s]', project_id)
        if project_id == '':
            logging.info('Project id is mandatory for listing topics')
            flash('Topic id cannot be empty when choice is topics')
            return redirect(request.url)
        else:
            topics = []
            publisher = google.cloud.pubsub_v1.PublisherClient()
            project_path = 'projects/{pid}'.format(pid=project_id)
            response = publisher.list_topics(request={'project': project_path})
            for topic in response:
                # logging.info(topic)
                topics.append(topic)

            return render_template('list.html', message='Showing topics', data=topics)

    if choice == 'subscriptions':
        logging.info('Listing subscriptions for topic [%s] in project [%s]', topic_id, project_id)
        if project_id == '' or topic_id == '':
            logging.info('Topic or subscription cannot be blank')
            flash('Topic or subscription cannot be empty when choice is subscriptions')
            return redirect(request.url)
        else:
            # todo - to be implemented
            return render_template('list.html', message='', data=[])


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5000')
    # Development only: run 'python app.py' and open http://localhost:5000
    app.run(debug=False, port=server_port, host='0.0.0.0')
```

### 1.3 form.html

Create an html file named - <code>form.html</code> in the <code>templates</code> folder responsible to take the user input (i.e. topic and subscription name) and the backend code available at this endpoint - <code>/</code> is responsible to create the topic and subscription in the google cloud platform.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Index</title>
    </head>
    <body>
        <h1>Topic & subscription</h1>
        <hr />
        <p>
            {% with messages = get_flashed_messages() %}
              {% if messages %}
                <ul class=flashes>
                {% for message in messages %}
                  <li>{{ message }}</li>
                {% endfor %}
                </ul>
              {% endif %}
            {% endwith %}
        </p>

        <h3>Enter details to create topic and subscription</h3>
        <form action="/" method="post">
            <label for="project">Enter project id...:</label>
            <input type="text" id="project" name="project" placeholder="project name">
            <br>
            <br>
            <label for="topic">Enter topic name...:</label>
            <input type="text" id="topic" name="topic" placeholder="topic name" />
            <br>
            <br>
            <label for="subscription">Enter subscription name...:</label>
            <input type="text" id="subscription" name="subscription" placeholder="subscription name" />
            <br>
            <br>
            <input type="submit" value="Submit" />
        </form>
    </body>
</html>
```

### 1.4 list.html

Create an html file named - <code>list.html</code> in the <code>templates</code> folder responsible to accept the user's choice and get the required results from the google cloud platform with the help of backend endpoint - <code>/list</code> attached to the form input.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Files</title>
    </head>
    <body>
        <h1>Fetch topics in a project or subscriptions for a topic</h1>
        <hr />
        <p>
            {% with messages = get_flashed_messages() %}
              {% if messages %}
                <ul class=flashes>
                {% for message in messages %}
                  <li>{{ message }}</li>
                {% endfor %}
                </ul>
              {% endif %}
            {% endwith %}
        </p>

        <form action="/list" method="post">
            <label for="choice_select">Select choice...</label>
            <select id="choice_select" name="choice_select">
                <option value="topics">topics</option>
                <option value="subscriptions">subscriptions</option>
            </select>
            <br>
            <br>
            <label for="project">Enter project id...:</label>
            <input type="text" id="project" name="project" placeholder="project name">
            <br>
            <br>
            <label for="topic">Enter topic name...:</label>
            <input type="text" id="topic" name="topic" placeholder="topic name" />
            <br>
            <br>
            <input type="submit" value="Submit" />
        </form>

        <h3>{{message}}</h3>
        <ul>
            {% for item in data %}
            <li>{{ item }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

## 2. Run the application

After successfully developing the application let us start the application by running the <code>main.py</code> file. Once the application is started successfully head over to the browser of your choice and enter the following endpoint - `http://localhost:5000` to play with the application.

"If you feel like something needs to add or changed feel free to connect with us with the slack community or drop us an email at - support@in28minutes.com"
