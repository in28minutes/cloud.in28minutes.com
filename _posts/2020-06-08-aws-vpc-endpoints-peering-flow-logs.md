---
layout:     post
title:      VPC Endpoints - Gateway vs Interface, VPC Peering and VPC Flow Logs - AWS Certification Cheat Sheet
date:       2020-09-12 12:31:19
summary:    Let's get a quick overview of VPC Endpoints (Gateway vs Interface), VPC Peering and VPC Flow Logs. 
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-vpc-endpoints-gateway-interface-peering-flow-logs
---

Let's get a quick overview of VPC Endpoints (Gateway vs Interface), VPC Peering and VPC Flow Logs.

## You will learn
- What are VPC Endpoints?
- What are the different types of VPC Endpoints?
- When do you use Gateway Endpoints vs Interface Endpoints?
- What is VPC Peering?
- How do you use VPC Flow Logs to debug problems?

## AWS Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## VPC Endpoint 

![](/images/aws/00-icons/vpcendpoint.png)

VPC Endpoint helps you to securely connect your VPC to another service.

There are two types
- Gateway endpoint
- Interface endpoint

A Gateway endpoint:
- Help you to securely connect to Amazon S3 and DynamoDB
- Endpoint serves as a target in your route table for traffic
- Provide access to endpoint (endpoint, identity and resource policies)

An Interface endpoint:
- Help you to securely connect to AWS services EXCEPT FOR Amazon S3 and DynamoDB
- Powered by PrivateLink (keeps network traffic within AWS network)
- Needs a elastic network interface (ENI) (entry point for traffic)

Important things to remember about VPC Endpoints:
- (Avoid DDoS & MTM attacks) Traffic does NOT go thru internet
- (Simple) Does NOT need Internet Gateway, VPN or NAT

## VPC Peering

![](/images/aws/vpc-peering.png)

VPC Peering helps you to connect VPCs belonging to same or different AWS accounts irrespective of the region of the VPCs.

This allows private communication between the connected VPCs.

Peering uses a request/accept protocol:
- Owner of requesting VPC sends a request 
- Owner of the peer VPC has one week to accept

Couple of important things to remember about VPC Peering:
- Peering is not transitive
- Peer VPCs cannot have overlapping address ranges

## VPC Flow Logs

![](/images/aws/00-icons/vpcflowlogs.png) 

VPC Flow Logs are used to Monitor network traffic.

Using VPC Flow Logs you can:
- Troubleshoot connectivity issues (NACL and/or security groups misconfiguration).
- Capture traffic going in and out of your VPC (network interfaces).

VPC Flow Logs can be created for 
- a VPC
- a subnet
- or a network interface (connecting to ELB, RDS, ElastiCache, Redshift etc)

You can Publish logs to Amazon CloudWatch Logs or Amazon S3.  Flow log records contain ACCEPT or REJECT - Is traffic is permitted by security groups or network ACLs?

## Troubleshoot using VPC Flow Logs 

![](/images/aws/00-icons/user.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/nacl.png)
![](/images/aws/00-icons/subnet.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/securitygroup.png)
![](/images/aws/00-icons/ec2.png)

How do you troubleshoot issues? Here is some simplified logic:
- Problem with response => Problem with NACL.
- Problem with request could be problems with NACL or SG.

Inbound traffic rules are checked in this order: NACL IN, SG IN, NACL OUT (SG OUT NOT checked):
- If inbound request is rejected, SG or NACL could be mis-configured
- If outbound response is rejected, NACL is mis-configured

Outbound traffic rules are checked in this order: SG OUT, NACL OUT, NACL IN (SG IN NOT checked):
- If outbound request is rejected, SG or NACL could be mis-configured
- If inbound response is rejected, NACL is mis-configured
