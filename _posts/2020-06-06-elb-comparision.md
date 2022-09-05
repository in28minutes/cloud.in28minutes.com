---
layout:     post
title:      Elastic Load Balancers - Application Load Balancer vs Network Load Balancer vs Classic Load Balancer (ALB vs NLB vs CLB) - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Elastic Load Balancers from an AWS certification perspective. We will look at important certification questions regarding Elastic Load Balancers - Application Load Balancer vs Network Load Balancer vs Classic Load Balancer (ALB vs NLB vs CLB). 
categories:  AWS_CLOUD ELB
permalink:  /aws-certification-elb-alb-nlb-clb
---

Let's get a quick overview of Elastic Load Balancers from an AWS certification perspective. We will look at important certification questions regarding Elastic Load Balancers - Application Load Balancer vs Network Load Balancer vs Classic Load Balancer (ALB vs NLB vs CLB).

## You will learn

- What are the different Elastic Load Balancers offered by AWS?
- How do they compare - Application Load Balancer vs Network Load Balancer vs Classic Load Balancer (ALB vs NLB vs CLB)?
- How do you choose - Application Load Balancer vs Network Load Balancer vs Classic Load Balancer (ALB vs NLB vs CLB)?



## ALB vs NLB vs CLB - Overview

There are three important types of Load Balancers offered by AWS:
- Application Load Balancer (ALB)
- Network Load Balancer (NLB)
- Classic Load Balancer (CLB)

Classic Load Balancer are the older versions of Load Balancers. Application Load Balancer (ALB) and the Network Load Balancer (NLB) are the newer versions.


### ALB vs NLB vs CLB - Comparison

Here's a table comparing the features of different load balancers. You can find details about these features below the table.

| Feature |  Application Load Balancer | Network Load Balancer | Classic Load Balancer |
|--|--|--|--|
| Version  | New v2 | New v2 | Old v1|
| Use cases  | Web apps, microservices & containers | Extreme performance - millions of requests with less latency (100ms) | Avoid if possible. Not recommended by AWS. |
| Protocols Supported  | HTTP, HTTPS (Layer 7) | TCP, UDP, TLS (Layer 4) | TCP, SSL/TLS, HTTP, HTTPS(Layer 4 & 7) |
| Connection draining  |  &nbsp;&nbsp;&nbsp;✓ |  |  &nbsp;&nbsp;&nbsp;&nbsp;✓ |
| Dynamic Host Port Mapping  |  &nbsp;&nbsp;&nbsp;✓ |  &nbsp;&nbsp;&nbsp;&nbsp;✓ | &nbsp; |
| Cross-zone load balancing |  ✓(Always Enabled) |  ✓(Default Disabled) |  ✓(Default Disabled) |
| Sticky sessions |  ✓ |  |  ✓ |
| Server Name Indication (SNI) |  ✓ |  ✓ |  |
| Static IP |  |  ✓ |  |
| Elastic IP address  |  |  ✓ |  |
| Preserve Source IP address |  |  ✓ |  |
| WebSockets  |  ✓ |  ✓ | &nbsp; |
| IP addresses as targets |  ✓ |  ✓ (TCP, TLS) |  |
| Source IP address range (CIDR) based routing |  ✓ |  |  |
| Path(Route) Based Routing |  ✓ |  |  |
| Host-Based Routing   |  ✓ |  |  |
| Fixed response |   ✓ |  |  |
| Lambda functions as targets   |  ✓ |  |  |
| HTTP header-based routing   |  ✓ |  |  |
| HTTP method-based routing   |  ✓ |  |  |
| Query string parameter-based routing |  ✓ |  | &nbsp; |

### Elastic Load Balancer Terminology

Here is some of the important terminology referred to in the above table:
- **Connection draining** - Before an instance is terminated, requests in execution are given time to complete (deregistration_delay.timeout_seconds)
- **Dynamic Host Port Mapping** - Useful with containers. Two instances of the same task can be running on the same ECS container instance
- **Cross-zone load balancing** - Distribute load between available instances in multiple AZs in One Region
- **Sticky sessions** - Send requests from same user to same instance (cookies with configurable expiration  - Stickiness duration default - 1 day)
- **Preserve Source IP address**  - Allows instances to know where the request is coming from
- **WebSockets** - Allows full-duplex communication over a single TCP connection
- **Source IP range (CIDR) based routing** - Redirect to different targets based on the Source CIDR block
- **Path(Route) Based Routing** - Send traffic to different targets based on the path of the request
- **Query string parameter-based routing** - /user?target=target1 vs /user?target=target2
- **Server Name Indication (SNI)** - Support multiple websites with different SSL certificates with one Load Balancer