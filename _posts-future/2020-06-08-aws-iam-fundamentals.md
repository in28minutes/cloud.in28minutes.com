---
layout:     post
title:      IAM Fundamentals - Identity and Access Management - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of IAM Fundamentals from an AWS certification perspective. We will look at important certification questions regarding Identity and Access Management - IAM . 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-iam-fundamentals-identity-and-access-management
---

Let's get a quick overview of IAM Fundamentals from an AWS certification perspective. We will look at important certification questions regarding IAM Fundamentals.

## You will learn
- What is Identity and Access Management - IAM ?
- How do you manage authentication and authorization using IAM?
- What are IAM users, IAM groups, Roles and Policies?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Typical identity management in the cloud

![](/images/aws/iam.png)
- You have **resources** in the cloud (examples - a virtual server, a database etc)
- You have **identities (human and non-human)** that need to access those resources and perform actions 
	- For example: launch (stop, start or terminate) a virtual server
- How do you **identify users** in the cloud?
- How do you configure resources they can access? 
- How can you configure what actions to allow?
- In AWS, *Identity and Access Management (IAM)* provides this service

## AWS Identity and Access Management (IAM)

![](/images/aws/iam.png)
- **Authentication** (is it the right user?) and 
- **Authorization** (do they have the right access?) 
- **Identities** can be 
	- AWS users or 
	- Federated users (externally authenticated users)
- Provides very **granular** control
	- Limit a single user:
		- to perform single action
		- on a specific AWS resource
		- from a specific IP address
		- during a specific time window

## Important IAM Concepts

![](/images/aws/iam-overview.png) 
- **IAM users**: Users created in an AWS account
	- Has credentials attached (name/password or access keys)
- **IAM groups**: Collection of IAM users
- **Roles**: Temporary identities
	- Does NOT have credentials attached
	- (Advantage) Expire after a set period of time
- **Policies**: Define permissions 
	- **AWS managed policies** - Standalone policy predefined by AWS
	- **Customer managed policies** - Standalone policy created by you
	- **Inline policies** - Directly embedded into a user, group or role

## IAM Scenario Questions
|Scenario|Solution|
|--|:--|
|How to rotate access keys <BR/>without causing problems| Create new access key <BR/> Use new access key in all apps <BR/> Disable original access key <BR/> Test and verify <BR/> Delete original access key|
|How are multiple permissions resolved in IAM Policy| If there is an explicit deny - return deny <BR/> If there is no explicit deny and there is an explicit allow - allow<BR/> If there is no explicit allow or deny - deny|
|Which region are IAM users created in | IAM Users are **global entities**. <BR/>Can use AWS services in any geographic region|
|What is the difference between <BR/>IAM user, Federated user and Web identity federation user|**IAM users** - created and maintained in your AWS account <BR/> **Federated users** - managed outside of AWS - corporate directory <BR/> **Web identity federation users** - Amazon Cognito, Amazon, Google, or any OpenID Connect-compatible provider Accounts |

## Authentication with IAM  - Remember
- IAM Users identities exist until they are **explicitly deleted**
- IAM allows you to create **a password policy**
	- What characters should your password contain?
	- When does a password expire? 
- Access key's should be **constantly rotated**
- Two access keys can be **active simultaneously**. Makes rotation of keys easier.
- An IAM role can be added to already running EC2 instances. **Immediately effective**.
- An IAM role is **NOT** associated with an IAM user. 
- Am IAM user can assume an IAM role temporarily.

## Authentication with IAM  - Remember
- An IAM role is **NOT associated** with long-term credentials 
	- When a user, a resource (For example, an EC2 instance) or an application assumes a Role, it is provided with temporary credentials
- **Do NOT** use AWS IAM root user for regular everyday tasks. Lock it away after creating an admin IAM user. 
- Enable **Multi Factor Authentication** for all important IAM operations
	- Extra layer of security
	- MFA Devices 
		- Hardware device - Gemalto
		- Virtual device - An app on a smart phone


## IAM Certification and Interview Questions

| Scenario | User/Role  | Recommendation|
|--|--|:--|
| You're the only one in your account | IAM user      | Do not use ROOT user|
| Your team needs access to your AWS account and there is no other identity mechanism   |  IAM users |Use IAM Groups to manage policies |
|EC2 instance talks with Amazon S3 or a database|IAM role|&nbsp;|
|Cross Account Access|IAM role|&nbsp;|

## Instance Profile

![](/images/aws/00-icons/ec2instance.png)
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png) 

- A Container (A Box) for an IAM role
- Used to pass role information to an EC2 instance
- AWS Management Console:
	- An instance profile is automatically created when you create a role for EC2 instance
- From CLI or API
	- Explicitly manage Instance Profiles - CreateInstanceProfile etc
- (REMEMBER) Instance profile is a simple container for IAM Role

## IAM Role Use case 1 : EC2 talking with S3
![](/images/aws/00-icons/ec2instance.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/s3.png) 
- Create IAM role with access to S3 bucket
- Assign IAM role to EC2 instance
- No need to store credentials in config files
- No need for rotation of keys
