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
  - **No. Encrypt data in transit -** between application to database as well.
   
### Symmetric Key Encryption
![symetrickey](https://user-images.githubusercontent.com/57451228/144870527-fbf574e6-8718-44d9-a87d-1c9821900fe0.png)

- Symmetric encryption algorithms use the **same key for encryption and decryption**
- Key Factor 1: Choose the **right encryption algorithm**
- Key Factor 2: How do we **secure the encryption key?**
- Key Factor 3: How do we **share the encryption key?**

### Asymmetric Key Encryption
![Asymmetric_encryption](https://user-images.githubusercontent.com/57451228/144870702-777536a0-ae97-44e5-a56e-850d12afe5f3.png)

- **Two Keys :** Public Key and Private Key
Also called Public Key Cyptography
Encrypt data with Public Key and decrypt with Private Key
Share Public Key with everybody and keep the Private Key with you(YEAH, ITS PRIVATE!)
- No crazy questions:
  - Will somebody not figure out private key using the public key?
- **How do you create Asymmetric Keys?**

## Cloud KMS

![kms](https://user-images.githubusercontent.com/57451228/144871178-e94ef009-0a9e-4e1c-9df3-e45e32add0f2.png)

- Create and manage **cryptographic keys** (symmetric and asymmetric)
Control their use in your applications and GCP Services
Provides an API to encrypt, decrypt, or sign data
Use existing cryptographic keys created on premises
- **Integrates with almost all GCP services** that need data encryption:
  - Google-managed key: No configuration required
  - Customer-managed key: Use key from KMS
  - Customer-supplied key: Provide your own key

### Cloud KMS - Images
<BR/>

![Screenshot 2021-12-06 at 8 45 45 PM](https://user-images.githubusercontent.com/57451228/144871603-e0bcf284-5a09-4ccf-ab1d-b90ea9e55c3c.png)

![Screenshot 2021-12-06 at 8 46 18 PM](https://user-images.githubusercontent.com/57451228/144871670-0ff3fe04-d826-41ba-b9b4-717b33554a36.png)

![Screenshot 2021-12-06 at 8 46 49 PM](https://user-images.githubusercontent.com/57451228/144871776-9970d4f8-153b-475c-bc0f-b16d1d2934bf.png)



<BR/>


<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
