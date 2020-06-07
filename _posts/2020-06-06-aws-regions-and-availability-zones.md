---
layout:     post
title:      Regions and Availability Zones - AWS Certification
date:       2020-06-07 00:00:00
summary:    Let's get a quick overview of Regions and Availability Zones from an AWS certification perspective. We will look at important certification questions regarding Regions and Availability Zones. 
categories:  AWS_CLOUD General
permalink:  /aws-certification-region-availability-zones-az
---

Let's get a quick overview of Regions and Availability Zones from an AWS certification perspective. We will look at important certification questions regarding Regions and Availability Zones.

## You will learn
- What is a Region?
- What is an Availability Zone?
- Why do we need Regions and Availability Zones?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target="_blank"}


## Regions and Zones 
![](/images/aws/vpc/1-SingleDataCenter.png)
- Imagine that your application is deployed in a data center in London
- What would be the challenges?
	- Challenge 1 : Slow access for users from other parts of the world (**high latency**)
	- Challenge 2 : What if the data center crashes? 
		- Your application goes down (**low availability**)



## Multiple data centers
![](/images/aws/vpc/2-2-datacenters-london.png)
- Let's **add in one more data center** in London
- What would be the challenges?
	- Challenge 1 : Slow access for users from other parts of the world
	- Challenge 2 (**SOLVED**) : What if one data center crashes?
		- Your application is **still available** from the other data center
	- Challenge 3 : What if **entire region** of London is unavailable?
		- Your application goes down
		

## Multiple regions
![](/images/aws/vpc/3-2-datacenters-london-mumbai.png)
- Let's add a new region : Mumbai
- What would be the challenges?
	- Challenge 1 (**PARTLY SOLVED**) : Slow access for users from other parts of the world
		- You can solve this by adding deployments for your applications in other regions
	- Challenge 2 (SOLVED) : What if one data center crashes?
		- Your application is still live from the other data centers
	- Challenge 3 (**SOLVED**) : What if entire region of London is unavailable?
		- Your application is served from Mumbai


## Regions
![](/images/aws/aws-regions-and-az.png)
- Imagine setting up your own data centers in different regions around the world 
	- **Would that be easy?**
- (Solution) AWS provides **20+ regions** around the world (expanding every year)
- Regions - Advantages
	- High Availability
	- Low Latency
	- Adhere to government **regulations**

## How do you choose AWS Regions?
![](/images/aws/region.png)
- Choose the right region(s) based on:
	- Where are your users located?
	- Where is your data located?
	- Regulatory and security compliance needs
- AWS Services can be:
	- Regional (OR)
	- Global



## AWS Availability Zones
![](/images/aws/region-az.png) 
- **Isolated locations** in a Region
- Each AWS Region has at least two Availability Zones
- **Increase availability** of applications in the same region


## AWS Regions and Availability Zones examples

 
> New Regions and AZs are constantly added
 
| Region Code | Region  | Availability Zones | Availability Zones List |
|:--:|--|:--:|--|
| us-east-1   |  US East (N. Virginia)   | 6        | us-east-1a us-east-1b <BR/>us-east-1c  us-east-1d<BR/> us-east-1e us-east-1f      |
|  eu-west-2   |   Europe (London)     |   3     |  eu-west-2a eu-west-2b <BR/>eu-west-2c   |
|ap-south-1|Asia Pacific(Mumbai)|3|ap-south-1a ap-south-1b <BR/>ap-south-1c|

## Regions and Availability Zones - AWS Certification Exam Practice Questions

Coming Soon..