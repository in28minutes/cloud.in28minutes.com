---
layout:     post
title:      Server Side vs Client Side Encryption - KMS-S3 - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Server Side vs Client Side Encryption for Amazon S3 using KMS. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-server-side-vs-client-side-encryption-kms-s3
---

Let's get a quick overview of Server Side vs Client Side Encryption for Amazon S3 using KMS. 

## You will learn
- What is Server Side Encryption?
- What is Client Side Encryption?
- How can you implement Encryption for S3 using KMS?
- When do we use Server Side vs Client Side Encryption?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## KMS and Cloud HSM

![](/images/aws/00-icons/kms.png)
![](/images/aws/00-icons/cloudhsm.png) 

- How do you generate, store, use and replace your keys?
- AWS provides two important services - **KMS** and **Cloud HSM**
	- Manage your keys
	- Perform encryption and decryption

## AWS KMS

![](/images/aws/00-icons/kms.png)

- Create and manage **cryptographic keys** (symmetric and asymmetric)
- **Control their use** in your applications and AWS Services
- Define key usage permissions (including **cross account** access)
- Track key usage in AWS CloudTrail (regulations & compliance)
- **Integrates with almost all AWS services** that need data encryption
- **Automatically rotate master keys** once a year 
	- No need to re-encrypt previously encrypted data (versions of master key are maintained)
- **Schedule key deletion** to verify if the key is used
	- Mandatory minimum wait period of 7 days (max-30 days)

## Server Side Encryption
 
![](/images/aws/01-S3/3-server-side-encryption.png)

- Client sends data (as is) to AWS service
- AWS service interacts with KMS to perform encryption on the server side
- Recommended to **use HTTPS endpoints** to ensure encryption of data in transit
	- All AWS services (including S3) provides HTTPS endpoints
	- Encryption is optional with S3 but highly recommended in flight and at rest

## Server Side Encryption - S3

![](/images/aws/00-icons/user.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/s3.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/kms.png)

- **SSE-S3**: 
	- AWS S3 manages its own keys
	- Keys are rotated every month
	- Request Header - *x-amz-server-side-encryption(AES256)*
- **SSE-KMS**: 
	- Customer manages keys in KMS
	- Request Headers - *x-amz-server-side-encryption(aws:kms)* and *x-amz-server-side-encryption-aws-kms-key-id(ARN for key in KMS)*
- **SSE-C**: 
	- Customer sends the key with every request
	- S3 performs encryption and decryption without storing the key
	- HTTPS is mandatory

## Client Side Encryption
 
![](/images/aws/01-S3/4-client-side-encryption.png)

- Client **manages encryption process** and sends encrypted data to AWS service
	- AWS will not be aware of master key or data key
- AWS service stores data as is
- For Amazon S3, you can use a client library (Amazon S3 Encryption Client)
