---
layout:     post
title:      Private Subnets - NAT Gateway vs NAT Instance - AWS Certification
date:       2020-06-06 12:31:19
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

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## Network Address Translation(NAT) Instance and Gateway
- How do you **allow instances in a private subnet to download software updates** and security patches while denying inbound traffic from internet?
- How do you allow instances in a private subnet to **connect privately to other AWS Services** outside the VPC?
- **Three Options**:
	- **NAT Instance**: Install a EC2 instance with specific NAT AMI and configure as a gateway
	- **NAT Gateway**: Managed Service
	- **Egress-Only Internet Gateways**: For IPv6 subnets

## Private Subnet - Download Patches
![](/images/aws/00-icons/ec2.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/natgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internetgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internet.png) 

- Cannot be accessed from internet.
- Might allow traffic to internet using a NAT Device.

## NAT instance

![](/images/aws/nat-instance-diagram.png)
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html
- **Step 1**: Create EC2 instance
	- AMI - Linux *amzn-ami-vpc-nat
	- Public subnet with **public IP address or Elastic IP**
- **Step 2**: Assign Security Group
	- Inbound - HTTP(80) HTTPS(443) from private subnet
	- Outbound - HTTP(80) & HTTPS(443) to internet (0.0.0.0/0)
- **Step 3**: Private Subnet Route Table
	- Redirect all outbound traffic (0.0.0.0/0) to the NAT instance

## NAT gateway
![](/images/aws/00-icons/ec2.png) 
![](/images/arrow.png)
![](/images/aws/00-icons/natgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internetgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internet.png) 

- AWS Managed Service 
- Step 1: Get an **Elastic IP Address**
- Step 2: Create NAT gateway in a **PUBLIC subnet** with the Elastic IP Address.
- Step 3: Private subnet route  - **all outbound traffic (0.0.0.0/0) to NAT gateway**.

## NAT gateway - Remember
![](/images/aws/00-icons/ec2.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/natgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internetgateway.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/internet.png) 
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

## Private Subnet Nat Gateway and Instance - AWS Certification Exam Practice Questions

Coming Soon..