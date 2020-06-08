---
layout:     post
title:      IAM Policies - AWS Managed vs Customer Managed vs Resource Based vs Identity Based  - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of IAM Policies - AWS Managed vs Customer Managed vs Resource Based vs Identity Based. We will look at important certification questions regarding IAM Policies. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-iam-policies
---

Let's get a quick overview of IAM Policies - AWS Managed vs Customer Managed vs Resource Based vs Identity Based. We will look at important certification questions regarding IAM Policies.

## You will learn
- What is IAM Policies?
- What are different types of IAM Policies - AWS Managed vs Customer Managed vs Resource Based vs Identity Based ?
- Why do we need IAM Policies?
- Comparison of AWS Managed IAM Policies vs Customer Managed IAM Policies
- Comparison of Resource Based Policies vs Identity Based IAM Policies
- What are Bucket ACLs and Object ACLs?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}



## IAM Policies

![](/images/aws/iam-overview.png) 
- **Policies**: Define permissions 
	- **AWS managed policies** - Standalone policy predefined by AWS
	- **Customer managed policies** - Standalone policy created by you
	- **Inline policies** - Directly embedded into a user, group or role


## AWS IAM Policies - Authorization

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```
- Policy is a JSON document with one or more permissions
	- Effect - Allow or Deny
	- Resource - Which resource are you providing access to?
	- Action - What actions are allowed on the resource?
	- Condition - Are there any restrictions on IP address ranges or time intervals?
- Example above: AWS Managed Policy : AdministratorAccess



## AWS Managed Policy : AmazonS3ReadOnlyAccess
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*"
            ],
            "Resource": "*"
        }
    ]
}
```

## Customer Managed Policy : ReadSpecificS3Bucket

```
{ 
  "Version":"2012-10-17", 
  "Statement":[ 
   { 
     "Effect":"Allow", 
     "Action":[ 
       "s3:Get*", 
       "s3:List*" 
     ],
 
     "Resource":"arn:aws:s3:::mybucket/somefolder/*" 
    } 
  ] 
}
```




## Identity-based and Resource-based policies
![](/images/aws/01-S3/2-S3-AccessPolicies.png)
- By default only account owner has access to a S3 bucket
- Access policies enable other users to access S3 buckets and objects:
    - **Identity-based policies** : Attached to an IAM user, group, or role
    - **Resource-based policies and ACLs** : Attached to a resource - S3 buckets, Amazon SQS queues, and AWS KMS keys  

## Identity-based and Resource-based policies
 
| Policy Type |Identity-based  | Resource-based | 
|--|:--|:--|
| Attached with   |  IAM user, group, or role     | A resource       | 
| Type   |  Managed and Inline     | Inline only       |
|Focus|What resource? What actions?|Who? What actions?| 
|Example|Can list S3 buckets with name **XYZ**|Account A can read and modify. <BR/>Public can read.|
|Cross-account access| User should switch role|Simpler. User accesses resource directly from his AWS account|
|Supported by|All services|Subset of services - S3, SQS, SNS, KMS etc|
|Policy Conditions|When (dates),  Where(CIDR blocks), Enforcing MFA|When (dates),  Where(CIDR blocks), Is SSL Mandatory?|

## Identity-based Policy Example

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```
- Policy is a JSON document with one or more permissions
    - Effect - Allow or Deny
    - Resource - Which resource are you providing access to?
    - Action - What actions are allowed on the resource?
    - Condition - Are there any restrictions on IP address ranges or time intervals?
- Example above: AWS Managed Policy : AdministratorAccess

## Resource-based policies - Bucket policies
```
{
    "Version":"2012-10-17",
    "Statement":[
    {
        "Sid":"PublicRead",
        "Effect":"Allow",
        "Principal": "*",
        "Action":["s3:GetObject"],
        "Resource":["arn:aws:s3:::mybucket/*"]
    }
    ]
}
```

- Control access to your bucket and objects
- Can grant **cross account** and **public** access

## Bucket ACLs and Object ACLs 
- **Bucket/Object ACLs**
    - Access for bucket/object owner
    - Access for other AWS accounts
    - Public access
- Use **object ACLs (object level access)**
    - When bucket owner is not the object owner
    - When you need different permissions for different objects in the same bucket
- (Remember) Bucket/Object ACLs
    - **CANNOT** have conditions while policies can have conditions
    - **CANNOT** explicitly DENY access
    - **CANNOT** grant permissions to other individual users
- (Remember) ACLs are **primarily** used to grant permissions to public or other AWS accounts
