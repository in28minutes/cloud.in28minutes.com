---
layout:     post
title:      Google Cloud Storage : Block and File Storage in Google Cloud Platform - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Block and File Storage in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Block and File Storage in Google Cloud Platform.
categories:  GCP_General GCP_Storage_Services
permalink:  /gogle-cloud-storage-block-and-file-storage-in-gcp
---

Let's get a quick overview of Block and File Storage in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Block and File Storage in Google Cloud Platform.


## You will learn

- Google Cloud Storage
- Storage Types - Block Storage and File Storage
- Block Storage & File Storage
- GCP - Block Storage and File Storage
- Local SSDs - Advantages and Disadvantages
- Persistent Disks (PD)
- Persistent Disks vs Local SSDs
- Persistent Disks - Standard vs Balanced vs SSD
- Persistent Disks - Snapshots - Recommendations
- Playing with Machine Images
- Playing with Disks & Images & Machine Images - Command Line
- Global, Regional and Zonal Resources
- Google Cloud Storage - QNA


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




### Persistent Disks (PD)
 
 In this step, let's look at persistent disks. Persistent disks are network block storage that is attached to your VM instance. 

 ![compute-instance-card](https://user-images.githubusercontent.com/57451228/148962360-aa09f528-c2e7-448c-bf49-270b8aefde82.png)
 
&emsp; &emsp; &emsp; &emsp;  ![arrowtd](https://user-images.githubusercontent.com/57451228/148962379-bf2db923-33ef-4332-95ea-5e119d629428.png)

![persistent-disks-card](https://user-images.githubusercontent.com/57451228/148962390-8693199d-0797-40e9-929b-ff60a08d2c98.png)



- **Network block storage** attached to your VM instance
- **Provisioned capacity**
- Very Flexible:
  - **Increase size when you need it** - when attached to VM instance
  - Performance scales with size
     - For higher performance, resize or add more PDs
- **Independent lifecycle **from VM instance
  - Attach/Detach from one VM instance to another
- Options: Regional and Zonal
  - Zonal PDs replicated in single zone. Regional PDs replicated in 2 zones in same Region.
  - Typically Regional PDs are 2X the cost of Zonal PDs
- **Use case :** Run your custom database


## Persistent Disks vs Local SSDs

| Feature | Persistent Disks  | Local SSDs | 
|:--:|--|:--:|
| Attachment to VM instance   |  As a network drive  | Physically attached        | 
|  Lifecycle   |   Separate from VM instance     |   Tied with VM instance     |  
|I/O Speed|Lower (network latency)|10-100X of PDs|
|Snapshots	|Supported	|Not Supported|
|Use case	|Permanent storage	|Ephemeral storage|

## Persistent Disks - Standard vs Balanced vs SSD
|Feature	|Standard	|Balanced	|SSD|
|:--:|--|:--:|--|
|Underlying Storage|	Hard Disk Drive|	Solid State Drive	|Solid State Drive|
|Referred to as|	pd-standard|	pd-balanced	|pd-ssd|
|Performance - Sequential IOPS (Big Data/Batch)|	Good	|Good	|Very Good|
|Performance - Random IOPS (Transactional Apps)	|Bad	|Good	|Very Good|
|Cost|	Cheapest	|In Between	|Expensive|
|Use cases	|Big Data (cost efficient)	|Balance between cost and performance	|High Performance|

## Persistent Disks - Snapshots

![persistent-disk-card](https://user-images.githubusercontent.com/57451228/148964689-b717294b-242e-4b8f-9c09-d1f480e9ad2b.png)

&emsp; &emsp; &emsp; &emsp;  ![arrowtd](https://user-images.githubusercontent.com/57451228/148964700-c332343d-23bd-40ac-afa2-dd4edeb0a32d.png)
  
  
![snapshots-card](https://user-images.githubusercontent.com/57451228/148964708-19700cbd-e199-45a0-a28b-92afc9971c70.png)

  
  
- Take **point-in-time snapshots** of your Persistent Disks
- You can also schedule snapshots (configure a schedule):
  - You can also auto-delete snapshots after X days
- Snapshots can be Multi-regional and Regional
- You can share snapshots across projects
- You can create new disks and instances from snapshots
- Snapshots are **incremental**:
  - Deleting a snapshot **only deletes data which is NOT needed** by other snapshots
- Keep similar data together on a Persistent Disk:
  - Separate your operating system, volatile data and permanent data
  - Attach multiple disks if needed
  - This helps to better organize your snapshots and images

### Persistent Disks - Snapshots - Recommendations
  
- **Avoid** taking snapshots more often than once an hour
- Disk volume is available for use **but Snapshots reduce performance**
  - (RECOMMENDED) Schedule snapshots during off-peak hours
- Creating snapshots from disk is faster than creating from images:
  - But creating disks from image is faster than creating from snapshots
  - (RECOMMENDED) If you are repeatedly creating disks from a snapshot:
     - Create an image from snapshot and use the image to create disks
- Snapshots are **incremental:**
  - BUT you don't lose data by deleting older snapshots
  - Deleting a snapshot **only deletes data which is NOT needed** by other snapshots
  - (RECOMMENDED) Do not hesitate to delete unnecessary snapshots

## Playing with Machine Images
![persistent-disks-card](https://user-images.githubusercontent.com/57451228/148965384-e9fae65f-ac31-4a6d-9dd8-96f83e37f9bc.png)

![compute-instance-card](https://user-images.githubusercontent.com/57451228/148965394-cb77114e-ad9b-4577-aefb-10154761651c.png)


&emsp; &emsp; &emsp; &emsp;  ![arrowtdsmall](https://user-images.githubusercontent.com/57451228/148965402-92fbaf37-0e7b-4f0b-aaa6-a4842d852a58.png)

![machine-image-card](https://user-images.githubusercontent.com/57451228/148965414-296f61a0-153b-4f99-9427-5e1b9e6e1c2d.png)

&emsp; &emsp; &emsp; &emsp;  ![arrowtdsmall-1](https://user-images.githubusercontent.com/57451228/148965428-db814c6c-1f8b-4a15-a62b-2a79be2f1e32.png)

![compute-instance-card-1](https://user-images.githubusercontent.com/57451228/148965459-f64096ef-85d1-4ccf-9348-049f7cf0db72.png)


![persistent-disks-card-1](https://user-images.githubusercontent.com/57451228/148965471-fc17fe28-d5f2-4e97-8f34-ea321be7ac35.png)


- (Remember) **Machine Image** is different from Image
- **Multiple disks can be attached** with a VM:
  - One Boot Disk (Your OS runs from Boot Disk)
  - Multiple Data Disks
- An image is created from the boot Persistent Disk
- HOWEVER, a Machine Image is created from a VM instance:
  - Machine Image **contains everything you need** to create a VM instance:
     - Configuration
     - Metadata
     - Permissions
     - Data from one or more disks
- **Recommended for** disk backups, instance cloning and replication

## Let's Compare


![comparison-image-snapshot-etc](https://user-images.githubusercontent.com/57451228/148965562-41d9dcdb-a29c-4904-9450-70937bae9d48.png)


Ref : https://cloud.google.com/compute/docs/machine-images


## Playing with Disks - Command Line
  
**gcloud compute disks list/create/delete/resize/snapshot**
  - gcloud compute disks **create** my-disk-1 --zone=us-east1-a
    - What should be the size and type?
      - --size=SIZE (1GB or 2TB)
      - --type=TYPE (default - pd-standard) (gcloud compute disk-types list)
    - What should be on the disk?
      - --image --image-family --source-disk --source-snapshot
    - How should data on disk be encrypted?
      - --kms-key --kms-project
  - gcloud compute disks **resize** example-disk-1 --size=6TB
    - Only increasing disk size is supported
  - gcloud compute disks **snapshot** test --zone=us-central1-a --snapshot-names=snapshot-test
    - You can also play with the snapshots which are created:
      - gcloud compute snapshots list/describe/delete


## Playing with Images - Command Line
  
**gcloud compute images**
Actions: **create/delete/deprecate/describe/export/import/list/update**
  - Creating Images
    - gcloud compute images **create** my-image
      - From a Disk - --source-disk=my-disk --source-disk-zone=us-east1-a
      - From a Snapshot - --source-snapshot=source-snapshot
      - From another image - --source-image=source-image --source-image-project=source-image-project
      - From latest non deprecated image from a family - --source-image-family=source-image-family --source-image-project=source-image-project
  - Deprecate Image
    - gcloud compute images **deprecate** IMAGE --state=DEPRECATED
  - Exports virtual disk images
    - gcloud compute images **export** --image=my-image --destination-uri=gs://my-bucket/my-image.vmdk --export-format=vmdk --project=my-project
  - Other Examples:
    - gcloud compute images **delete** my-image1 my-image2
    - gcloud compute images **list** --format="value(NAME)"

## Playing with Machine Images - Command Line
      
(Remember) gcloud commands for machine images are IN BETA
Commands:
  - Create Machine Image:
    - gcloud beta compute machine-images create MACHINE_IMAGE_NAME --source-instance SOURCE_INSTANCE_NAME
  - Create an Instance from the Machine Image:
    - gcloud beta compute instances create VM_NAME --zone ZONE --source-machine-image SOURCE_MACHINE_IMAGE_NAME


## Storage - Scenarios - Persistent Disks - QNA

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


## Storage - Scenarios QNA

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
