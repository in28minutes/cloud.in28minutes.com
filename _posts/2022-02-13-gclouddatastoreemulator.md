---
layout:     post
title:      Google cloud datastore emulator - For Architects - Google cloud certification
date:       2022-02-13 21:06:00
summary:    Let's understand the google cloud datastore emulator with the help of a sample application
categories:  GOOGLE_CLOUD DATASTORE_EMULATOR
permalink:  /google-cloud-certification-datastore-emulator
---

In this tutorial, you'll learn how to create a simple python flask application and integrate it with a cloud datastore emulator.

![](/images/googlecloud/cloudrun_datastore.png)

# Requirements

- Python, Flask
- Google cloud account
- [Google cloud sdk](https://cloud.google.com/sdk/docs/install)
- [Google Cheat Sheet](https://cloud.google.com/sdk/docs/images/gcloud-cheat-sheet.pdf)

# Example Code

This tutorial is accompanied by a working code example [on in28minutes]()

# Getting Started

## 1. Create Python application

- Create a folder named `PythonAppWithDatastoreEmu` on your desired drive. You will be storing all the files in this folder
- I would recommend using the [Community version PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=windows) for the development of the application

### 1.1 requirements.txt

Let us start creating the application by installing the required dependencies. Run the following command - <code>pip install -r requirements.txt</code> in your terminal shell to download the required dependencies

```plain
Flask
google-cloud-datastore
```

### 1.2 main.py

Create a file responsible to interact with the cloud datastore and perform the required operations. You're free to change the application as per your wish

```python
import datetime
import os

from flask import Flask, render_template
from google.cloud import datastore

os.environ['DATASTORE_EMULATOR_HOST'] = 'localhost:8484'
os.environ['DATASTORE_PROJECT_ID'] = 'testproject'

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

### 1.3 index.html

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

## 2. Start the emulator

To work with this application we need to start the datastore emulator. Let us take at the below steps on how to start the emulator and for that I have create a separate folder named - <code>infra</code> in the project. If required you can also take a look at the README.md file in the attached source code.

### 2.1 Setting up the configuration

Set up the service endpoint in the <code>config.sh</code> file to start the localhost emulator.

```shell
#!/bin/bash

export DATASTORE_EMULATOR_HOST=YOUR_SERVICE_ENDPOINT
```

### 2.2 Starting the emulator

To start the emulator open the terminal, navigate to the <code>infra</code> directory and run the <code>start.sh</code> file

```shell
#!/bin/bash

set -e

source ./config.sh

echo "Starting datastore emulator on localhost environment"
gcloud beta emulators datastore start --host-port="$DATASTORE_EMULATOR_HOST"
```

### 2.2 Stopping the emulator

To stop the emulator use the terminal (opened in step2.2), navigate to the <code>infra</code> directory and run the <code>stop.sh</code> file. Make note that before running the script trigger the <code>ctrl+c</code> command to terminate the running emulator instance 

```shell
#!/bin/bash

# TO STOP THE EMULATOR PRESS Control+C
echo "Cleaning up datastore emulator environment variables from localhost environment"
unset DATASTORE_EMULATOR_HOST
```

## 3. Run the application

After successfully developing the application let us start the application by running the <code>main.py</code> file. Once the application is started successfully head over to the browser of your choice and enter the following endpoint - `http://localhost:8080` to display the application output.

"If you feel like something needs to add or changed feel free to connect with us with the slack community or drop us an email at - support@in28minutes.com"
