---
layout:     post
title:      Elastic Load Balancer (ELB) vs Network Load Balancer (NLB) - A Difference - AWS Certification
date:       2020-11-16 15:00:00
summary:    Let's compare the difference between Elastic Load Balancer (ELB) vs Network Load Balancer (NLB)
categories:  AWS_CLOUD
permalink:  /aws-certification-elastic-load-balancer-vs-network-load-balancer
---
# Understanding the differences between Elastic Load Balancer and Network Load Balancer

In this tutorial, we will understand a basic comparison between *Elastic Load Balancer* and *Network Load Balancer*.

| Attribute | Elastic load balancer (ELB) | Network load balancer (NLB) |
|--|--|--|
| **Protocols** | Supports HTTP and HTTPS protocols | Supports TCP, UDP, and TLS |
| **Type** | Supports both internet-facing and internal | Supports both internet-facing and internal |
| **Supports health check** | YES | YES |
| **Cloudwatch logging and metrics** | YES | YES |
| **Connection draining (or deregistration delay)** | YES | YES |
| **Load balancing to multiple ports on same instances** | YES | YES |
| **Configurable idle connection timeout** | YES | YES |
| **Cross zone load balancing** | YES | YES |
| **Stickiness (or Sticky sessions)** | YES | YES |
| **Static IP address allocation (or the Elastic IP address)** | NO | YES |
| **Resource-based IAM permissions** | YES | YES |
| **Tag-based IAM permissions** | YES | YES |
| **CIDR based routing** | YES | NO |
| **Path-based routing** | YES | NO |
| **Host-based routing** | YES | NO |
| **HTTP header-based routing** | YES | NO |
| **Query string parameter-based routing** | YES | NO |
| **Fixed response** | YES | NO |
| **Lambda functions as targets** | YES | NO |
| **User authentication** | YES | NO |
| **SSL offloading** | YES | YES |
