---
layout:     post
title:      Managing Multiple AWS Accounts - Organizations, Trusted Advisor and more - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Managing Multiple AWS Accounts - Organizations, Trusted Advisor and more. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-managing-aws-accounts-organizations
---

Let's get a quick overview of Managing Multiple AWS Accounts - Organizations, Trusted Advisor and more.

## You will learn
- How can you manage multiple AWS accounts together?
- How can you use AWS Organizations, Trusted Advisor and more?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## AWS Organizations 
![](/images/aws/00-icons/organizations.png) 
- Organizations typically have multiple AWS accounts 
	- Different business units 
	- Different environments
- How do you centralize your management (billing, access control, compliance and security) across multiple AWS accounts? 
- Welcome AWS Organizations!
- Organize accounts into Organizational Units (OU)
- Provides API to automate creation of new accounts

## AWS Organizations - Features
- One consolidated bill for all AWS accounts
- Centralized compliance management for AWS Config Rules
- Send AWS CloudTrail data to one S3 bucket (across accounts)
- AWS Firewall Manager to manage firewall rules (across accounts)
	- AWS WAF, AWS Shield Advanced protections and Security Groups
- Use Service control policies (SCPs) to define restrictions for actions (across accounts):
	- Prevent users from disabling AWS Config or changing its rules
	- Require Amazon EC2 instances to use a specific type
	- Require MFA to stop an Amazon EC2 instance
	- Require a tag upon resource creation

## AWS Resource Access Manager
- Share AWS resources with any AWS account or within your AWS Organization
	- AWS Transit Gateways
	- Subnets
	- AWS License Manager configurations 
	- Amazon Route 53 Resolver rules
- Reduce Operational Overhead
- Optimize Costs

## AWS Trusted Advisor

![](/images/aws/00-icons/trustedadvisor.png) 
- Recommendations for cost optimization, performance, security and fault tolerance
	- Red - Action recommended Yellow - investigate and Green - Good to go
- All AWS customers get 4 checks for free:
	- Service limits (usage > 80%)
	- Security groups having unrestricted access (0.0.0.0/0)
	- Proper use of IAM
	- MFA on Root Account
- Business or Enterprise AWS support plan provides over 50 checks
	- Disable those you are not interested in
	- How much will you save by using Reserved Instances?
	- How does your resource utilization look like? Are you right sized?

## AWS Trusted Advisor Recommendations

![](/images/aws/00-icons/trustedadvisor.png) 

- Cost Optimization
	- Highlight unused resources 
	- Opportunities to reduce your costs
- Security 
	- Settings that can make your AWS solution more secure
- Fault Tolerance 
	- Increase resiliency of your AWS solution 
	- Redundancy improvements, over-utilized resources
- Performance 
	- Improve speed and responsiveness of your AWS solutions
- Service Limits 
	- Identify if your service usage is more than 80% of service limits

## AWS Service Quotas
- AWS account has Region-specific default quotas or limits for each service
	- You don't need to remember all of them :)
- Service Quotas allows you to manage your quotas for over 100 AWS services, from one location

## AWS Directory Service

![](/images/aws/00-icons/directoryservice.png) 
- Provide AWS access to on-premise users without IAM users
- Managed service deployed across multiple AZs
- Option 1 : AWS Directory Service for Microsoft AD
	- More than 5000 Users
	- Trust relationship needed between AWS and on-premise directory
- Option 2 : Simple AD
	- Less than 5000 users
	- Powered by Samba4 and compatible with Microsoft AD
	- Does not support trust relationships with other AD domains
- Option 3 : AD Connector
	- Use your existing on-premise directory with AWS cloud services
	- Your users use existing credentials to access AWS resources

## AWS Workspaces
- Desktop-as-a-Service (DaaS)
- Provision Windows or Linux desktops in minutes
- Eliminate traditional desktop management - Virtual Desktop Infrastructure (VDI)

