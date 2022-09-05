---
layout:     post
title:      Encryption - Symmetric Key vs Asymmetric Key - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Encryption - Symmetric Key vs Asymmetric Key.
categories:  AWS_CLOUD General
permalink:  /aws-certification-encryption-symmetric-key-vs-asymmetric-key
---

Let's get a quick overview of Encryption - Symmetric Key vs Asymmetric Key.

## You will learn
- What is Encryption? 
- Why do we need Encryption?
- When do we use Encryption - Symmetric Key vs Asymmetric Key?
- How is Symmetric Key Encryption different from Asymmetric Key Encryption?
- What are different Data States?



## Data States

![](/images/aws/00-icons/ec2instance.png) 
![](/images/arrow.png) 
![](/images/aws/00-icons/database.png) 

- **Data at rest**: Stored on a device or a backup 
	- Examples : data on a hard disk, in a database, backups and archives
- **Data in motion**: Being transferred across a network
	- Also called **Data in transit**
	- **Examples** : 
		- Data copied from on-premise to cloud storage
		- An application in a VPC talking to a database
	- **Two Types**:
		- In and out of AWS
		- Within AWS
- **Data in use**: Active data processed in a non-persistent state
	- Example: Data in your RAM

## Encryption
- If you store data as is, what would happen if an **unauthorized entity gets access** to it?
	- Imagine losing an unencrypted hard disk
- **First law of security** : Defense in Depth
- Typically, enterprises encrypt all data 
	- Data on your hard disks
	- Data in your databases
	- Data on your file servers
- Is it sufficient if you encrypt data at rest? 
	- **No**. **Encrypt data in transit** - between  application to database as well.

## Symmetric Key Encryption

![](/images/aws/iam/symetrickey.png)

- Symmetric encryption algorithms use the **same key for encryption and decryption**
- Key Factor 1: Choose the **right encryption algorithm**
- Key Factor 2: How do we **secure the encryption key**?
- Key Factor 3: How do we **share the encryption key**?

## Asymmetric Key Encryption

- **Two Keys** : Public Key and Private Key
- Also called **Public Key Cyptography**
- Encrypt data with Public Key and decrypt with Private Key
- Share Public Key with everybody and keep the Private Key with you(YEAH, ITS PRIVATE!)
- No crazy questions:
	- Will somebody not figure out private key using the public key?
- How do you create Asymmetric Keys?
