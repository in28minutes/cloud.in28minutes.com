# Python flask application

## Pre-requisite
* Docker from [here](https://docs.docker.com/engine/install/)

## Files

* [app.py](app.py) is entry point of the python application
* [requirements.txt](requirements.txt) file specify what python packages are required to run the project you're looking
  at
* [Dockerfile](Dockerfile) file allows you to build the image from Docker
* [docker-compose.yml](docker-compose.yml) file for building Docker image and deploying the Docker container
* [.dockerignore](.dockerignore) file mentions a list of files and/or directories you want to ignore while building the
  Docker image

## Recipes and Examples

### To create image and start the container in detached mode

Starting from scratch? Let's go!

```shell
docker-compose up -d
```

### To stop and remove the container

It's OK if you want to kill few servers. Here's how:

```shell
docker-compose down
```

## Localhost Debugging

Application will be started on port `8080` and you can play with the application at these endpoints

- Return a friendly greeting - `http://localhost:8080/`
- Return current timestamp - `http://localhost:8080/timestamp`
