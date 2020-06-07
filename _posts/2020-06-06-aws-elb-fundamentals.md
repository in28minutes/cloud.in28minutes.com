---
layout:     post
title:      Elastic Load Balancers - ELB - AWS Certification
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

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target="_blank"}


## Elastic Load Balancer
![](/images/aws/ec2/1-simple-elb.png)
- Distribute traffic across EC2 instances in one or more AZs in a single region
- **Managed service** - AWS ensures that it is highly available
- Auto scales to handle huge loads
- Load Balancers can be **public or private**
- **Health checks** - route traffic to healthy instances

## Three Types of Elastic Load Balancers
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
- **Demo** : Create an Application Load Balancer 

## Load Balancers - Security Group Best Practice
||
|--|
| Load Balancer allow traffic from everywhere! |
|![](/images/aws/loadbalancer-inbound-sg-rules.png)     |
|EC2 Security Group **ONLY** allows traffic from Load Balancer Security Group|
|![](/images/aws/ec2-inbound-sg-rules.png)|
|(Best Practice) Restrict allowed traffic using Security Groups|

## Listeners
![](/images/aws/elb-listener.png)
- Each Load Balancer has **one or more listeners** listening for connection requests from the client
- Each listener has:
	- a protocol
	- a port
	- a set of rules to route requests to targets

## Multiple Listeners
![](/images/aws/elb-listeners-multiple.png)
- You can have multiple listeners listening for a different protocol or port
- In the above example:
	- HTTP requests on port 80 are routed to the EC2 instances target group
	- HTTPS requests on port 443 are routed to port 80
	- HTTP requests on port 8080 get a fixed response (customized HTML)

## Target Groups
![](/images/aws/ec2/4-elb-target-groups.png)
- How to group instances that ALB has to distribute the load between? 
	- Create a Target Group
- A target group can be:
	- A set of EC2 instances
	- A lambda function
	- Or a set of IP addresses

## Target Group Configuration - Sticky Session
> Enable sticky user sessions

![](/images/aws/ec2/2-elb-sticky-session.png)
- Send all requests from one user to the same instance
- Implemented using a cookie
- Supported by ALB and CLB

## Target Group Configuration - Deregistration delay 

> How long should ELB wait before de-registering a target?

- Load balancer stops routing new requests to a target when you unregister it
- What about requests that are **already in progress** with that target?
- This setting ensures that load balancer gives **in-flight requests** a chance to complete execution
- 0 to 3600 seconds (default 300 seconds)
- Also called Connection Draining

## Microservices architectures - Multiple Target Group(s)
![](/images/aws/ec2/5-elb-target-groups.png)
- Microservices architectures have 1000s of microservices
	- http://www.xyz.com/microservice-a 
	- http://www.xyz.com/microservice-b 
- Should we create multiple ALBs?
- **Nope**. One ALB can support multiple microservices! 
- Create separate target group for each microservices
- (Remember) Classic Load Balancer, **does NOT** support multiple target groups.
	

## Listener Rules
![](/images/aws/elb-listener-rules.png)
- How do I identify which request should be sent to which target group?
- Configure multiple listener rules for the same listener
- Rules are executed in the order they are configured. 
- Default Rule is executed last.

## Listener Rules - Possibilities
![](/images/aws/elb-listener-rules.png)
- Based on **path** - in28minutes.com/a to target group A and in28minutes.com/b to target group B
- Based on **Host** - a.in28minutes.com to target group A and b.in28minutes.com to target group B
- Based on **HTTP headers** (Authorization header) and methods (POST, GET, etc)
- Based on **Query Strings** (/microservice?target=a, /microservice?target=b)
- Based on **IP Address** - all requests from a range of IP address to target group A. Others to target group B

## Architecture Summary
![](/images/aws/elb_architecture.png)

https://docs.amazonaws.cn/en_us/elasticloadbalancing/latest/application/introduction.html
- Highly decoupled architecture
- Load balancer can have multiple listeners (protocol + port combinations).
- Each listener can have multiple rules each routing to a target group based on request content.
- A target can be part of multiple target groups. 

## Network Load Balancer
- Functions at the **Transport Layer** - Layer 4 (Protocols TCP, TLS and UDP)
- For **high performance** use cases (millions of requests per second)
- Can be assigned a **Static IP/Elastic IP**
- Can load balance between:
	- EC2 instances
	- Containerized applications (Amazon ECS)
	- Web applications (using IP addresses)
- Demo

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

## Review

##### Application Load Balancer
- Layer 7(HTTP/HTTPS) 
- Supports **advanced routing approaches** (path, host, http headers, query strings and origin IP addresses)
- Load balance between EC2 instances, containers, IP addresses and lambdas

##### Concepts
- Each Load Balancer has one or more **listeners** (different protocol or port) listening for connection requests from the client
- **Target group** is a group representing the targets (ex: EC2 instances)
- One ALB or NLB can support multiple microservices (multiple target groups)!


## Elastic Load Balancers - AWS Certification Exam Practice Questions

Coming Soon..