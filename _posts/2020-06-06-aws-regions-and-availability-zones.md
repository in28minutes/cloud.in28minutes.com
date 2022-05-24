---
layout:     post
title:      AWS Regions and Availability Zones - AWS Certification Cheat Sheet
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

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>


## Regions and Zones - Need

Why do we need Regions and Zones?

Let's first understand that with a simple scenario.

### Step 1 : Single Data Center

Scenario: Imagine that your application is deployed in a data center in London.

![](/images/aws/vpc/1-SingleDataCenter.png)

What would be the challenges?
- Challenge 1 : Slow access for users from other parts of the world (**high latency**)
- Challenge 2 : What if the data center crashes?
	- Your application goes down (**low availability**)

### Step 2 : Multiple data centers in London

Let's **add in one more data center** in London.

![](/images/aws/vpc/2-2-datacenters-london.png)

What would be the challenges now?
- Challenge 1 : Slow access for users from other parts of the world
- Challenge 2 (**SOLVED**) : What if one data center crashes?
	- Your application is **still available** from the other data center
- Challenge 3 : What if **entire region** of London is unavailable?
	- Your application goes down
		
### Step 3 : Multiple regions

Let's add a new region : Mumbai.

![](/images/aws/vpc/3-2-datacenters-london-mumbai.png)

What would be the challenges?
- Challenge 1 (**PARTLY SOLVED**) : Slow access for users from other parts of the world
	- You can solve this by adding deployments for your applications in other regions
- Challenge 2 (SOLVED) : What if one data center crashes?
	- Your application is still live from the other data centers
- Challenge 3 (**SOLVED**) : What if entire region of London is unavailable?
	- Your application is served from Mumbai


## Regions

![](/images/aws/aws-regions-and-az.png)

Imagine setting up your own data centers in different regions around the world. That's not easy unless you are a big corporate!

AWS provides **20+ regions** around the world (expanding every year). 

Advantages of Regions include:
- High Availability
- Low Latency
- Adhere to government **regulations**

You can choose the right region(s) for your application based on:
- Where are your users located?
- Where is your data located?
- Regulatory and security compliance needs

## AWS Availability Zones

Availability Zones are **Isolated locations** in a Region. 

Each AWS Region has at least two Availability Zones. 

Availability Zones **increase availability** of applications in the same region.

![](/images/aws/region-az.png) 


## AWS Regions and Availability Zones examples

New Regions and AZs are constantly added. Here is table showing examples of regions and AZs.
 
| Region Code | Region  | Availability Zones | Availability Zones List |
|:--:|--|:--:|--|
| us-east-1   |  US East (N. Virginia)   | 6        | us-east-1a us-east-1b <BR/>us-east-1c  us-east-1d<BR/> us-east-1e us-east-1f      |
|  eu-west-2   |   Europe (London)     |   3     |  eu-west-2a eu-west-2b <BR/>eu-west-2c   |
|ap-south-1|Asia Pacific(Mumbai)|3|ap-south-1a ap-south-1b <BR/>ap-south-1c|
