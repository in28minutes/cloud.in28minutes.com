---
layout:     post
title:      Cross Account Access and Federation - IAM - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Cross Account Access and Federation from an AWS certification perspective. We will look at important certification questions regarding Cross Account Access and Federation. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-iam-cross-account-access-and-federation
---

Let's get a quick overview of Cross Account Access and Federation from an AWS certification perspective. We will look at important certification questions regarding Cross Account Access and Federation.

## You will learn
- What is Cross Account Access?
- What is Federation?
- Why do we need Cross Account Access and Federation?
- How is Corporate Directory Federation different from Web Identity Federation?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## IAM Role Use case : Cross Account Access

![](/images/aws-cloud.png)
![](/images/arrow.png) 
![](/images/aws-cloud.png)

- PROD Account (111111111111)
	- Create IAM role (ProdS3AccessRole) with right permissions and establish trust relationship with AWS account 222222222222
- DEV Account (222222222222)
	- Grant users (Operations Group) permissions to assume the ProdS3AccessRole in PROD Account 
		- Create a customer managed policy ProdS3AccessPolicy allowing access to call STS AssumeRole API for ProdS3AccessRole(arn:aws:iam::111111111111:role/ProdS3AccessRole)
		- Assign the policy to users (Operations Group)
		- (Optional) Enable MFA for assuming the role
- Operations user requests access to the role
	- Background: Call is made to AWS Security Token Service (AWS STS) AssumeRole API for the ProdS3AccessRole role
	- Gets access!

## IAM  - Corporate Directory Federation
![](/images/aws/iam2.png)

- Users authenticated with **a corporate directory**
	- For SAML2.0 compliant identity systems, establish a trust relationship with IAM
	- For enterprise using Microsoft AD (Active Directory), use AWS Directory Service to establish trust
	- Otherwise, set up a custom proxy server to translate user identities from enterprise to IAM roles

## IAM  - Web Identity Federation

- Authenticate users using **web identities** - mobile or web apps
- Example: Open ID (Facebook, Google, etc)
- **Amazon Cognito** supports login with Facebook, Google, or other OpenID Connect compatible IdP
- Configure Role to use Web Identity as trusted entity 
	- Authentication tokens exchanged using **STS AssumeRoleWithWebIdentity** API
