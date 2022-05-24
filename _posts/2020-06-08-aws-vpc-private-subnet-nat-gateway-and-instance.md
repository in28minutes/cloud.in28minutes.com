---
layout:     post
title:      Private Subnets - NAT Gateway vs NAT Instance - AWS Certification Cheat Sheet
date:       2020-09-12 12:31:19
summary:    Let's get a quick overview of how you can enable Private Subnets to download patches using NAT Gateway and NAT Instance. We will look at important certification questions regarding Private Subnet, NAT Gateway and NAT Instance. 
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-private-subnet-nat-gateway-and-instance
---

Let's get a quick overview of how you can enable Private Subnets to download patches using NAT Gateway and NAT Instance. We will look at important certification questions regarding Private Subnet, NAT Gateway and NAT Instance.

## You will learn
- What is Private Subnet?
- What is Network Address Translation?
- How do you allow Private Subnets to download patches using NAT Gateway and NAT Instance?
- When do we use NAT Gateway and NAT Instance?
- How do NAT Gateway and NAT Instance compare?

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>


## Network Address Translation(NAT) Instance and Gateway
Consider these two questions:
- How do you **allow instances in a private subnet to download software updates** and security patches while denying inbound traffic from internet?
- How do you allow instances in a private subnet to **connect privately to other AWS Services** outside the VPC?

There are **Three Options**:
- **NAT Instance**: Install a EC2 instance with specific NAT AMI and configure as a gateway
- **NAT Gateway**: Managed Service
- **Egress-Only Internet Gateways**: For IPv6 subnets

## Private Subnet - Download Patches

Here's the high level architecture:

![](/images/aws/00-icons/ec2.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/natgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internetgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internet.png) 

## NAT instance

Here are the steps in setting up a NAT instance:
- **Step 1**: Create EC2 instance
	- AMI - Linux *amzn-ami-vpc-nat
	- Public subnet with **public IP address or Elastic IP**
- **Step 2**: Assign Security Group
	- Inbound - HTTP(80) HTTPS(443) from private subnet
	- Outbound - HTTP(80) & HTTPS(443) to internet (0.0.0.0/0)
- **Step 3**: Private Subnet Route Table
	- Redirect all outbound traffic (0.0.0.0/0) to the NAT instance

## NAT gateway

NAT gateway is an AWS Managed Service.

Here are the steps in setting it up:
- Step 1: Get an **Elastic IP Address**
- Step 2: Create NAT gateway in a **PUBLIC subnet** with the Elastic IP Address.
- Step 3: Private subnet route  - **all outbound traffic (0.0.0.0/0) to NAT gateway**.

Here are few things to remember about NAT gateway:
- Prefer **NAT gateway over NAT instance**
	- Less administration, more availability and higher bandwidth
	- NAT Gateway does not need any security group management.
- NAT Gateway supports **IPv4 ONLY**.
	- Use Egress-Only Internet Gateways for IPv6.
- NAT Gateway uses the Internet Gateway.

## NAT gateway vs NAT instance

|Feature|NAT gateway|NAT instance|
|--|:--|:--|
|Managed by|AWS|You|
|Created in|Public Subnet| Public Subnet|
|Internet Gateway| Needed | Needed|
|High Availability| Yes (in an AZ) <BR/>Multi AZ (higher availability) | You are responsible.|
|Bandwidth| Upto 45 Gbps|Depends on EC2 instance type|
|Public IP addresses| Elastic IP address| Elastic IP address OR Public IP Address| 
|Disable source destination check|No|Required|
|Security groups| No specific configuration needed| Needed on NAT instance |
|Bastion servers| No| Can be used as a Bastion server|
