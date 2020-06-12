---
layout:     post
title:      Elastic Load Balancers - ELB Fundamentals - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Elastic Load Balancers from an AWS certification perspective. We will look at important certification questions regarding Elastic Load Balancers. 
categories:  AWS_CLOUD ELB
permalink:  /aws-certification-elastic-load-balancers-elb
---

Let's get a quick overview of Elastic Load Balancers from an AWS certification perspective. We will look at important certification questions regarding Elastic Load Balancers.

## You will learn
- What is an Elastic Load Balancers?
- What are the different types of Elastic Load Balancers?
- Classic vs Application vs Network Load Balancers
- What is a Target Group?
- What is a Listener?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Elastic Load Balancer
Elastic Load Balancer are used to distribute traffic across EC2 instances in one or more AZs in a single region.
![](/images/aws/ec2/1-simple-elb.png)

Few important things to note:
- Elastic Load Balancer is a **Managed service** - AWS ensures that it is highly available.
- Auto scales to handle huge loads
- Load Balancers can be **public or private**
- **Health checks** - route traffic to healthy instances

## Three Types of Elastic Load Balancers

Three Types of Elastic Load Balancers include:
- **Classic** Load Balancer ( Layer 4 and Layer 7)
	- Old generation supporting Layer 4(TCP/TLS) and Layer 7(HTTP/HTTPS) protocols 
	- Not Recommended by AWS
- **Application** Load Balancer (Layer 7)
	- New generation supporting HTTP/HTTPS and advanced routing approaches
- **Network** Load Balancer (Layer 4)
	- New generation supporting TCP/TLS and UDP
	- Very high performance usecases

## Classic Load Balancer
- **Older** version of ELB
- **Not recommended anymore**
- Supports TCP, SSL/TLS and HTTP(S) (Layer 4 and 7)
- **Demo**: Create a Classic Load Balancer

## Application Load Balancer
![](/images/aws/ec2/1-simple-elb.png)
- **Most popular** and frequently used ELB in AWS
- Supports WebSockets and HTTP/HTTPS (Layer 7)
- Supports all important load balancer features
- Scales **automatically** based on demand (Auto Scaling)
- Can load balance between:
	- EC2 instances (AWS)
	- Containerized applications (Amazon ECS)
	- Web applications (using IP addresses)
	- Lambdas (serverless)

## Load Balancers - Security Group Best Practice
Best Practice is to Restrict allowed traffic using Security Groups.

Load Balancer allow traffic from everywhere!
![](/images/aws/loadbalancer-inbound-sg-rules.png) 

EC2 Security Group **ONLY** allows traffic from Load Balancer Security Group
![](/images/aws/ec2-inbound-sg-rules.png)


## Listeners
Each Load Balancer has **one or more listeners** listening for connection requests from the client

Each listener has:
- a protocol
- a port
- a set of rules to route requests to targets
![](/images/aws/elb-listener.png)


## Multiple Listeners
You can have multiple listeners listening for a different protocol or port

![](/images/aws/elb-listeners-multiple.png)
In the above example:
- HTTP requests on port 80 are routed to the EC2 instances target group
- HTTPS requests on port 443 are routed to port 80
- HTTP requests on port 8080 get a fixed response (customized HTML)

## Target Groups
How to group instances that ALB has to distribute the load between? 
- Create a Target Group

A target group can be:
- A set of EC2 instances
- A lambda function
- Or a set of IP addresses

![](/images/aws/ec2/4-elb-target-groups.png)

## Target Group Configuration - Sticky Session
Enabling sticky user sessions sends all requests from one user to the same instance. 

Important things to note:
- Implemented using a cookie
- Supported by ALB and CLB

![](/images/aws/ec2/2-elb-sticky-session.png)

## Target Group Configuration - Deregistration delay 

> How long should ELB wait before de-registering a target?

Load balancer stops routing new requests to a target when you unregister it. What about requests that are **already in progress** with that target?

Deregistration delay ensures that load balancer gives **in-flight requests** a chance to complete execution. This is also called Connection Draining. Can vary from 0 to 3600 seconds (default 300 seconds).

## Microservices architectures - Multiple Target Group(s)
Microservices architectures have 1000s of microservices
- http://www.xyz.com/microservice-a 
- http://www.xyz.com/microservice-b 

Should we create multiple ALBs?
- **Nope**. One ALB can support multiple microservices! 
- Create separate target group for each microservices

Classic Load Balancer, **does NOT** support multiple target groups.
	
![](/images/aws/ec2/5-elb-target-groups.png)

## Application Load Balancer - Health Check Settings
**Goal** is to Route traffic to healthy instances only! 
- Periodic requests are sent to targets to test their status
- Important Settings:
	- **HealthCheckProtocol**: Which protocol?
	- **HealthCheckPort**: Which port?
	- **HealthCheckPath**: Destination path (default - /)
	- **HealthCheckTimeoutSeconds** - Maximum wait time
	- **HealthCheckIntervalSeconds** - How often should a health check be performed?
	- **HealthyThresholdCount** - How many health check successes before marking an instance as healthy?
	- **UnhealthyThresholdCount** - How many health check failures before marking an instance as unhealthy?

## Listener Rules
How do I identify which request should be sent to which target group?
- Configure multiple listener rules for the same listener

![](/images/aws/elb-listener-rules.png)

