# Infrastructure setup

Infrastructure automation scripts, created by a developer, for the developers. Be patient, look around, and get yourself
comfortable.

## Pre-requisite

* Google Cloud SDK from [here](https://cloud.google.com/sdk/docs/install)
* Docker from [here](https://docs.docker.com/engine/install/)

## Files

* [service.dev.yml](service.dev.yaml) represents the service yaml file for the application
* [config.sh](config.sh) responsible for setting the required gcp environment variables
* [start.sh](start.sh) responsible for starting the cloudrun emulator
* [stop.sh](stop.sh) responsible for clearing the environment variables

## Recipes and Examples

### Pre-Requisites

```shell
gcloud beta auth configure-docker
gcloud components install minikube
gcloud components install skaffold
gcloud components install alpha
gcloud components install kubectl
gcloud components install beta
```

### Quick Start from Zero to Hero

Starting from scratch? Let's go!

```shell
# Open the terminal and navigate to 'infra' folder (say terminal1)
$ sh start.sh
```

### Tear Down

It's OK if you want to kill few servers. Here's how:

```shell
# Navigate back to the terminal1
$ press Control+C
$ sh stop.sh
```