---
layout:     post
title:      Virtual Private Cloud and Subnet Fundamentals - VPC - AWS Certification
date:       2020-09-12 12:31:19
summary:    Let's get a quick overview of Virtual Private Cloud and Subnets from an AWS certification perspective. We will look at important certification questions regarding Virtual Private Cloud and Subnets. 
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-virtual-private-cloud-subnet-vpc
---

Let's get a quick overview of Virtual Private Cloud (VPC) from an AWS certification perspective. We will look at important certification questions regarding Virtual Private Cloud - VPC.

## You will learn
- What is Virtual Private Cloud VPC?
- Why do we need Virtual Private Cloud?
- When do we use Virtual Private Cloud?
- What are the important components of a VPC?
- What is an CIDR?
- How do you assign CIDR blocks to VPC and Subnets?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## Need for Amazon VPC 

![](/images/aws/vpc/1-SingleDataCenterWithDB.png)

Think about this: In a corporate network or an on-premises data center:
- Can anyone on the internet **see the data exchange** between the application and the database? 
	- **No**
- Can anyone from internet **directly connect to your database**? 
	- Typically **NO**. You need to connect to your corporate network and then access your applications or databases.

Corporate network provides a **secure internal network** protecting your resources, data and communication from external users.

How do you do create **your own private network** in the cloud?
- Enter **Virtual Private Cloud (VPC)**

## Amazon VPC (Virtual Private Cloud)

![](/images/aws/00-icons/VPC.png)
VPC (Virtual Private Cloud) is your **own isolated network** in AWS cloud. Network traffic within a VPC is isolated (not visible) from all other Amazon VPCs:
- You **control all the traffic** coming in and going outside a VPC

**(Best Practice)**: Create all your AWS resources (compute, storage, databases etc) **within a VPC**. This enables you to:
- Secure resources from unauthorized access AND 
- Enable secure communication between your cloud resources

## Need for VPC Subnets
![](/images/aws/00-icons/user.png)
![](/images/arrow.png) 
![](/images/aws/00-icons/elb.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/ec2instance.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/database.png) 

Different resources are created on cloud - databases, compute (EC2) etc. Each type of resource has **its own access needs**:
- Public Elastic Load Balancers are accessible from internet (**public** resources)
- Databases or EC2 instances should NOT be accessible from internet
	- ONLY applications within your network (VPC) should be able to access them(**private** resources)

How do you **separate public resources from private resources** inside a VPC?

(Solution) **Create different subnets** for public and private resources.
	- Resources in a public subnet **CAN** be accessed from internet
	- Resources in a private subnet **CANNOT** be accessed from internet
	- BUT resources in public subnet can talk to resources in private subnet

![](/images/aws/vpc/8-vpc-subnets.png)

Each VPC is created in a Region. Each Subnet is created in an Availability Zone
- **Example** : VPC - us-east-1 => Subnets - AZs us-east-1a or us-east-1b or ..

## Addressing for Resources - IP address

![](/images/aws/00-icons/elb.png) 
![](/images/aws/00-icons/ec2instance.png) 

How do you identify resources on a network ( public (internet) or private(intranet) )? 

Each resource has an **IP address**.

There are **two IP address formats**:
- **IPv4** (Internet Protocol version 4 - numeric 32 bit). Example : 127.255.255.255
- **IPv6** (Internet Protocol version 6 - alphanumeric 128 bit). Example : 2001:0db8:85a3:0000:0000:8a2e:0370:7334

IPv4 allows a total of 4.3 billion addresses. We are running out of the IPv4 address space. Therefore, IPv6 is introduced as an extension

While IPv4 and IPv6 are supported on AWS, IPv4 is the most popularly used address format within an AWS VPC. 

## CIDR (Classless Inter-Domain Routing) Blocks
Typically resources in same network use similar IP address to make routing easy:
- Example: Resources inside a specific network can use IP addresses from 69.208.0.0 to 69.208.0.15

