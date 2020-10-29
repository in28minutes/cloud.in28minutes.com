---
layout:     post
title:      AWS CloudTrail vs Config vs CloudWatch - AWS Certification Cheat Sheet
date:       2020-10-28 12:31:19
summary:    Let's get a quick overview of differences between AWS CloudTrail, AWS Config and Amazon CloudWatch. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-aws-cloudtrail-vs-config-vs-cloudwatch
---

Let's get a quick overview of differences between AWS CloudTrail, AWS Config and Amazon CloudWatch.

## You will learn
- What is AWS CloudTrail?
- What is AWS Config?
- When do you use Amazon CloudWatch?
- Comparison - AWS CloudTrail vs Config vs CloudWatch
- When do you use - AWS CloudTrail vs Config vs CloudWatch

## AWS Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## AWS CloudTrail

![](/images/aws/00-icons/cloudtrail.png)

- Track events, API calls, changes made to your AWS resources: 
	- Who made the request?
	- What action was performed?
	- What are the parameters used?
	- What was the end result?
- (USE CASE) Compliance with regulatory standards
- (USE CASE) Troubleshooting. Locate a missing resource
- Delivers log files to S3 and/or Amazon cloud watch logs log group ( S3 is default )
- You can setup SNS notifications for log file delivery

## AWS Cloud Trail Types

![](/images/aws/00-icons/cloudtrail.png)

- Multi Region Trail 
	- One trail of all AWS regions
	- Events from all regions can be sent to one CloudWatch logs log group
- Single Region Trail 
	- Only events from one region
	- Destination S3 bucket can be in any region

## AWS Cloud Trail - Good to know

![](/images/aws/00-icons/cloudtrail.png)

- Log files are automatically encrypted with Amazon S3 SSE
- You can configure S3 Lifecycle rules to archive or delete log files
- Supports log file integrity 
	- You can prove that a log file has not been altered

## AWS Config

![](/images/aws/00-icons/config.png) 

- **Auditing** 
	- Create a complete inventory of your AWS resources
- **Resource history and change tracking** 
	- Find how a resource was configured at any point in time
	- Configuration of deleted resources would be maintained
	- Delivers history file to S3 bucket every 6 hours 
	- Take configuration snapshots when needed
- **Governance**
	- Customize Config Rules for specific resources or for entire AWS account
	- Continuously evaluate compliance against desired configuration
	- Get a SNS notification for every configuration change
- **Consistent rules and compliance** across AWS accounts:
	- Group Config Rules and Remediation Actions into Conformance Packs

## Predefined Config Rule Examples (80+)

- **alb-http-to-https-redirection-check** - Checks whether HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancers
- **ebs-optimized-instance** - Checks whether EBS optimization is enabled for your EC2 instances that can be EBS-optimized
- **ec2-instance-no-public-ip** - Do EC2 instances have public IPs?
- **encrypted-volumes** - Are all EC2 instance attached EBS volumes encrypted?
- **eip-attached** - Are all Elastic IP addresses used?
- **restricted-ssh** - Checks whether security groups that are in use disallow unrestricted incoming SSH traffic

## AWS Config Rules

- (Feature) Create Lambda functions with your custom rules
- (Feature) You can setup auto remediation for each rule
	- Take immediate action on a non compliant resource
	- (Example) Stop EC2 instances without a specific tag!
- Enable AWS Config to use the rules
	- No Free Tier
	- More rules to check => More $$$$

## AWS Config + AWS CloudTrail

- AWS Config 
	- What did my AWS resource look like?
- AWS CloudTrail 
	- Who made an API call to modify this resource?

## Monitoring AWS with Amazon CloudWatch

- Monitoring and observability service
- Collects monitoring and operational data in the form of logs, metrics, and events
- Set alarms, visualize logs, take automated actions and troubleshoot issues
- Integrates with more than 70 AWS services:
	- Amazon EC2
	- Amazon DynamoDB
	- Amazon S3
	- Amazon ECS
	- AWS Lambda
	- and ....