Important things to note:
- Rules are executed in the order they are configured. 
- Default Rule is executed last.

## Listener Rules - Possibilities

You can configure Listener Rules based on:
- Based on **path** - in28minutes.com/a to target group A and in28minutes.com/b to target group B
- Based on **Host** - a.in28minutes.com to target group A and b.in28minutes.com to target group B
- Based on **HTTP headers** (Authorization header) and methods (POST, GET, etc)
- Based on **Query Strings** (/microservice?target=a, /microservice?target=b)
- Based on **IP Address** - all requests from a range of IP address to target group A. Others to target group B

![](/images/aws/elb-listener-rules.png)


## Architecture Summary
Highly decoupled architecture
- Load balancer can have multiple listeners (protocol + port combinations).
- Each listener can have multiple rules each routing to a target group based on request content.
- A target can be part of multiple target groups. 

![](/images/aws/elb_architecture.png)

https://docs.amazonaws.cn/en_us/elasticloadbalancing/latest/application/introduction.html

## Network Load Balancer
Network Load Balancer functions at the **Transport Layer** - Layer 4 (Protocols TCP, TLS and UDP). It is recommended for **high performance** use cases (millions of requests per second).

Here are the important things to note:
- Can be assigned a **Static IP/Elastic IP**
- Can load balance between:
	- EC2 instances
	- Containerized applications (Amazon ECS)
	- Web applications (using IP addresses)

## AWS Certification Review for Elastic Load Balancer

##### Elastic Load Balancer
- Distribute traffic across EC2 instances in one or more AZs in a single region
- **Managed Service** - highly available, Auto scales, public or private

##### Classic Load Balancer 
- Layer 4(TCP/TLS) and Layer 7(HTTP/HTTPS)
- **Old**. Not Recommended by AWS

##### Network Load Balancer
- Layer 4(TCP/TLS and UDP)
- Very **high performance usecases**
- Can be assigned a Static IP/Elastic IP

##### Application Load Balancer
- Layer 7(HTTP/HTTPS) 
- Supports **advanced routing approaches** (path, host, http headers, query strings and origin IP addresses)
- Load balance between EC2 instances, containers, IP addresses and lambdas

##### Concepts
- Each Load Balancer has one or more **listeners** (different protocol or port) listening for connection requests from the client
- **Target group** is a group representing the targets (ex: EC2 instances)
- One ALB or NLB can support multiple microservices (multiple target groups)!

## Important Load Balancer Certification and Interview Questions - Quick Review
 
| Scenario |Solution  | 
|--|--|
|You want to maintain sticky sessions|	Enable stickiness on ELB(cookie name: AWSELB)|
|You want to distribute load only to healthy instances| Configure health check. Health check can be a ping, connection or a web page request. You can configure interval, max wait time, threshold for number of failures. An instance can be InService/OutOfService. |
|Distribute load among two AZs in same region| Enable Cross Zone Load Balancing|
|How to ensure that in-flight requests to unhealthy instances are given an opportunity to complete execution?| Enable connection draining (1 to 3600 seconds. Default timeout - 300 seconds)|
|Give warm up time to EC2 instances before they start receiving load from ELB|Configure Health Check Grace Period |
|Protect ELB from web attacks - SQL injection or cross-site scripting| Integrate with AWS WAF (Web Application Firewall)|
|Protect web applications from DDoS attacks| Application Load Balancer (ALB) protects you from common DDoS attacks, like SYN floods or UDP reflection attacks.|

## Secure Communication - HTTPS
Using HTTPS secures the communication on the internet. To use HTTPS, install SSL/TLS certificates on the server
- In AWS, SSL certificates can be managed using AWS Certificate Manager

When using Elastic Load Balancer there are two Communication hops
- Client to ELB:
	- Over internet. 
	- HTTPS recommended
	- ELB requires X.509 certificates (SSL/TLS server certificates)
- ELB to EC2 instance:
	- Through AWS internal network. 
	- HTTP is ok. HTTPS is preferred. 

![](/images/aws/00-icons/client.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/elb.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/ec2instance.png)

## Elastic Load Balancer - SSL/TLS Termination
![](/images/aws/00-icons/client.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/elb.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/ec2instance.png)
- Application/Classic Load Balancer - SSL Termination
	- Client to ELB: HTTPS
	- ELB to EC2 instance: HTTP
- Network Load Balancer - TLS Termination
	- Client to ELB: TLS
	- ELB to EC2 instance: TCP

## Server Name Indication
ALB can provide load balancing for multiple target groups. Each of these targets can be separate websites with different SSL/TLS certificates. Each Listener can be associated with multiple SSL certificates(one for each website) to enable this.

![](/images/aws/elb-sni.png) 

Few important details:
- Server Name Indication is automatically enabled when multiple SSL certificates are associated with a listener
- Server Name Indication is an extension to TLS protocol 
	- Client indicates the host name being contacted at the start of interaction

## Elastic Load Balancer - Logs and Headers
You can enable access logs on ELB to capture:
- Time request was received
- Client's IP address
- Latencies
- Request Paths, and 
- Server Response

Network Load Balancer allows the EC2 instance to see the client details. 

HOWEVER Application Load Balancer does NOT
- Client details are in request headers:
	- X-Forwarded-For: Client IP address
	- X-Forwarded-Proto: Originating Protocol - HTTP/HTTPS
	- X-Forwarded-Port: Originating Port
