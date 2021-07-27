---
layout:     post
title:      Deploy Spring Boot Application with Nginx Ubuntu on AWS Beanstalk
date:       2020-09-25 22:15:00
summary:    In this tutorial, we will explain how to deploy Spring Boot Application with Nginx Ubuntu on AWS Beanstalk.
categories:  AWS_CLOUD AWS_VPC
permalink:  /deploy-spring-boot-application-with-nginx-aws


# Deploy Spring Boot Application with Nginx Ubuntu on AWS


Greetings from [in28minutes.com](https://courses.in28minutes.com/).

- The Spring Framework is an application framework and inversion of control container for the Java platform. The framework&apos;s core features can be used by any Java application, but there are extensions for building web applications on top of the Java EE platform.

- Nginx, stylized as NGINX, nginx or NginX, is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. The software was created by Igor Sysoev and publicly released in 2004. Nginx is free and open-source software, released under the terms of the 2-clause BSD license.

- Amazon Web Services is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.


## Requirements

- Java Version 8
- Ubuntu server
- AWS Server

## Getting Started

Update your server with the following command:

```sh
apt-get update -y
apt-get upgrade -y
```

Install Java and check version

```sh
apt-get install openjdk-8-jdk -y
java -version
```

You should see the following output:

```sh
java version "1.8.0_221"
Java(TM) SE Runtime Environment (build 1.8.0_221-b11)
Java HotSpot(TM) 64-Bit Server VM (build 25.221-b11, mixed mode)

```

## Install Spring Boot CLI

Now install Spring Boot CLI and Other build tools

```sh
# curl -s https://get.sdkman.io | bash
# source "/root/.sdkman/bin/sdkman-init.sh"
# sdk install springboot
# spring version
# sdk install gradle 4.5.1

```
## Build a Jar File with Gradle


```sh
# spring init --build=gradle --dependencies=web --name=hello hello-world
Using service at https://start.spring.io
Project extracted to '/root/hello-world'
# spring init --list
# cd hello-world
# nano src/main/java/com/example/helloworld/HelloApplication.java
# ./gradlew build
# java -jar build/libs/hello-world-0.0.1-SNAPSHOT.jar
# gradle bootRun

```

## Create a Systemd Service File for Spring Boot

```sh
# nano /etc/systemd/system/helloworld.service
# systemctl daemon-reload
# systemctl start helloworld
# systemctl enable helloworld
# systemctl status helloworld


```

## Configure Nginx as a Reverse Proxy

```sh
# apt-get install nginx -y
# nano /etc/nginx/conf.d/helloworld.conf
# systemctl restart nginx

```

## Test Application

The Spring Boot application deployment is ready. 
- url :  http://example.com



Good luck and Happy learning! 

Feel free to share it with your friends/colleagues.
