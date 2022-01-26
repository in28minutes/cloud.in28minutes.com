# Infrastructure setup

Infrastructure automation scripts, created by a developer, for the developers. Be patient, look around, and get yourself
comfortable.

## Pre-requisite

* Google Cloud SDK from [here](https://cloud.google.com/sdk/docs/install)
* Docker from [here](https://docs.docker.com/engine/install/)

## Files

* [config.sh](config.sh) responsible for setting the required gcp environment variables
* [build.sh](build.sh) responsible to create the Docker image
* [create_cloud_run.sh](create_cloud_run.sh) responsible to deploy the created image on the cloud run instance
* [start.sh](start.sh) for the impatient ;)

## Recipes and Examples

### Pre-Requisites

```shell
gcloud beta auth configure-docker
gcloud components install beta
```

### Quick Start from Zero to Hero

Starting from scratch? Let's go!

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

## Localhost Debugging

Application will be deployed on cloud run, and you can play with the application at these endpoints

- Return a friendly greeting - `http://CLOUDRUN_INSTANCE_ENDPOINT/`
- Return current timestamp - `http://CLOUDRUN_INSTANCE_ENDPOINT/timestamp`