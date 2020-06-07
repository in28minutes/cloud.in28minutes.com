---
layout:     post
title:      Public Subnet vs Private Subnet - Routing and Internet Gateway - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Public Subnet vs Private Subnet from an AWS certification perspective. We will look at important certification questions regarding Public Subnet vs Private Subnet. 
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-public-subnet-vs-private-subnet
---

Let's get a quick overview of Public Subnet vs Private Subnet from an AWS certification perspective. We will look at important certification questions regarding Public Subnet vs Private Subnet.

## You will learn
- What are Public Subnets and Private Subnet?
- When do we use Public Subnet vs Private Subnet?
- How is Public Subnet different from Private Subnet?
- What is an Internet Gateway?
- Why is Internet Gateway Important?
- What is Routing?
- What are Route Tables?
- How does Routing happen inside AWS?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}



## Public Subnet

![](/images/aws/00-icons/subnet.png) 
![](/images/arrowbi.png)
![](/images/aws/00-icons/internetgateway.png) 
![](/images/arrowbi.png)
![](/images/aws/00-icons/internet.png) 
- Communication allowed from subnet to internet
- Communication allowed from internet to subnet

## Routing on the internet
![](/images/aws/vpc/10-vpc-router.png)
- You have an IP address of a website you want to visit
- There is **no direct connection** from your computer to the website
- Internet is actually a **set of routers** routing traffic
- Each router has a set of rules that help it decide the path to the destination IP address

## Routing inside AWS

| Destination             | Target                 |
|--|--|
| 172.31.0.0/16           | Local                  |
|        0.0.0.0/0        | igw-1234567            |

- In AWS, **route tables** are used for routing
- Route tables can be associated with VPCs and subnets
- Each route table consists of a **set of rules** called routes
	- Each route or routing rule has a **destination and target**
	- What CIDR blocks (range of addresses) should be routed to which target resource?
- **Rule 1** - Route requests to VPC CIDR 172.31.0.0/16 (172.31.0.0 to 172.31.255.255) to local resources within the VPC
- **Rule 2** - Route all other IP addresses (0.0.0.0/0) to internet (internet gateway)

## Execution of Route Table

| Destination             | Target                 |
|--|--|
| 172.31.0.0/16           | Local                  |
|        0.0.0.0/0        | igw-1234567            |

- What happens if I search for an address **172.31.0.10**?
 	- Two destinations match -  172.31.0.0/16 (172.31.0.0 to 172.31.255.255) and 0.0.0.0/0
 	- The most specific rule wins. 172.31.0.0/16 is more specific
 	- Result : Routing to a local resource
- What happens if I search for an address **69.209.0.10**?
 	- One destination match - 69.208.0.10 
 	- Result : Routing to internet
- The **most specific matching route** wins

## Public Subnet vs Private Subnet

![](/images/aws/00-icons/subnet.png) 
![](/images/arrowbi.png) 
![](/images/aws/00-icons/internetgateway.png) 
![](/images/arrowbi.png) 
![](/images/aws/00-icons/internet.png) 

|Name | Destination             | Target                 | Explanation               |
|--|--|--|--|
|RULE 1| 172.31.0.0/16            | Local                  | Local routing   |
|RULE 2|        0.0.0.0/0        | igw-1234567            | Internet routing|

- An **Internet Gateway** enables internet communication for subnets
- Any subnet which has a route to an internet gateway is called a **public subnet**
- Any subnet which **DOES NOT** have route to an internet gateway is called a **private subnet**

## More about Internet Gateway
![](/images/aws/00-icons/subnet.png) 
![](/images/arrowbi.png) 
![](/images/aws/00-icons/internetgateway.png) 
![](/images/arrowbi.png) 
![](/images/aws/00-icons/internet.png) 

- Sits between subnet (VPC) resources  and internet
- **One to one mapping** with a VPC
- Supports IPv4 and IPv6
- Translate private IP address to public IP address and vice-versa
- **DHCP option set**: Assign custom host names and IP addresses to EC2 instances


## Public Subnet vs Private Subnet - AWS Certification Exam Practice Questions

Coming Soon..