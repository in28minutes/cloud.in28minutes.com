---
layout:     post
title:      Google cloud datastore - For Architects - Google cloud certification
date:       2022-02-09 21:06:00
summary:    Let's understand the google cloud datastore with the help of a sample application
categories:  GOOGLE_CLOUD DATASTORE
permalink:  /google-cloud-certification-datastore
---

In this tutorial, you'll learn how to create a simple python flask application and integrate it with a cloud datastore.

![](/images/googlecloud/cloudrun_datastore.png)

# Requirements

- Python, Flask
- Google cloud account
- [Google cloud sdk](https://cloud.google.com/sdk/docs/install)
- [Google Cheat Sheet](https://cloud.google.com/sdk/docs/images/gcloud-cheat-sheet.pdf)

# Example Code

This tutorial is accompanied by a working code example [on Github](https://github.com/in28minutes/cloud.in28minutes.com/tree/master/projects/google-cloud-content/datastore)

# Getting Started

## 1. Create Python application

- Create a folder named `PythonAppWithDatastore` on your desired drive. You will be storing all the files in this folder
- I would recommend using the [Community version PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=windows) for the development of the application

## 1.1 requirements.txt

Let us start creating the application by installing the required dependencies. Run the following command - <code>pip install -r requirements.txt</code> in your terminal shell to download the required dependencies

```plain
Flask
google-cloud-datastore
```

## 1.2 main.py

Create a file responsible to interact with the cloud datastore and perform the required operations. You're free to change the application as per your wish

```python
import datetime
import os

from flask import Flask, render_template
from google.cloud import datastore

app = Flask(__name__)

client = datastore.Client()


def store_time(now):
    # add object to db
    entity = datastore.Entity(key=client.key('visit'))
    entity.update({
        'timestamp': now
    })

    client.put(entity)


def fetch_times(limit):
    # query from db
    query = client.query(kind='visit')

    return query.fetch(limit=limit)


# http://localhost:8080/
@app.route('/', methods=['GET'])
def index():
    timestamp = datetime.datetime.now(tz=datetime.timezone.utc)

    store_time(now=timestamp)

    times = fetch_times(limit=10)

    return render_template('index.html', times=times)


if __name__ == '__main__':
    server_port = os.environ.get('PORT_NUMBER', '8080')

    app.run(debug=False, port=server_port, host='0.0.0.0')

```

## 1.3 index.html

Create a html file in the <code>templates</code> responsible to show the data from the backend application.

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Visit</title>
    </head>
    <body>
        <h2>Last 10 visits</h2>
        {% for time in times %}
        <p>{{ time['timestamp'] }}</p>
        {% endfor %}
    </body>
</html>
```

## 2. Run the application

After successfully developing the application let us start the application by running the <code>main.py</code> file. Once the application is started successfully head over to the browser of your choice and enter the following endpoint - `http://localhost:8080` to display the application output.

"If you feel like something needs to add or changed feel free to connect with us with the slack community or drop us an email at - support@in28minutes.com"
