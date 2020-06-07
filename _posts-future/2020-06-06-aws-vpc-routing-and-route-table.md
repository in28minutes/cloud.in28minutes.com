---
layout:     post
title:      VPC and Subnet Route Tables - Routing in AWS - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Routing and Route Tables in AWS.
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-vpc-route-table-and-routing
---

Let's get a quick overview of Routing and Route Tables in AWS.

## You will learn
- What is routing?
- What is route table?
- How does routing happen on internet?
- How does routing happen in AWS?
- What is VPC Route Table?
- What is Subnet Route Table?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}

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

## VPC Main Route Table

![](/images/aws/00-icons/vpc.png) 
![](/images/aws/00-icons/vpcrouter.png) 

| Destination             | Target                 |
|--|--|
| 172.31.0.0/16           | Local                  |

- Each VPC has a **main route table**, by default
- **Main route table** has a default route enabling communication between resources in all subnets in a VPC
- Default route rule CANNOT be deleted/edited
- HOWEVER you can add/edit/delete other routing rules to the main route table

## Subnet Route Tables

![](/images/aws/00-icons/subnet.png) 
![](/images/aws/00-icons/vpcrouter.png) 

- Each subnet can have its **own** route table OR **share** its route table with the VPC
- If a subnet does not have a route table associated with it, it **implicitly** uses the route table of its VPC
- Multiple subnets can share a route table
- HOWEVER at any point in time, a subnet can be associated with one route table ONLY


## VPC Route Table and Routing - AWS Certification Exam Practice Questions

Coming Soon..