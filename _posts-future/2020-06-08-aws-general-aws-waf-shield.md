---
layout:     post
title:      AWS Shield, AWS WAF and AWS Macie - Protect Resources and Data - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of AWS Shield, AWS WAF and AWS Macie. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-aws-shield-waf-macie
---

Let's get a quick overview of AWS Shield, AWS WAF and AWS Macie.

## You will learn
- What is AWS Shield and AWS WAF?
- When do we use AWS Shield and WAF?
- How does AWS Macie help in protecting your data in Amazon S3?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}

## AWS Shield
![](/images/aws/00-icons/shield.png) 
![](/images/aws/00-icons/route53.png) 
![](/images/aws/00-icons/cloudfront.png) 
![](/images/aws/00-icons/ec2.png) 
![](/images/aws/00-icons/elb.png) 

- Shields from Distributed Denial of Service (DDoS) attacks
	- Disrupt normal traffic of a server by overwhelming it with a flood of Internet traffic
- Protect
	- Amazon Route 53
	- Amazon CloudFront
	- AWS Global Accelerator
	- Amazon Elastic Compute Cloud (EC2) instances
	- Elastic Load Balancers (ELB)

## AWS Shield - Standard and Advanced

![](/images/aws/00-icons/shield.png) 
![](/images/aws/00-icons/cloudfront.png)

- AWS Shield Standard
	- Zero Cost. Automatically enabled.
	- Protection against common infrastructure (layer 3 and 4) DDoS attacks
- AWS Shield Advanced
	- Paid service
	- Enhanced protection for Amazon EC2, Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53
	- 24x7 access to the AWS DDoS Response Team (DRT)
	- Protects your AWS bill from usage spikes as a result of a DDoS attack
- Protect any web application (from Amazon S3 or external) from DDoS by putting Amazon CloudFront enabled with AWS Shield in front of it

## AWS WAF - Web Application Firewall

![](/images/aws/00-icons/waf.png) 
- AWS WAF protect your web applications from OWASP Top 10 exploits, CVE and a lot more!
	- OWASP (Open Web Application Security Project) Top 10 
		- List of broadly agreed "**most critical security risks to web applications**" 
		- Examples : SQL injection, cross-site scripting etc
	- Common Vulnerabilities and Exposures (CVE) is a list of information-security vulnerabilities and exposures
- Can be deployed on Amazon CloudFront, Application Load Balancer, Amazon API Gateway
- Customize rules & trigger realtime alerts (CloudWatch Alarms)
- Web traffic filtering : block attacks
	- Filter traffic based on IP addresses, geo locations, HTTP headers and body (block attacks from specific user-agents, bad bots, or content scrapers)

## Amazon Macie
- Fully managed data security and data privacy service
- Automatically discover, classify, and protect sensitive data in Amazon S3 buckets
- When migrating data to AWS use S3 for staging 
	- Run Macie to discover secure data
- Uses machine learning 
- Recognizes sensitive data 
	- Example: personally identifiable information (PII) or intellectual property
- Provides you with dashboards and alerts 
	- Gives visibility into how data is being accessed or moved