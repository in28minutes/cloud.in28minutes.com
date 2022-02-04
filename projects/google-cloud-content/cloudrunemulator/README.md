# Python flask application

## Pre-requisite

* Docker from [here](https://docs.docker.com/engine/install/)

## Files

* [app.py](app.py) is the entry point of the python application
* [ctrl.py](ctrl.py) is responsible handle the interactions between the incoming request and sql
* [db.py](db.py) is responsible to make a connection with sql table and create a table programmatically
* [helper.py](helper.py) is responsible to handle the bootstrap function which will be called during application startup
* [requirements.txt](requirements.txt) file specify what python packages are required to run the project
* [Dockerfile](Dockerfile) file allows you to build the image from Docker
* [docker-compose.yml](docker-compose.yml) file for building Docker image and deploying the Docker container
* [.dockerignore](.dockerignore) file mentions a list of files and/or directories you want to ignore while building the
  Docker image
* [docker-commands.txt](docker-commands.txt) lists the basic commands for docker-compose
* [todo.db](todo.db) is automation by the sqlite database on application startup. same will be created in the docker
  container if hosted

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
