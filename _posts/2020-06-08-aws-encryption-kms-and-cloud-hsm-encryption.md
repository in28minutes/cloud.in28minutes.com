---
layout:     post
title:      KMS and Cloud HSM - Encryption - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of KMS and Cloud HSM from an AWS certification perspective. We will look at important certification questions regarding KMS and Cloud HSM. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-kms-and-cloud-hsm-encryption
---

Let's get a quick overview of KMS and Cloud HSM from an AWS certification perspective. We will look at important certification questions regarding KMS and Cloud HSM.

## You will learn
- What is KMS?
- What is Cloud HSM?
- Why do we need KMS and Cloud HSM?
- How is KMS different from Cloud HSM?
- How do you manage keys with KMS and Cloud HSM?

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

## Server Side Encryption with KMS
- Create **Customer Master Key**. Map to AWS service (S3)
- **Steps**
	- Data sent to S3
	- S3 receives **data keys** from KMS
	- S3 encrypts data
	- Stores encrypted data & data key
- Remember
	- CMK never leaves KMS
	- **Encryption of data key** - **KMS** using CMK
	- **Encryption of data** - AWS Service - **Amazon S3** using data key

## Envelope Encryption

- The process KMS uses for encryption is called **Envelope Encryption**
	- Data is encrypted using **data key**
	- Data key is encrypted using Master key
	- Master key **never leaves KMS**
- KMS **encrypts small pieces of data** (usually data keys) less than 4 KB

## Decryption of data using KMS

![](/images/aws/00-icons/s3.png) 
![](/images/arrowbi.png) 
![](/images/aws/00-icons/kms.png)

- AWS service (Amazon S3) sends **encrypted data key** to KMS
- KMS uses Customer Master Key (CMK) to decrypt and return **plain-text data key**
- AWS service (Amazon S3) uses the plain-text data key to perform decryption
- (TIP) Remove plain-text data key from memory asap
- (TIP) AWS service needs IAM permissions to use the CMK
- Remember:
	- (Optional) You can associate a key/value map called **encryption context** with any cryptographic operation
	- (TIP) If encryption context is different, decryption will NOT succeed

## AWS CloudHSM

![](/images/aws/00-icons/cloudhsm.png)

- Managed (highly available & auto scaling) **dedicated** **single-tenant** Hardware Security Module(HSM) for regulatory compliance
	- (Remember) AWS KMS is a multi-tenant service
- FIPS 140-2 Level 3 compliant
- AWS **CANNOT access your encryption master keys** in CloudHSM
	- In KMS, AWS can access your master keys
	- Be ultra safe with your keys when you are using CloudHSM
	- **(Recommendation)** Use two or more HSMs in separate AZs in a production cluster

## AWS CloudHSM

![](/images/aws/00-icons/s3.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/kms.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/cloudhsm.png)

- AWS KMS can use CloudHSM cluster as **"custom key store"** to store the keys:
	- AWS Services can continue to talk to KMS for data encryption
	- (AND) KMS does the necessary integration with CloudHSM cluster
- (Best Practice) **CloudWatch** for monitoring and **CloudTrail** to track key usage
- **Use cases**
	- (Web servers) Offload SSL processing
	- Certificate Authority
	- Digital Rights Management
	- TDE for Oracle databases
