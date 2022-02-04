---
layout:     post
title:      Google cloud run emulator - For Architects - Google cloud certification
date:       2022-02-30 21:06:00
summary:    Let's understand the google cloud run emulator with the help of a sample application
categories:  GOOGLE_CLOUD CLOUDRUN
permalink:  /google-cloud-certification-cloudrun-emulator
---

In this tutorial, You'll learn how to create a simple Python Flask application with an in-memory database (popularly
known as Sqlite), create a docker image, and run the scripts to deploy into the Google CloudRun emulator.

![](/images/googlecloud/cloudrun_app.png)

# Requirements

- Python, Flask, Sqlite Installation
- Google cloud account
- [Google cloud sdk](https://cloud.google.com/sdk/docs/install)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Google Cheat Sheet](https://cloud.google.com/sdk/docs/images/gcloud-cheat-sheet.pdf)

# Example Code

This tutorial is accompanied by a working code example [on Github]()

# Getting Started

## 1. Creating Python application

- Create a folder called `PythonAppOnCREmulator` on your desired drive. You will be storing all the files in this folder
- I would recommend using
  the [Community version PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=windows) for the development
  of this application

### 1.1 requirements.txt

Let us start creating the application by installing the required dependencies. Run the following command - <code>pip install -r requirements.txt</code> in your terminal shell to download the required dependencies

```plain
Faker==10.0.0
Flask==1.1.4
```

### 1.2 db.py

Create a file responsible to interact with the in-memory database and perform the DDL (data definition language) operation. You're free to change the properties as per your learning

```python
import sqlite3
from sqlite3 import Error

DATABASE_name = 'todo.db'


def get_conn():
    try:
        conn = sqlite3.connect(DATABASE_name)
        return conn
    except Error as e:
        print(e)


def create_table():
    tables = [
        """
        CREATE TABLE todos(id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT NOT NULL, status TEXT NOT NULL)
        """
    ]
    db = get_conn()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


def get_tables():
    cursor = get_conn().cursor()
    sql = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(sql)
    names = [row[0] for row in cursor.fetchall()]
    return names


def is_table(name):
    """Determine if a table exists"""
    return name in get_tables()
```

### 1.3 ctrl.py

Create a file responsible to handle the interactions from the client and fetch the data from the in-memory database. The implementation of <code>update</code> and <code>delete</code> methods have been left intentionally for our readers to experiment it.

```python
from db import get_conn


def get_total():
    return len(get_all())


def get_all():
    cursor = get_conn().cursor()
    sql = 'SELECT id, item, status FROM todos'
    cursor.execute(sql)
    return cursor.fetchall()


def get_by_id(key):
    cursor = get_conn().cursor()
    sql = 'SELECT id, item, status FROM todos WHERE id=?'
    cursor.execute(sql, [key])
    return cursor.fetchone()


def save(item, status):
    db = get_conn()
    cursor = db.cursor()
    sql = 'INSERT into todos (item, status) VALUES (?, ?)'
    cursor.execute(sql, [item, status])
    db.commit()
    return True

# update and delete - To be implemented...
```

### 1.4 helper.py

This file acts utility helper and we are primarily using it for bootstrapping operations. In this application, we are using the <code>bootstrap()</code> responsible to create the table (if it does not exist) and inserting some mock data into the <code>todos</code> table.

```python
from faker import Faker

from ctrl import get_total, save
from db import is_table, create_table

faker = Faker()


def bootstrap():
    if not (is_table('todos')):
        create_table()

    if get_total() == 0:
        for x in range(1, 6):
            save(faker.word(), faker.name())
```

### 1.5 app.py

This file is the main file of the application and will be called during the application startup.

```python
import os

from flask import Flask

import ctrl
from helper import bootstrap

app = Flask(__name__)


# http://localhost:8080/
@app.route('/', methods=['GET'])
def hello():
    return {'code': 200, 'message': 'hello world!'}


# http://localhost:8080/item/all
@app.route('/item/all', methods=['GET'])
def get_all():
    eles = []
    for todo in ctrl.get_all():
        eles.append({'id': todo[0], 'item': todo[1], 'status': todo[2]})

    return {'code': 200, 'todos': eles, 'count': len(eles)}


# http://localhost:8000/item/1
@app.route('/item/<key>', methods=['GET'])
def get_by_id(key):
    ele = ctrl.get_by_id(key)
    if ele is None:
        return {'code': 404, 'message': 'RESOURCE_NOT_FOUND'}

    return {'code': 200, 'todo': {'id': ele[0], 'item': ele[1], 'status': ele[2]}}


# update and delete - To be implemented...

# main code
if __name__ == '__main__':
    bootstrap()
    server_port = os.environ.get('PORT_NUMBER', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
```

## 2. Build the apps' container image

### 2.1. Using Dockerfile

To build the application, we need to use a `Dockerfile`. A Dockerfile is simply step-by-step instructions (text-based) that is used to create a container image. Create a file name called `Dockerfile` in the same folder of `PythonAppOnCREmulator` with the following contents. Please note that the file `Dockerfile` has no file extension.

```plain
# Python image to use
FROM python:3.10-slim

# Author of the image
MAINTAINER geeks

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file used for dependencies
COPY requirements.txt .

# Install the needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the working directory contents into the container at /app
COPY . .

# Run app.py when the container launches
ENTRYPOINT ["python3", "app.py"]
```

### 2.2. Using Docker Compose

Using `Dockerfile` we can create a docker image for a single application, however, with the help of the `Docker Compose` tool, we can create a multi-container application.

If you have installed Docker Desktop in your respective operating system, you already have the Docker Compose!.

- Create a file named `docker-compose.yml` with the following contents. In most cases, it's best to use the latest supported `version`

```plain
version: "3.7"

services:
  helloworld:
    build:
      context: .
      dockerfile: Dockerfile
    image: "py-flask-sqlite:latest"
    container_name: "py-flask-sqlite"
    ports:
      - "8080:8080"
```

### 2.3 Running app on localhost

Once the <code>docker-compose.yml</code> is ready, open the terminal and hit the following commands to either get the application up and running on docker or stop it.

```plain
-- to create the image and start container --
docker-compose up -d --build

-- to check if the container is started
docker ps -a

-- to stop and remove the container --
docker-compose down
```

So once the application is up and running on Docker on port number 8080 take a look at it and playground to understand the basis of the application. Now let's go ahead with the deployment on the google cloud emulator.

## 3. Configure Google SDK

For Google Cloud SDK Installation and Account setup, please refer to the below links:

1. Google Cloud SDK from [here](https://cloud.google.com/sdk/docs/install)

2. Configure Google Cloud SDK in Windows
   from [here](https://cloudaffaire.com/how-to-install-and-configure-google-cloud-sdk-or-gcloud-on-windows-os/)

3. Configure Google Cloud SDK in Windows
   from [here](https://cloud.google.com/docs/authentication/production#linux-or-macos)

4. Configure Docker with GCP
   from [here](https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper)

## 4. Deploying to `gcloud`

After successfully configuring Google Cloud SDK, now we will run a couple of scripts for deploying applications to the cloud run emulator.

### Prerequisites

```shell
gcloud beta auth configure-docker
gcloud components install minikube
gcloud components install skaffold
gcloud components install alpha
gcloud components install kubectl
gcloud components install beta
```

### Execute the below Commands

For the cloud run emulator to work properly we will first create a folder named infra in the current working directory and add the below files to it.

- `service.dev.yml`: Represents a file that will be used for the deployment on the cloud run emulator. You're free to change the properties as your wish
- `config.sh` : For configuring an environment variables
- `start.sh`: Start the cloud run emulator and host application on it
- `stop.sh`: Cleaning up the environment

```shell
# Open the terminal and navigate to 'infra' folder (say terminal1)
$ sh start.sh
```

To stop the application trigger the below command from the terminal.

```shell
$ sh stop.sh
```

The application will be deployed on cloud run, and you can play with the application at these endpoints: `http://localhost:8080/`

"If you feel like something needs to add or changed feel free to connect with us with the slack community or drop us an
email at - support@in28minutes.com"
