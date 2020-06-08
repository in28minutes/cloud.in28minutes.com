---
layout:     post
title:      Route 53 - Routing Policies - Geoproximity and Geolocation - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Route 53. We will look at Route 53 Routing Policies including Geoproximity and Geolocation.
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-route-53-routing-policies-geoproximity-geolocation
---

Let's get a quick overview of Route 53. We will look at Route 53 Routing Policies including Geoproximity and Geolocation.

## You will learn
- What is Route 53?
- What are the different Route 53 Routing Policies?
- What is difference between different Route 53 Routing Policies - Geoproximity vs Geolocation vs ...?
- What is a Route 53 Hosted Zone?
- How do you manage DNS Records and Routing Policies?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## Route 53 

![](/images/aws/00-icons/route53.png) 
- What would be the steps in setting up a website with a domain name (for example, in28minutes.com)?
	- Step I : Buy the domain name in28minutes.com (Domain Registrar)
	- Step II : Setup your website content (Website Hosting)
	- Step III : Route requests to in28minutes.com to the my website host server (DNS)
- Route 53 = Domain Registrar + DNS
	- Buy your domain name
	- Setup your DNS routing for in28minutes.com

## Route 53 - DNS (Domain Name Server)

![](/images/aws/00-icons/route53.png) 

> How should traffic be routed for in28minutes.com?

- Configure Records:
	- Route api.in28minutes.com to the IP address of api server
	- Route static.in28minutes.com to the IP address of http server
	- Route email (ranga@in28minutes.com) to the mail server(mail.in28minutes.com)
	- Each record is associated with a TTL (Time To Live) - How long is your mapping cached at the routers and the client?

## Route 53 Hosted Zone

![](/images/aws/00-icons/route53.png) 
- Container for records containing DNS records routing traffic for a specific domain
- I want to use Route 53 to manage the records (Name Server) for in28minutes.com
	- Create a hosted zone for in28minutes.com in Route 53
- Hosted zones can be
	- private - routing within VPCs
	- public - routing on internet
- Manage the DNS records in a Hosted Zone

## Standard DNS Records

![](/images/aws/dns-record-types.png)

- A - Name to IPV4 address(es)
- AAAA - Name to IPV6 address(es )
- NS - Name Server containing DNS records
	- I bought in28minutes.com from GoDaddy (Domain Registrar)
	- BUT I can use Route 53 as DNS
		- Create NS records on GoDaddy 
		- Redirect to Route 53 Name Servers
- MX - Mail Exchange
- CNAME - Name1 to Name2

## Route 53 Specific Extension - Alias records

![](/images/aws/00-icons/route53.png) 

- Route traffic to selected AWS resources 
	- Elastic Beanstalk environment
	- ELB load balancer
	- Amazon S3 bucket
	- CloudFront distribution 
- Alias records can be created for 
	- root(in28minutes.com) and 
	- non root domains(api.in28minutes.com) 
- COMPARED to CNAME records which can only be created for 
	- non root domains (api.in28minutes.com)

## Route 53 - Routing

![](/images/aws/route53-routing.png)

- Route 53 can route across Regions
	- Create ALBs in multiple regions and route to them!
	- Offers multiple routing policies

## Route 53 Routing Policies 
 
| Policy | Description  | 
|--|:--|
| Simple | Maps a domain name to (one or more) IP Addresses|
|Weighted | Maps a single DNS name to multiple weighted resources <BR/>10% to A, 30% to B, 60% to C (useful for canary deployments)|
|Latency |Choose the option with minimum latency <BR/>Latency between hosts on the internet can change over time|
|Failover | Active-passive failover. <BR/>Primary Health check fails (optional cloud Watch alarm) => DR site is used|
|Geoproximity| Choose the nearest resource (geographic distance) to your user. Configure a bias.|
|Multivalue answer |Return multiple healthy records (upto 8) at random <BR/>You can configure an (optional) health check against every record|
|Geolocation | Choose based on the location of the user|

## Route 53 Routing Policies - Geolocation

![](/images/aws/00-icons/route53.png) 

- Choose based on the location of the user 
	- continent, country or a (state in USA) 
	- Send traffic from Asia to A
	- Send traffic from Europe to B etc. 
- Record set for smallest geographic region has priority
- Use case 
	- Restrict distribution of content to specific areas where you have distribution rights
- (RECOMMENDED) Configure a default policy (used if none of the location records match)
	- Otherwise, Route 53 returns a "no answer" if none of the location records match
