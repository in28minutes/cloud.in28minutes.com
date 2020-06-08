---
layout:     post
title:      VPC Endpoints - Gateway vs Interface, VPC Peering and VPC Flow Logs
date:       2020-06-06 12:31:19
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

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## VPC Endpoint 

![](/images/aws/00-icons/vpcendpoint.png)
- Securely connect your VPC to another service
- Gateway endpoint	
	- Securely connect to Amazon S3 and DynamoDB
	- Endpoint serves as a target in your route table for traffic
	- Provide access to endpoint (endpoint, identity and resource policies)
- Interface endpoint
	- Securely connect to AWS services EXCEPT FOR Amazon S3 and DynamoDB
	- Powered by PrivateLink (keeps network traffic within AWS network)
	- Needs a elastic network interface (ENI) (entry point for traffic)
- (Avoid DDoS & MTM attacks) Traffic does NOT go thru internet
- (Simple) Does NOT need Internet Gateway, VPN or NAT

## VPC Peering

![](/images/aws/vpc-peering.png)
- Connect VPCs belonging to same or different AWS accounts irrespective of the region of the VPCs
- Allows private communication between the connected VPCs
- Peering uses a request/accept protocol
	- Owner of requesting VPC sends a request 
	- Owner of the peer VPC has one week to accept
- Remember : Peering is not transitive
- Remember : Peer VPCs cannot have overlapping address ranges

## VPC Flow Logs

![](/images/aws/00-icons/vpcflowlogs.png) 
- Monitor network traffic 
- Troubleshoot connectivity issues (NACL and/or security groups misconfiguration)
- Capture traffic going in and out of your VPC (network interfaces)
- Can be created for 
	- a VPC
	- a subnet
	- or a network interface (connecting to ELB, RDS, ElastiCache, Redshift etc)
- Publish logs to Amazon CloudWatch Logs or Amazon S3
- Flow log records contain ACCEPT or REJECT 
	- Is traffic is permitted by security groups or network ACLs?

## Troubleshoot using VPC Flow Logs 

![](/images/aws/00-icons/user.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/nacl.png)
![](/images/aws/00-icons/subnet.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/securitygroup.png)
![](/images/aws/00-icons/ec2.png)

- Inbound traffic rules - NACL IN, SG IN, NACL OUT (SG OUT NOT checked)
	- If inbound request is rejected, SG or NACL could be mis-configured
	- If outbound response is rejected, NACL is mis-configured
- Outbound traffic rules - SG OUT, NACL OUT, NACL IN (SG IN NOT checked)
	- If outbound request is rejected, SG or NACL could be mis-configured
	- If inbound response is rejected, NACL is mis-configured
- Problem with response => Problem with NACL
- Problem with request could be problems with NACL or SG