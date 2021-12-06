---
layout:     post
title:      Encryption in Google Cloud with Cloud KMS - GCP Certification Cheat Sheet
date:       2021-12-06 11:13:00
summary:    Let's get a quick overview of Encryption in Google Cloud with Cloud KMS from an GCP certification perspective. We will look at important certification questions regarding Encryption in Google Cloud with Cloud KMS.
categories:  GCP_General
permalink:  /encryption-in-google-cloud-with-KMS
---

Let's get a quick overview of Encryption in Google Cloud with Cloud KMS from an GCP certification perspective. We will look at important certification questions regarding Encryption in Google Cloud with Cloud KMS.

## You will learn
- What is Data States?
- What is Encryption?
- Why do we need Encryption?
- What is Symmetric Key Encryption?
- What is Asymmetric Key Encryption?
- What is Cloud KMS?
- Advantages of Cloud KMS?


## Data States
   ![compute-instance-card](https://user-images.githubusercontent.com/57451228/144869368-dd3cb711-7861-4acd-8467-922bb9e36d36.png)![arrow-card](https://user-images.githubusercontent.com/57451228/144869384-d3e48e9d-72be-4e07-bbc5-2a7fabaa07fe.png)![persistent-disks-card](https://user-images.githubusercontent.com/57451228/144869399-a7efe4ff-4347-4195-9b47-51d9de400d69.png)


 
    
- **Data at rest**: Stored on a device or a backup
Examples : data on a hard disk, in a database, backups and archives
- **Data in motion:** Being transferred across a network
  - Also called **Data in transit**
  - **Examples :**
      - Data copied from on-premise to cloud storage
      - An application talking to a database
  - **Two Types:**
      - In and out of cloud (from internet)
      - Within cloud
- **Data in use:** Active data processed in a non-persistent state
   - Example: Data in your RAM

## Encryption
 ![compute-instance-card](https://user-images.githubusercontent.com/57451228/144869368-dd3cb711-7861-4acd-8467-922bb9e36d36.png)![arrow-card](https://user-images.githubusercontent.com/57451228/144869384-d3e48e9d-72be-4e07-bbc5-2a7fabaa07fe.png)![persistent-disks-card](https://user-images.githubusercontent.com/57451228/144869399-a7efe4ff-4347-4195-9b47-51d9de400d69.png)
 
- If you store data as is, what would happen if an **unauthorized entity gets access to it?**
  - Imagine losing an unencrypted hard disk
- **First law of security :** Defense in Depth
- Typically, enterprises encrypt all data
  - Data on your hard disks
  - Data in your databases
  - Data on your file servers
- Is it sufficient if you encrypt data at rest?
  - **No. Encrypt data in transit - **between application to database as well.


<BR/>


<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
