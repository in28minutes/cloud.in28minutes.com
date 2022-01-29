In this tutorial, You'll learn how to create a simple Python flask application, create docker image and run the scripts to deploy into Google CloudRun.

![](/images/googlecloud/cloudrun_app.png)

## Requirements
* Python and Flask Installation
* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* [Google Cheat Sheet](https://cloud.google.com/sdk/docs/images/gcloud-cheat-sheet.pdf)

## Example Code
This tutorial is accompanied by a working code example [on Github]()

## Getting Started

## 1. Create Helloworld Python Application

* Create a folder called ``SamplePythonApplication`` on your desired drive. You will be storing all you files in this folder.
* Since it is a simple helloworld application, you can create using Notepad.
* Open Notepad application, copy and paste the below code snippet and save it as ``app.py``.

## app.py

```python
import os from datetime import datetime

from flask import Flask

app = Flask(__name__)


# http://localhost:8080/
@app.route('/', methods=['GET'])
def hello_world():
    """Return a friendly greeting."""
    return {'code': '200', 'message': 'Welcome to the in28minutes tutorials!'}


# http://localhost:8080/timestamp
@app.route('/timestamp', methods=['GET'])
def get_timestamp():
    """Return current timestamp."""
    now = datetime.now()
    timestamp = now.strftime('%d-%m-%y') + "-" + now.strftime("%H:%M:%S")
    return {'code': '200', 'time_stamp': timestamp}


# driver code
if __name__ == '__main__':
    # Development only: run "python app.py" and open http://localhost:8080
    # In production WSGI HTTP server, such as Gunicorn, will serve the app.
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')


```

## 2. Build the apps's container image 

### 2.1. Using Dockerfile

In order to build the application, we need to use a ``Dockerfile``. A Dockerfile is simply step-by-step instructions (text-based) that is used to create a container image.

Create a file name called ``Dockerfile`` in the same folder of ``SamplePyhtonApplication`` with the following contents. Please note that the file ``Dockerfile`` has no file extension.

```
# Python image to use
FROM python:3.10-slim

# Author of the image
MAINTAINER teacher@in28minutes.com

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

Using ``Dockerfile`` we can create a docker image for the single application, however with the help of ``Docker  Compose`` tool, we can create multi-container application.

If you have installed Docker Desktop in your respective operating system, you already have the Docker Compose!.

* Create a file named ``docker-compose.yml`` with the following contents. 
In most cases, it's best to use the latest supported ``version``

```
version: "3.7"

services:
  helloworld:
    build:
      context: .
      dockerfile: Dockerfile
    image: "pythonflask:latest"
    container_name: "pythonflask"
    ports:
      - "8080:8080"
```

So now, we have created app's container image, next step is to deploy into Google Cloud environment. Let's go

## 3. Configure Google SDK

For Google Cloud SDK Installation and Account setup, please refer to the below links:

1. Google Cloud SDK from [here](https://cloud.google.com/sdk/docs/install)

2. Configure Google Cloud SDK in Windows from [here](https://cloudaffaire.com/how-to-install-and-configure-google-cloud-sdk-or-gcloud-on-windows-os/)

3. Configure Google Cloud SDK in Windows from [here](https://cloud.google.com/docs/authentication/production#linux-or-macos)

4. Configure Docker with GCP from [here](https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper)

## 4. Deploying to `gcloud`

After successfully configuring Google Cloud SDK, now we will run the couple of scripts for deploying application to the cloud.

## Prerequisites

```shell
gcloud beta auth configure-docker
gcloud components install beta
```
### Execute the below Commands

1. `config.sh` : For configuring an environment variables
2. `build.sh` : For creating and pushing a docker image
3. `create_cloud_run.sh` : Deploy the created image on the cloud run instance
4. `start.sh`: Start the cloud run instance

```shell
# Open the terminal and navigate to 'infra' folder (say terminal1)

$ source config.sh
$ sh build.sh
$ sh create_cloud_run.sh
```

Or,

```shell
# Open the terminal and navigate to 'infra' folder (say terminal1)

$ source config.sh
$ sh start.sh
```
Application will be deployed on cloud run, and you can play with the application at these endpoints:

* `http://localhost:8080/`

### Output
```shell
Welcome to the in28minutes tutorials!
```
* `http://localhost:8080/timestamp`
### Output
```shell
22-01-2022-10:10:10
```

"If you feel like something needs to add or changed feel free to connect with us with the slack community or drop us an email at - support@in28minutes.com"