---
layout:     post
title:      GCP Regions and Availability Zones - GCP Certification Cheat Sheet
date:       2020-06-07 00:00:00
summary:    Let's get a quick overview of Regions and Availability Zones from an GCP certification perspective. We will look at important certification questions regarding Regions and Availability Zones. 
categories:  GCP_CLOUD General
permalink:  /gcp-certification-region-availability-zones-az
---

Let's get a quick overview of Regions and Availability Zones from an GCP certification perspective. We will look at important certification questions regarding Regions and Availability Zones.

## You will learn
- What is a Region?
- What is an Availability Zone?
- Why do we need Regions and Availability Zones?

## GCP Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
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
![](/gcpimages/02-architecture/regions.png)
- Imagine setting up data centers in different regions around the world 
	- **Would that be easy?**
- (Solution) Google provides **20+ regions** around the world 
	- Expanding every year
- **Region** : Specific geographical location to host your resources
- **Advantages**:
	- High Availability
	- Low Latency
	- Global Footprint
	- Adhere to government **regulations**

## Zones
![](/gcpimages/region-zones.png)
- How to achieve high availability in the same region (or geographic location)?
	- Enter **Zones**
- Each Region has three or more **zones**
- (Advantage) **Increased availability and fault tolerance** within same region
- (Remember) Each Zone has **one or more discrete clusters** 
	- **Cluster** : distinct physical infrastructure that is housed in a data center
- (Remember) Zones in a region are connected through **low-latency** links

## Regions and Zones examples
 
> New Regions and Zones are constantly added
 
| Region Code | Region  |  Zones | Zones List |
|:--:|--|:--:|--|
| us-west1   |  The Dalles, Oregon, North America   | 3        | us-west1-a <BR/>us-west1-b<BR/> us-west1-c      |
|  europe-north1   |   Hamina, Finland, Europe     |   3     |  europe-north1-a, europe-north1-b  <BR/>europe-north1-c   |
|asia-south1|Mumbai, India APAC|3|asia-south1-a, asia-south1-b <BR/>asia-south1-c|
