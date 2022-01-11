---
layout:     post
title:      Google Cloud Storage : Block and File Storage in Google Cloud Platform - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Block and File Storage in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Block and File Storage in Google Cloud Platform.
categories:  GCP_General GCP_Computing_Services
permalink:  /gogle-cloud-storage-block-and-file-storage-in-gcp
---

Let's get a quick overview of Block and File Storage in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Block and File Storage in Google Cloud Platform.


## You will learn

- Google Cloud Storage
- Block Storage
- File Storage


<BR/>

Welcome to this new section on storage. In this section, we will be looking at the different storage options that are present in Google Cloud. We would be talking about block storage, files storage, and object storage options in this section.


## Storage Types - Block Storage and File Storage

![01-storage-types](https://user-images.githubusercontent.com/57451228/148937327-4e2d88bb-2838-4a43-9fb7-f6fef594a4c4.png)


- What is the type of storage of your hard disk?
   - **Block Storage**
- You've created a file share to share a set of files with your colleagues in a enterprise. What type of storage are you using?
   - **File Storage**

### Block Storage

![02-storage-types-block](https://user-images.githubusercontent.com/57451228/148937445-b73be44a-1150-4b24-be25-fd97b0095735.png)


- Use case: Harddisks attached to your computers
- Typically, ONE Block Storage device can be connected to ONE virtual server
   - (EXCEPTIONS) You can attach read only block devices with multiple virtual servers and certain cloud providers are exploring multi-writer disks as well!
- HOWEVER, you can connect multiple different block storage devices to one virtual server
- Used as:
   - **Direct-attached storage (DAS)** - Similar to a hard disk
   - **Storage Area Network (SAN)** - High-speed network connecting a pool of storage devices
      - Used by Databases - Oracle and Microsoft SQL Server



### File Storage

![02-storage-types-file](https://user-images.githubusercontent.com/57451228/148937852-6e5f0f0e-af12-4274-8c7e-a674d53f6759.png)

- Use case:
  - Media workflows need huge shared storage for supporting processes like video editing
  - Enterprise users need a quick way to share files in a secure and organized way
  - These file shares are shared by several virtual servers


## GCP - Block Storage and File Storage
 
Let's now get specific to Google Cloud Platform.
And Let's learn What are the options that are present in Google Cloud Platform for block storage and File Storage?

![persistent-disk](https://user-images.githubusercontent.com/57451228/148938294-159a4f88-d59c-41ff-b305-7f5a9fd72cb3.png) ![filestore](https://user-images.githubusercontent.com/57451228/148938304-695c46db-6040-4882-9314-fcab8d82390c.png)


- **Block Storage:**
   - **Persistent Disks:** Network Block Storage
       - Zonal: Data replicated in one zone
       - Regional: Data replicated in multiple zone
   - **Local SSDs:** Local Block Storage
- **File Storage:**
   - **Filestore:** High performance file storage

## GCP - Block Storage

Let's dig deeper into block storage in this section.

- Two popular types of block storage can be attached to VM instances:
  - **Local SSDs**
  - **Persistent Disks**
- **Local SSDs** are physically attached to the host of the VM instance
  - Temporary data
  - Lifecycle tied to VM instance
- **Persistent Disks** are network storage
  - More durable
  - Lifecycle NOT tied to VM instance


### Local SSDs
- **Physically attached** to the host of VM instance:
  - Provide very high (IOPS) and very low latency
  - (BUT) **Ephemeral storage** - Temporary data (Data persists only until instance is running)
     - **Enable live migration** for data to survive maintenance events
  - Data automatically encrypted
     - HOWEVER, you CANNOT configure encryption keys!
  - Lifecycle tied to VM instance
  - ONLY some machine types support Local SSDs
  - Supports SCSI and NVMe interfaces
- Remember:
  - Choose NVMe-enabled and multi-queue SCSI images for best performance
  - Larger Local SSDs (more storage), More vCPUs (attached to VM) => Even Better Performance

### Local SSDs - Advantages and Disadvantages
- **Advantages**
  - Very Fast I/O (~ 10-100X compared to PDs)
     - Higher throughput and lower latency
  - Ideal for use cases needing high IOPs while storing **temporary information**
     - Examples: Caches, temporary data, scratch files etc
- **Disadvantages**
  - **Ephemeral storage**
     - Lower durability, lower availability, lower flexibility compared to PDs
  - You **CANNOT detach and attach** it to another VM instance




### Storage - Scenarios - Persistent Disks - QNA

- Q1) You want to improve performance of Persistent Disks (PD)
   - Sol > Increase size of PD or Add more PDs. Increase vCPUs in your VM.
- Q2) You want to increase durability of Persistent Disks (PD)
   - Sol > Go for Regional PDs (2X cost but replicated in 2 zones)
- Q3) You want to take hourly backup of Persistent Disks (PD) for disaster recovery
   - Sol > Schedule hourly snapshots!
- Q4) You want to delete old snapshots created by scheduled snapshots
   - Sol > Configure it as part of your snapshot scheduling!


## Cloud Filestore

![02-storage-types-file](https://user-images.githubusercontent.com/57451228/148940572-ae6e1c72-361d-491a-810d-e396fab82a46.png)

- **Shared cloud file storage:**
  - Supports NFSv3 protocol
  - Provisioned Capacity
- Suitable for **high performance** workloads:
  - Up to 320 TB with throughput of 16 GB/s and 480K IOPS
- Supports HDD (general purpose) and SSD (performance-critical workloads)
- **Use cases :** file share, media workflows and content management


## Review - Global, Regional and Zonal Resources

In the last few steps, we actually discussed about a number of resources and we talked about some of them are global resources, regional resources, and zonal resources.
Let's quickly review some of them.

- **Global**
  - Images
  - Snapshots
  - Instance templates (Unless you use zonal resources in your templates)
- **Regional**
  - Regional managed instance groups
  - Regional persistent disks
- **Zonal**
  - Zonal managed instance groups
  - Instances
  - Persistent disks
     - You can attach a disk only to instances in the same zone as the disk


### Storage - Scenarios QNA

- Q1) You want Very High IOPS but your data can be lost without a problem
   - Sol > Local SSDs
- Q2) You want to create a high perfomance file sharing system in GCP which can be attached with multiple VMs
   - Sol > Filestore
- Q3) You want to backup your VM configuration along with all its attached Persistent Disks
   - Sol > Create a Machine Image
- Q4) You want to make it easy to launch VMs with hardened OS and customized software
   - Sol > Create a Custom Image
   

<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