How do you express a **range of addresses** that resources in a network can have?
- Use a **CIDR block**

A **CIDR block** consists of a **starting IP address(69.208.0.0)** and a **range(/28)**
- Example: CIDR block 69.208.0.0/28 represents addresses from 69.208.0.0 to 69.208.0.15 - a total of 16 addresses

**Quick Tip**: 69.208.0.0/28 indicates that the first 28 bits (out of 32) are fixed. Last 4 bits can change => 2 to the power 4  = 16 addresses.

## CIDR Exercises
![](/images/aws/cidr-examples.png)
Exercise 1: How many addresses does **69.208.0.0/26** represent?
- 2 to the power (32-26 = 6) = 64 addresses from 69.208.0.0 to 69.208.0.63

Exercise 2: How many addresses does **69.208.0.0/30** represent?
- 2 to the power (32-30 = 2) = 4 addresses from 69.208.0.0 to 69.208.0.3

Exercise 3: What is the difference between **0.0.0.0/0** and **0.0.0.0/32**?
- 0.0.0.0/0 represent all IP addresses. 0.0.0.0/32 represents just one IP address 0.0.0.0.

## CIDR Block Example - Security Group

Consider the Security Group Configuration below:

| Direction | Protocol | Port Range | Source/Destination   |
|--|:--:|--:|--|
| Inbound   |    TCP   |        443 |  172.31.0.0/16       |
| Inbound   |    TCP   |        22  |  183.82.143.132/32   |
| Outbound  |    All   |        All |  0.0.0.0/0           |

This Security Group Configuration:
- Allows HTTPS (TCP - 443) requests from a range of addresses (172.31.0.0/16)
- Allows SSH (TCP - 22) from a single IP address (183.82.143.132/32)
- Allows all outbound communication
- All other inbound/outbound traffic is denied

## VPC CIDR Blocks

Each VPC is associated with a **CIDR Block**. CIDR block of VPC can be from /16 (65536 IP addresses) to /28 (16 IP addresses)
- **Example 1** : VPC with CIDR block 69.208.0.0/24 - 69.208.0.0 to 69.208.0.255
- **Example 2** : VPC with CIDR block 69.208.0.0/16 - 69.208.0.0 to 69.208.255.255

## Choosing a CIDR Block for VPC

![](/images/aws/vpc/8-vpc-subnets.png)
Be careful in choosing a CIDR block. **Choose a wider range** than you would need. There **CANNOT be an overlap** of a VPC CIDR block with any other connected network.

All addresses inside a VPC CIDR range are **private addresses**:
- Cannot route to private addresses from internet
- Assign and use public IP addresses to communicate with VPC resources from internet

## Choosing a CIDR Block for a Subnet

![](/images/aws/vpc/8-vpc-subnets.png)
Subnet provides a **grouping for resources inside a VPC**.

The CIDR block of a subnet **must be a subset or the same** as the CIDR block for the VPC. **Minimum** subnet range is /28 (16 addresses).

In each subnet, 5 IP address (first four and the last) are **reserved** by AWS.

Every new AWS account has a default VPC (/16) in every region with a public subnet(/20) in every AZ.

Address range of a VPC CAN be extended (Add new CIDR Block).

Address range of a Subnet CANNOT be changed.


## VPC and Subnets - Questions

| Question | Answer  | 
|--|--|
|Can I have a VPC spread over two regions? | No|
|Can I have multiple VPCs in same region?| Yes|
|Is communication between two resources in a VPC visible outside VPC? | No |
|Can you allow external access to your resources in a VPC?| Yes|
|Can I have a subnet spread over two regions?| No|
|Can I have a subnet spread over two availability zones?| No|
| Can I have two subnets in one availability zone?| Yes|
| Can I have a subnet in availability zone ap-south-1a if it's VPC is in the region us-east-1?| No. Subnet should be in AZs belonging to the VPC's region|

## Virtual Private Cloud - AWS Certification Exam Practice Questions

Coming Soon..