# Storage Fundamentals

## Storage Types - Block Storage and File Storage
![](/images/aws/001-basic-drawings/01-storage-types.png)
- What is the type of storage of your hard disk?
	- **Block Storage**
- You've created a file share to share a set of files with your colleagues in a enterprise. What type of storage are you using?
	- **File Storage**

## Block Storage

![](/images/aws/001-basic-drawings/02-storage-types-block.png)
- Use case: Harddisks attached to your computers
- Typically, ONE Block Storage device can be connected to ONE virtual server
- HOWEVER, you can connect multiple different block storage devices to one virtual server
- Used as:
	- **Direct-attached storage (DAS)** - Similar to a hard disk
	- **Storage Area Network (SAN)** - High-speed network connecting a pool of storage devices
		- Used by Databases - Oracle and Microsoft SQL Server

## File Storage	

![](/images/aws/001-basic-drawings/02-storage-types-file.png)
- Media workflows need huge shared storage for supporting processes like video editing
- Enterprise users need a quick way to share files in a secure and organized way
- These file shares are shared by several virtual servers

## AWS - Block Storage and File Storage
![](/images/aws/00-icons/efs.png)
![](/images/aws/00-icons/ebs.png) 
- **Block Storage**:
	- Amazon Elastic Block Store (EBS)
	- Instance store
- **File Storage**:
	- Amazon EFS (for Linux instances)
	- Amazon FSx Windows File Servers 
	- Amazon FSx for Lustre (high performance use cases)

## EC2 - Block Storage

![](/images/aws/001-basic-drawings/02-storage-types.png)
- Two popular types of block storage can be attached to EC2 instances:
	- **Elastic Block Store (EBS)**
	- **Instance Store** 
- **Instance Stores** are physically attached to the EC2 instance
	- Temporary data
	- Lifecycle tied to EC2 instance
- **Elastic Block Store (EBS)** is network storage
	- More durable
	- Lifecycle NOT tied to EC2 instance

## Instance Store

![](/images/aws/001-basic-drawings/03-storage-types.png)
- **Physically attached** to your EC2 instance
- **Ephemeral storage** 
	- Temporary data. 
	- Data is lost when hardware fails or an instance is terminated.
	- Use case: cache or scratch files
- **Lifecycle is tied** to EC2 instance
- Data is **NOT lost** on instance reboot
- Only some of the EC2 instance types support **Instance Store**

## Instance Store - Advantages and Disadvantages

![](/images/aws/001-basic-drawings/03-storage-types.png)

- **Advantages**
	- Very Fast I/O (2-100X of EBS)
	- (Cost Effective) **No extra cost**. Cost is included in the cost of EC2 instance
	- Ideal for storing **temporary information** - cache, scratch files etc
- **Disadvantages**
	- **Slow boot up** (up to 5 minutes)
	- **Ephemeral storage** (data is lost when hardware fails or instance is terminated)
	- **CANNOT take a snapshot** or restore from snapshot
	- Fixed size based on instance type
	- You cannot detach and attach it to another EC2 instance

## Amazon Elastic Block Store (EBS)

![](/images/aws/001-basic-drawings/04-ebs.png)
- **Network block storage** attached to your EC2 instance
- **Provisioned capacity**
- Very flexible. 
	- **Increase size when you need it** - when attached to EC2 instance
- Independent lifecycle from EC2 instance
	- Attach/Detach from one EC2 instance to another
- 10X more durable compared to an usual hard disk (annual failure rate of 0.1% - 0.2%)
- *99.999% Availability* & replicated within the same AZ
- **Use case** : Run your custom database

## Amazon EBS vs Instance Store
|Feature|Elastic Block Store (EBS)|Instance Store|
|--|:--|:--|
|Attachment to EC2 instance|As a network drive|Physically attached|
|Lifecycle|Separate from EC2 instance|Tied with EC2 instance|
|Cost| Depends on provisioned size|Zero (Included in EC2 instance cost)|
|Flexibility| Increase size| Fixed size|
|I/O Speed| Lower (network latency) | 2-100X of EBS|
|Snapshots| Supported | Not Supported|
|Use case| Permanent storage| Ephemeral storage|
|Boot up time| Low| High|

## Elastic Block Store - Hands-on

![](/images/aws/00-icons/ec2instance.png)
![](/images/arrow.png)
![](/images/aws/00-icons/volume.png)

- Create 3 EC2 instances
	- Instance A in AZ A - Root volume
	- Instance B in AZ A - Root volume and Secondary volume
	- Instance C in AZ B - Root volume

## Hard Disk Drive vs Solid State Drive

> Amazon EBS offers HDD and SSD options! <BR/>How do you choose between them?

|Feature|HDD(Hard Disk Drive)|SSD(Solid State Drive)|
|--|:--|:--|
|Performance - IOPS| Low | High|
|Throughput| High | High|
|Great at| Large sequential I/O operations |Small, Random I/O operations &<BR/> Sequential I/O|
|Recommended for| Large streaming or big data workloads| Transactional workloads|
|Cost| Low| Expensive|
|Boot Volumes|Not Recommended| Recommended|

## Amazon Elastic Block Store (EBS) SSD Types

##### General Purpose SSD (gp2) ($$$)
- I/O performance **increases with size** - 3 IOPS/GB (min 100) upto 16,000 IOPS
- **Balance price & performance** for transactional workloads (Cost sensitive)
- **Use cases** : small/medium databases, dev/test environments, & boot volumes
- **Burst** up to 3,000 IOPS above the baseline

##### Provisioned IOPS SSD (io1) ($$$$)
- Provision IOPS you need
- Designed for **low latency transactional** workloads
- Delivers consistent performance for **random and sequential** access
- **Use cases** : large relational or NoSQL databases

## Amazon Elastic Block Store (EBS) HDD Types

![](/images/aws/00-icons/ebs.png) 

##### Throughput Optimized HDD (st1) ($$)
- For **frequently accessed, throughput-intensive sequential** workloads
- **Use cases** : MapReduce, Kafka, log processing, data warehouse, and ETL

##### Cold HDD (sc1) ($)
- Lowest Cost
- **Use cases** : infrequent data access - very low transaction databases

## Amazon Elastic Block Store (EBS) Types
|                       | Provisioned IOPS SSD | General Purpose SSD | Throughput Optimized HDD | Cold HDD |
|--|:--|:--|:--|:--|
| Volume Size           | 4 GB - 16 TB         | 1 GB - 16 TB        | 500 GB - 16 TB           | 500 GB - 16 TB |
| Max IOPS/Volume       | 64,000               | 16,000              | 500                      | 250            |
| Max Throughput/Volume | 1,000 MB/s           | 250 MB/s            | 500 MB/s                 | 250 MB/s       |
| Boot Volume | ✓          | ✓           |         X        |   X     |

## Amazon Elastic Block Store (EBS)
![](/images/aws/00-icons/volume.png)
![](/images/arrow.png)
![](/images/aws/00-icons/snapshot.png)

- Supports **live changes to volumes** without service interruptions
	- Increase size
	- Change type 
	- Increase IOPS capacity
- Take **point-in-time snapshots** of EBS volumes (stored in Amazon S3)
	- **Asynchronous process** - reduces performance but EBS volume is available
	- Snapshots cannot be accessed directly from S3
	- Use EC2 APIs to restore them to EBS volumes

## Amazon EBS Snapshots
- Snapshots are **incremental**
	- BUT you don't lose data by deleting older snapshots
	- Deleting a snapshot **only deletes data which is NOT needed** by other snapshots
	- Do not hesitate to delete unnecessary snapshots
	- All information needed to restore the active snapshots will be retained
- **Can be shared** with other AWS accounts
	- To share an encrypted snapshot, you would need to share (give permissions) to encryption keys also
- Constrained to the **created region**
	- To use in other regions, copy it
- **Fast Snapshot Restore** speeds up the process of creating volumes from snapshots
	- **Eliminates need for pre-warming** volumes created from snapshots

## Amazon EBS Encryption
![](/images/aws/00-icons/ebs.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/kms.png)
- Encryption (AES-256) is done *transparently* using **master keys from KMS**
- Turning on Encryption **automatically encrypts**:
	- **Data at rest**
		- Data volumes, boot volumes 
		- Snapshots
	- **Data in transit**
		- Between EC2 instances and EBS volume
		- Between EBS volume and EBS snapshots

## Faster I/O performance between EC2 and EBS

![](/images/aws/00-icons/ec2.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ebs.png)

 
| Option | Description  | 
|--|:--|
| Launch EC2 instances as **EBS optimized Instances**| Available on select instances <BR/> Default and free for a few instance types <BR/> Hourly fee for other instance types|
|**Enhanced networking** through Elastic Network Adapter (ENA)|Increases throughput(PPS) <BR/>Needs custom configuration|
|Use **Elastic Fabric Adapter (EFA)**|Available on select instances <BR/>NOT available on Windows EC2 instances<BR/> EFA = ENA + OS-bypass<BR/>**Ideal for** High Performance Computing (HPC) applications like weather modeling|

## EC2 Instance Lifecycle

![](/images/aws/instance_lifecycle.png)
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html

- Only EBS backend instances can be **stopped or hibernated**
- When you terminate an EC2 instance, **everything** on root device (EBS or instance store) is lost
- Hibernating **preserves RAM memory** in root EBS volume
	- Provides **quick restarts** for use cases with either long running processes or slow boot up times
- Hibernating can be done for a **max of 60 days**

## RAID
![](/images/aws/001-basic-drawings/05-raid-0.png)
- Need **higher durability** than one EBS volume? 
	- Use **RAID 1** structure
	- Same performance and storage capacity BUT **higher fault tolerance**
- Need **higher IOPS or storage** than one EBS volume?
	- Use **RAID 0** structure
	- Double the storage, IOPS and throughput BUT data lost even if one disk fails
	- Use this when **I/O performance is more important than fault tolerance**. Ex: Replicated Database

## EBS Snapshots and AMIs
![](/images/aws/00-icons/ebs.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/snapshot.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ami.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/ec2.png)
- You **can create**:
	- Snapshot from EBS volume and vice versa
	- AMI from EC2 instance and vice versa
	- AMI from root EBS volume snapshots

## Using an AMI from different AWS account or region
![](/images/aws/00-icons/ami.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ami.png)
- Scenario : You want to use an AMI belonging to a different AWS account or a different region
	- REMEMBER : AMI are restricted to a region
	- Step I (Optional) : Owner of AMI provides read permission to the AMI
	- Step II(Optional) : For encrypted AMI, owner should share the encryption keys
	- Step III : Copy the AMI into your region
	- If you do not have permission to copy an AMI but you have permission to use an AMI:
		- Create an EC2 instances from AMI
		- Create a new AMI from EC2 instance

## Amazon EBS Certification and Interview Questions - with EC2

| Scenario | Solution  | 
|--|:--|
|Can I attach an EBS volume in us-east-1a to EC2 instance in us-east-1b?|No. EBS volumes should in the same AZ as your EC2 instance|
|Can I attach multiple EBS volumes to EC2 instance?|Yes|
|Can I attach an EBS volume with two EC2 instances?|No|
|Can I switch EBS volume from EC2 instance to another?|Yes|
|Will an EBS volume be immediately available when attached to an EC2 instance?|Yes. However, by default, data is lazily loaded|
|How do you ensure that an EBS volume is deleted when EC2 instance is terminated?|Enable **Delete on Termination** on EC2 instance|
|How do you retain EBS volume even if an EBS backed EC2 instance fails?|Remember : On termination of EC2 instance all data on root volume is lost (even if it is EBS backed) <BR/>Detach the EBS volume before terminating the instance<BR/>Recover data by connecting the EBS volume to another EC2 instance|

## Amazon EBS Certification and Interview Questions - Snapshots

| Scenario | Solution  | 
|--|:--|
|How do you create an EBS volume from an EBS volume in a different AZ?|Take a snapshot <BR/> Create EBS volume from snapshot|
|How do you create an EBS volume from EBS volume in a different region?|Take a snapshot <BR/> Copy the snapshot to second region <BR/> Create EBS volume from snapshot in second region|
|What is the lowest cost option to maintain snapshots with EBS?|Store just the latest snapshot. Other snapshots can be deleted without a problem|
|How do you encrypt an unencrypted EBS volume?|Take a snapshot <BR/> Encrypt the snapshot <BR/> Create new encrypted volume from snapshot|
|How do you automate the complete lifecycle (creation, retention, and deletion) of Amazon EBS snapshots?|Use **Amazon Data Lifecycle Manager** <BR/> Reduces costs and maintenance effort|

## Amazon EBS - Summary

![](/images/aws/00-icons/ebs.png) 
- Amazon EBS vs instance store
- **Features**:
	- Highly available and durable (within the same AZ)
	- Supports live changes to volumes without service interruptions
	- Transparent encryption integration with KMS
- **Types**:
	- **Cold HDD**: Infrequent access usecases (minimum cost)
	- **Throughput Optimized HDD**: Frequently accessed, large sequential operations with high throughput (cost sensitive)
	- **General Purpose SSD**: System boot volumes and transactional workloads
	- **Provisioned IOPS SSD**: Transactional workloads needing very high IOPS
- EBS volume <-> Snapshot -> AMI

## Amazon EFS

![](/images/aws/001-basic-drawings/efs.png)
- **Petabyte scale, Auto scaling** shared file storage
	- POSIX compliant
	- Supports **NFS v4.0** and **v4.1** protocols
- Pay for use 
- High availability and durability across AZs in one region
- Compatible with Amazon EC2 Linux-based instances
	- Share with thousands of Amazon EC2 instances
	- Use **Max I/O Mode** for higher throughput (with a small increase in latency for all file operations)
- **Use cases** :  home directories, file share, media workflows and content management

## Amazon FSx for Lustre
- File system **optimized for performance**
	- For high performance computing (HPC), machine learning, and media processing use cases
	- Sub-millisecond latencies, up to hundreds of gigabytes per second of throughput, and up to millions of IOPS
- Integrates with Amazon S3 
	- Process data sets directly stored in S3
- POSIX-compliant 
	- Connect Linux-based applications without having to make any changes
- File system data is automatically encrypted at-rest and in-transit

## Amazon FSx Windows File Servers
- Fully managed Windows file servers 
- Uses Service Message Block (SMB) protocol
- Accessible from Windows, Linux and MacOS instances
- Integrates with Microsoft Active Directory (AD) to support Windows-based environments and enterprises.
- Offers single-AZ and multi-AZ deployment options, SSD and HDD storage options, and provides fully managed backups.
- File system data is automatically encrypted at rest and in transit.
- (Remember) All File Sharing options are accessible on AWS or on premises

## Review of storage options

| Type    | Examples                            | Latency         | Throughput | Shareable |
|--|--|--|--|
|  Block  |  EBS, Instance Store                |  Lowest         | Single  | Attached to one instance at a time. Take snapshots to share.|
|  File   |  EFS, FSx Windows, FSx for Lustre   | Low             | Multiple | Yes |
|  Object | S3                                  |  Low            | Web Scale | Yes|
|  Archival| Glacier                            | Minutes to hours| High | No|

Note:
Performance Pillar 9

## AWS Storage Gateway

![](/images/aws/01-S3/5-Storage-Gateway.png)
- **Hybrid storage** (cloud + on premise)
- Unlimited cloud storage for on-premise software applications and users with good performance
- (Remember) Storage Gateway and S3 Glacier **encrypt data** by default
- **Three Options**
	- AWS Storage File Gateway
	- AWS Storage Tape Gateway
	- AWS Storage Volume Gateway
- VM image with AWS Storage Gateway software deployed on-premises

## AWS Storage File Gateway

![](/images/aws/storage-gateway-file-gateway.png)
- **Problem Statement**: Large on-premise file share with terabytes of data
	- Users put files into file share and applications use the files
	- Managing it is becoming expensive
	- Move the file share to cloud without performance impact
- AWS Storage File Gateway provides cloud storage for your file shares
	- Files **stored** in **Amazon S3 & Glacier**
	- Supports **Network File System (NFS)** and **Server Message Block (SMB)**

## AWS Storage File Gateway

![](/images/aws/01-S3/6-FileGateway.png)
- File gateway **deployed as virtual machine** on-premises 
	- Maintains a local cache with most recently used objects
- Benefits from **S3 features**
	- High durability, low-cost, lifecycle management and cross-region replication
- Benefits from **S3 integrations** 
	- Data analytics and machine learning applications using Amazon EMR or Amazon Athena
- Each file gateway supports **up to 10 bucket shares**

## AWS Storage Tape Gateway

![](/images/aws/storage-gateway-tape-gateway.png)
- Tape backups used in enterprises (archives)
	- Stored off-site - expensive, physical wear and tear
- **AWS Storage Tape Gateway** - Avoid physical tape backups 
- **No change needed** for tape backup infrastructure
- Backup data to virtual tapes (actually, Amazon S3 & Glacier)
- Benefit from S3 features
	- encryption, high durability, low-cost, and cross-region replication
- Use **S3 lifecycle management**
	- move data to S3 Glacier and S3 Glacier Deep Archive

## AWS Storage Volume Gateway

![](/images/aws/01-S3/7-volume-gateway.png)
- **Volume Gateway** : Move block storage to cloud
- Supports iSCSI protocol
- Reduce costs 
- Automate backup and disaster recovery
- Use AWS Backup for backup and restore
- Use cases
	- Backup and disaster recovery
	- Migration of application data

## AWS Storage Volume Gateway - Cached and Stored

![](/images/aws/storage-gateway-cached-volume-gateway.png)
![](/images/aws/storage-gateway-stored-volume-gateway.png)
- **Cached** (Gateway Cached Volumes):
	- Primary Data Store - **AWS - Amazon S3**
	- **On-premise cache** stores frequently accessed data
	- Data in S3 CANNOT be accessed directly
		- Take EBS snapshots from cached volumes
- **Stored** (Gateway Stored Volumes): 
	- Primary Data Store - **On-Premises**
	- Asynchronous copy to AWS
	- Stored as EBS snapshots
		- For disaster recovery, restore to EBS volumes

## AWS Storage Gateway - Summary
- Key to look for : **Hybrid storage** (cloud + on premise)
	- File share (NFS or SMB) + Looking for S3 features and integrations => **AWS Storage File Gateway**
	- Tapes on cloud => **AWS Storage Tape Gateway**
	- Volumes on cloud (Block Storage) => **AWS Storage Volume Gateway**
		- High performance => **Stored**
		- Otherwise => **Cached**
- Needs additional setup on-premises
	- **VM image** with AWS Storage Gateway **software** deployed on-premises or on EC2 instance

# Database Fundamentals

## Databases Primer

![](/images/aws/00-icons/database.png) 
- Databases provide **organized** and **persistent** storage for your data
- To **choose between different database types**, we would need to understand:
	- Availability
	- Durability
	- RTO
	- RPO
	- Consistency
	- Transactions etc
- Let's get started on a **simple journey** to understand these

## Database - Getting Started

![](/images/aws/rds/1-single-db.png)
- Imagine a database deployed **in a data center in London**
- Let's consider some challenges:
	- **Challenge 1**: Your database will go down if the data center crashes or the server storage fails
	- **Challenge 2**: You will lose data if the database crashes

## Database - Snapshots

![](/images/aws/rds/2-single-db-snapshot.png)
- Let's automate taking copy of the database (**take a snapshot**) every hour to another data center in London
- Let's consider some challenges:
	- **Challenge 1**: Your database will go down if the data center crashes
	- **Challenge 2** (PARTIALLY SOLVED): You will lose data if the database crashes
		- You can setup database from latest snapshot. But depending on when failure occurs you can lose up to an hour of data
	- **Challenge 3**(NEW): Database will be slow when you take snapshots

## Database - Transaction Logs

![](/images/aws/rds/3-single-db-snapshot-transaction.png)
- Let's add **transaction logs** to database and create a **process to copy it over** to the second data center
- Let's consider some challenges:
	- **Challenge 1**: Your database will go down if the data center crashes
	- **Challenge 2** (SOLVED): You will lose data if the database crashes
		- You can setup database from latest snapshot and apply transaction logs
	- **Challenge 3**: Database will be slow when you take snapshots

## Database - Add a Standby

![](/images/aws/rds/4-standby-database.png)
- Let's add a **standby database** in the second data center with replication
- Let's consider some challenges:
	- **Challenge 1** (SOLVED): Your database will go down if the data center crashes
		- You can switch to the standby database
	- **Challenge 2** (SOLVED): You will lose data if the database crashes
	- **Challenge 3** (SOLVED): Database will be slow when you take snapshots
		- Take snapshots from standby. 
		- Applications connecting to master will get good performance always

## Availability and Durability
- **Availability**
	- Will I be able to access my data now and when I need it?
	- Percentage of time an application provides the operations expected of it
- **Durability**
	- Will my data be available after 10 or 100 or 1000 years?
- Examples of measuring availability and durability:
	- 4 9's - 99.99
	- 11 9's - 99.999999999
- Typically, an **availability of four 9's** is considered very good
- Typically, a **durability of eleven 9's** is considered very good

## Availability

| Availability | Downtime (in a month)  | Comment |
|--|--|--|
| 99.95% | 22 minutes||
| 99.99% (4 9's)| 4 and 1/2 minutes | Typically online apps aim for 99.99% (4 9's) availability|
| 99.999% (5 9's) | 26 seconds| Achieving 5 9's availability is tough|

## Durability

![](/images/aws/rds/4-standby-database.png)

- What does a **durability of 11 9's** mean? 
	- If you **store one million files for ten million years**, you would expect to **lose one file**
- Why should durability be high?
	- Because **we hate losing data**
	- Once we lose data, it is gone

## Increasing Availability and Durability of Databases

![](/images/aws/rds/4-standby-database.png)
- **Increasing Availability**:
	- Have multiple standbys available 
		- in multiple AZs
		- in multiple Regions
- **Increasing Durability**:
	- Multiple copies of data (standbys, snapshots, transaction logs and replicas)
		- in multiple AZs
		- in multiple Regions
- **Replicating data** comes with its own challenges!
	- We will talk about them a little later

## Database Terminology : RTO and RPO

![](/images/aws/00-icons/database.png) 
- Imagine a **financial transaction being lost** 
- Imagine a **trade being lost**
- Imagine a **stock exchange going down** for an hour
- **Typically** businesses are fine with some downtime but they hate losing data
- Availability and Durability are technical measures
- How do we measure **how quickly we can recover from failure**?
	- **RPO (Recovery Point Objective)**: Maximum acceptable period of data loss
	- **RTO (Recovery Time Objective)**: Maximum acceptable downtime
- Achieving **minimum RTO and RPO is expensive** 
- **Trade-off** based on the criticality of the data

## Question - RTO and RPO

- You are running an EC2 instance storing its data on a EBS. You are taking EBS snapshots every 48 hours. If the EC2 instance crashes, you can manually bring it back up in 45 minutes from the EBS snapshot. What is your RTO and RPO?
	- RTO - 45 minutes
	- RPO - 48 hours

## Achieving RTO and RPO - Failover Examples

 
| Scenario | Solution  | 
|--|:--|
| Very small data loss (RPO - 1 minute) <BR/> Very small downtime (RTO - 5 minutes)   | **Hot standby** - Automatically synchronize data <BR/> Have a standby ready to pick up load <BR/> Use automatic failover from master to standby|
| Very small data loss (RPO - 1 minute) <BR/> BUT I can tolerate some downtimes (RTO - 15 minutes)| **Warm standby** - Automatically synchronize data <BR/> Have a standby with minimum infrastructure <BR/> Scale it up when a failure happens|
| Data is critical (RPO - 1 minute) but I can tolerate downtime of a few hours (RTO - few hours)| Create regular data **snapshots and transaction logs** <BR/> Create database from snapshots and transactions logs when a failure happens|
| Data can be lost without a problem (for example: cached data)|Failover to a completely new server|

## (New Scenario) Reporting and Analytics Applications

![](/images/aws/rds/5-reporting-database-application.png)
- New reporting and analytics applications are being launched using the same database
	- These applications will ONLY read data
- Within a few days you see that the database performance is impacted
- How can we fix the problem?
	- **Vertically scale the database** - increase CPU and memory
	- **Create a database cluster** - typically database clusters are expensive to setup
	- **Create read replicas** - Run read only applications against read replicas

## Database - Read Replicas

![](/images/aws/rds/6-sep-reporting-database-application.png)
- Add **read replica**
- Connect reporting and analytics applications to **read replica**
- Reduces load on the master databases
- Upgrade read replica to master database (supported by some databases)
- Create read replicas **in multiple regions**
- **Take snapshots** from read replicas

## Consistency

![](/images/aws/rds/6-sep-reporting-database-application.png)
- How do you ensure that data in multiple database instances (standbys and replicas) is updated simultaneously?
- **Strong consistency** - Synchronous replication to all replicas
	- Will be slow if you have multiple replicas or standbys
- **Eventual consistency** - Asynchronous replication. A little lag - few seconds - before the change is available in all replicas
	- In the intermediate period, different replicas might return different values
	- Used when scalability is more important than data integrity
	- Examples : Social Media Posts - Facebook status messages, Twitter tweets, Linked in posts etc
- **Read-after-Write consistency** - Inserts are immediately available. Updates and deletes are eventually consistent
	- Amazon S3 provides read-after-write consistency

## Database Categories

![](/images/aws/00-icons/rds.png)
![](/images/aws/00-icons/elasticache.png) 
![](/images/aws/00-icons/dynamodb.png)
![](/images/aws/00-icons/redshift.png)
- There are **several categories** of databases:
	- Relational (OLTP and OLAP), Document, Key Value, Graph, In Memory among others
- **Choosing type of database** for your use case is not easy. A few factors:
	- Do you want a **fixed schema**?
		- Do you want flexibility in defining and changing your schema? (schemaless)
	- What level of **transaction properties** do you need? (atomicity and consistency)
	- What kind of **latency** do you want? (seconds, milliseconds or microseconds)
	- **How many transactions** do you expect? (hundreds or thousands or millions of transactions per second)
	- **How much data** will be stored? (MBs or GBs or TBs or PBs)
	- and a lot more...

## Relational Databases

![Database](./images/aws/relational-schema.png)
- This was the **only option** until a decade back!
- Most **popular (or unpopular)** type of databases
- **Predefined schema** with tables and relationships
- Very **strong transactional** capabilities
- Used for 
	- OLTP (Online Transaction Processing) use cases and
	- OLAP (Online Analytics Processing) use cases

## Relational Database - OLTP (Online Transaction Processing)

![](/images/aws/00-icons/rds.png) 
- Applications where **large number of users make large number of small transactions** 
	- small data reads, updates and deletes
- **Use cases**:
	- Most traditional applications, ERP, CRM, e-commerce, banking applications
- **Popular databases**:
	- MySQL, Oracle, SQL Server etc
- Recommended AWS Managed Service: 
	- **Amazon RDS**
	- Supports Amazon Aurora, PostgreSQL, MySQL, MariaDB (Enhanced MySQL), Oracle Database, and SQL Server

## Relational Database - OLAP (Online Analytics Processing)

![](/images/aws/00-icons/redshift.png) 
- Applications allowing users to **analyze petabytes of data**
	- **Examples** : Reporting applications, Data ware houses, Business intelligence applications, Analytics systems
	- **Sample application** : Decide insurance premiums analyzing data from last hundred years
	- Data is consolidated from multiple (transactional) databases
- Recommended AWS Managed Service 
	- **Amazon Redshift**
	- **Petabyte-scale** distributed data ware house based on PostgreSQL

## Relational Databases - OLAP vs OLTP

![Database](./images/aws/database-columnar-storage.png)
![Database](./images/aws/database-columnar-storage-2.png)

- OLAP and OLTP use **similar data structures**
- BUT **very different approach in how data is stored**
- **OLTP databases** use row storage 
	- Each table row is stored together
	- Efficient for processing small transactions
- **OLAP databases** use columnar storage
	- Each table column is stored together
	- **High compression** - store petabytes of data efficiently
	- **Distribute data** - one table in multiple cluster nodes 
	- **Execute single query across multiple nodes** - Complex queries can be executed efficiently

## Document Database

![](/images/aws/database-document.png)
![](/images/aws/document-database-example.png)

- Structure data **the way your application needs it**
- Create **one table instead of dozens**!
- **Quickly evolving** semi structured data (**schema-less**)
- **Use cases** : Content management, catalogs, user profiles
- **Advantages** : (Horizontally) Scalable to **terabytes of data** with **millisecond responses** upto **millions of transactions per second**
- Recommended AWS Managed Service 
	- **Amazon DynamoDB**

## Key-value
![Database](./images/aws/database-key-value.png)
![Database](./images/aws/database-session-store.png)
- Use a **simple key-value pair** to store data. Key is a unique identifier.
- Values can be objects, compound objects or simple data values
- **Advantages** : (Horizontally) Scalable to **terabytes of data** with **millisecond responses** upto **millions of transactions per second**
- Recommended AWS Managed Service - **Amazon DynamoDB** again
- **Use cases** : shopping carts, session stores, gaming applications and very high traffic web apps

## Graph
![Database](./images/aws/graph.png)
- **Store and navigate** data with complex relationships
- **Use cases** : Social Networking Data (Twitter, Facebook), Fraud Detection
- Recommended AWS Managed Service - **Amazon Neptune**

## In-memory Databases

![](/images/aws/00-icons/elasticache.png) 
- **Retrieving data from memory is much faster from retrieving data from disk**
- In-memory databases like Redis deliver microsecond latency by storing **persistent data in memory**
- Recommended AWS Managed Service 
	- **Amazon ElastiCache**
	- Supports Redis and Memcached
		- Redis is recommended for persistent data
		- Memcached is recommended for simple caches
- **Use cases** : Caching, session management, gaming leader boards, geospatial applications

## Databases - Summary

| Database Type | AWS Service  | Description |
|--|:--|:--|
| Relational OLTP databases   |  Amazon RDS     |  Row storage <BR/>Transactional usecases needing **predefined schema** and very **strong transactional** capabilities       |
|Relational OLAP databases|Amazon Redshift|Columnar storage <BR/>Reporting, analytics & intelligence apps needing **predefined schema**|
|Document & Key Databases|Amazon DynamoDB|Apps needing **quickly evolving** semi structured data (**schema-less**) <BR/> Scale to **terabytes of data** with **millisecond responses** upto **millions of TPS**<BR/>Content management, catalogs, user profiles, shopping carts, session stores and gaming applications|

## Databases - Summary
| Database Type | AWS Service  | Description |
|--|:--|:--|
|Graph Databases|Amazon Neptune|Store and navigate data with **complex relationships**<BR/>Social Networking Data (Twitter, Facebook), Fraud Detection|
|In memory databases/caches|Amazon ElastiCache|Applications needing **microsecond** responses<BR/>**Redis** - persistent data<BR/>**Memcached** - simple caches|

## Databases - Questions

| Scenario | Solution  | 
|--|:--|
|A start up with quickly evolving tables  |   DynamoDB    |
|Transaction application needing to process million transactions per second  |   DynamoDB    |
|Very high consistency of data is needed while processing thousands of transactions per second| RDS |
|Cache data from database for a web application| Amazon ElastiCache |
|Relational database for analytics processing of petabytes of data| Amazon Redshift |

## Amazon RDS (Relational Database Service)

![](/images/aws/00-icons/rds.png) 
- Do you want to manage the setup, backup, scaling, replication and patching of your relational databases? 
	- Or do you want to use a managed service?
- Amazon RDS is a managed relational database service for OLTP use cases 
- Supports: 
	- Amazon Aurora
	- PostgreSQL
	- MySQL (InnoDB storage engine full supported)
	- MariaDB (Enhanced MySQL)
	- Oracle Database
	- Microsoft SQL Server

## Amazon RDS - Features

![](/images/aws/00-icons/rds.png) 

- Multi-AZ deployment (standby in another AZ)
- Read replicas:
	- Same AZ 
	- Multi AZ (Availability+)
	- Cross Region(Availability++) 
- Storage auto scaling (up to a configured limit)
- Automated backups (restore to point in time)
- Manual snapshots

## Amazon RDS - You vs AWS

![](/images/aws/00-icons/rds.png) 

- AWS is responsible for 
	- Availability (according to your configuration)
	- Durability
	- Scaling (according to your configuration)
	- Maintenance (patches)
	- Backups
- You are responsible for 
	- Managing database users
	- App optimization (tables, indexes etc)
- You CANNOT
	- SSH into database EC2 instances or setup custom software (NOT ALLOWED)
	- Install OS or DB patches. RDS takes care of them (NOT ALLOWED)

## Multi-AZ Deployments

![](/images/aws/rds/7-multi-az-deployment.png)

- Standby created in a different AZ
- **Synchronous replication** (strong consistency)
- Enhances durability, availability and fault tolerance of your database
- Multi-AZ makes **maintenance easy**
	- Perform maintenance (patches) on standby
	- Promote standby to primary
	- Perform maintenance on (old) primary
- **Avoid I/O suspension** when data is backed up (snapshots are taken from standby)

## Multi-AZ Deployments

![](/images/aws/rds/7-multi-az-deployment.png)

- No downtime when database is converted to Multi AZ
	- Increased latency until standby is ready
- Not allowed to connect to standby database directly 
	- For example: Standby CANNOT be used to serve read traffic
	- Standby increases availability but does not improve scalability
- Automatic failover to standby if master has problems (compute, storage or networking)
	- CNAME record flipped to standby
	- Database performance issues (long running queries or deadlocks) will NOT cause a failover
- (Good Practice) Use DNS name of database in applications configuration

## Read Replicas

![](/images/aws/rds/8-read-replica-deployment.png)
- Support **read-heavy database workloads** - reporting and data warehousing 
- Can be in same or different AZ or different Region
- Your apps can connect to them
- Create read replica(s) of a read replica
- Uses **asynchronous replication**
	- Provides eventual consistency (from replica)
	- For higher consistency, read from master
- Need to be **explicitly deleted** (Not deleted when database is deleted)

## Read Replicas - Few Tips
- (Mandatory) Enable automatic backups before you can create read replicas
	- Set Backup Retention period to a value other than 0
- Reduce replication lag by using better compute and storage resources
- Maximum no of read replicas:
	- MySQL, MariaDB, PostgreSQL, and Oracle - 5
	- Aurora - 15
	- SQL Server does not support read replicas

## Multi-AZ vs Multi-Region vs Read replicas

|Feature|Multi-AZ deployments|Multi-Region Read Replicas|Multi-AZ Read replicas|
|--|:--|:--|:--|
|Main purpose|High availability|Disaster recovery and local performance|Scalability|
|Replication|Synchronous (except for Aurora - Asynchronous)|Asynchronous|Asynchronous|
|Active|Only master (For Aurora - all)|All read replicas|All read replicas|

## Amazon Aurora

![](/images/aws/AuroraArch001.png)
https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html
- MySQL and PostgreSQL-compatible
- 2 copies of data each in a minimum of 3 AZ
- Up to 15 read replicas (Only 5 for MySQL)
- Provides "Global Database" option
	- Up to five read-only, secondary AWS Regions
		- Low latency for global reads
		- Safe from region-wide outages
	- Minimal lag time, typically less than 1 second
- Deployment Options
	- Single master (One writer and multiple readers) 
	- Multi master deployment (multiple writers)
	- Serverless
- Uses cluster volume (multi AZ storage)
	

## RDS - Scaling

![](/images/aws/00-icons/rds.png) 
- Vertical Scaling: Change DB instance type and scale storage
	- Storage and compute changes are typically applied during maintenance window
	- You can also choose to “apply-immediately”
	- RDS would take care of data migration
		- Takes a few minutes to complete
	- You can manually scale Aurora, MySQL, MariaDB, Oracle, and PostgreSQL engines to 64 TB
	- SQL Server can be scaled up to 16 TB
- Vertical Scaling: RDS also supports auto scaling storage
- Horizontal Scaling
	- Configure Read Replicas
	- For Aurora  (Multi-master, Writer with multiple readers etc)

## RDS - Operations

![](/images/aws/00-icons/rds.png) 
![](/images/aws/00-icons/cloudwatch.png) 
![](/images/aws/00-icons/config.png) 

- RDS console shows metrics upto a certain time period
- CloudWatch show historical data
- Configure CloudWatch alarms to alert when you near max capacity
- Enable Enhanced Monitoring to monitor slow queries
- Automatic backup during backup window (to Amazon S3)
	- Enables restore to **point in time**
	- Backups retained for 7 days by default (max - 35 days)
	- Elevated latency when snapshots are taken (except for Multi-AZ setup)
- Backup window used to **apply patches**
	- If you do not configure a 30 minute backup window, RDS chooses one randomly
- Achieve RPO of up to 5 minutes

## RDS - Security and Encryption

![](/images/aws/00-icons/kms.png)
![](/images/aws/00-icons/subnet.png)
![](/images/aws/00-icons/rds.png)
![](/images/aws/00-icons/securitygroup.png)

- Create in a VPC private subnet
- Use security groups to control access
- Option to use IAM Authentication with Aurora, MySQL and PostgreSQL
	- Use IAM roles and no need for passwords
- Enable encryption with keys from KMS
- When encryption is enabled
	- Data in the database, automated backups, read replicas and snapshots are all encrypted
- Data In-flight Encryption
	- Using SSL certificates

## RDS - Costs - Key Elements
- **DB instance hours** - How many hours is the DB instance running? 
- **Storage (per GB per month)** - How much storage have you provisioned for your DB instance?
- **Provisioned IOPS per month** - If you are using Amazon RDS Provisioned IOPS (SSD) Storage
- **Backups and snapshot storage** (across multi AZ) - More backups, More snapshots => More cost
- **Data transfer costs**

## Amazon RDS - When to use?

![](/images/aws/00-icons/rds.png) 
- Use Amazon RDS for transactional applications needing 
	- Pre-defined schema
	- Strong transactional capabilities
	- Complex queries
- Amazon RDS is **NOT recommended** when
	- You need highly scalable massive read/write operations - for example millions of writes/second
		- Go for DynamoDB
	- When you want to upload files using simple GET/PUT REST API
		- Go for Amazon S3
	- When you need heavy customizations for your database or need access to underlying EC2 instances
		- Go for a custom database installation

## RDS - Certification and Interview Questions

| Scenario | Solution  | 
|--|:--|
|You want full control of OS or need elevated permissions|Consider going for a custom installation (EC2 + EBS)|
|You want to migrate data from an on-premise database to cloud database of the same type|Consider using AWS Database Migration Service|
|You want to migrate data from one database engine to another (Example : Microsoft SQL Server to Amazon Aurora)|Consider using AWS Schema Conversion Tool|
|What are retained when you delete a RDS database instance?|All automatic backups are deleted<BR/>All manual snapshots are retained (until explicit deletion)<BR/>(Optional) Take a final snapshot|

## RDS - Certification and Interview Questions

| Scenario | Solution  | 
|--|:--|
|How do you reduce global latency and improve disaster recovery?|Use multi region read replicas|
|How do you select the subnets a RDS instance is launched into?|Create DB Subnet groups|
|How can you add encryption to an unencrypted database instance?|Create a DB snapshot<BR/>Encrypt the database snapshot using keys from KMS<BR/>Create a database from the encrypted snapshot|
|Are you billed if you stop your DB instance? |You are billed for storage, IOPS, backups and snapshots. You are NOT billed for DB instance hours|
|I will need RDS for at least one year. How can I reduce costs?|Use Amazon RDS reserved instances.|
|Efficiently manage database connections| Use Amazon RDS Proxy <BR/> Sits between client applications (including lambdas) and RDS|

## Amazon DynamoDB 

![](/images/aws/00-icons/dynamodb.png) 
- Fast, scalable, distributed for any scale
- Flexible NoSQL Key-value & document database (schemaless) 
- Single-digit millisecond responses for million of TPS
- Do not worry about scaling, availability or durability
	- Automatically partitions data as it grows
	- Maintains 3 replicas within the same region
- No need to provision a database 
	- Create a table and configure read and write capacity (RCU and WCU)
	- Automatically scales to meet your RCU and WCU
- Provides an expensive serverless mode
- Use cases: User profiles, shopping carts, high volume read write applications

## DynamoDB Tables

![](/images/aws/document-database-example.png)
- Hierarchy : Table > item(s) > attribute (key value pair)
- Mandatory primary key
- Other than the primary key, tables are schemaless
	- No need to define the other attributes or types
	- Each item in a table can have distinct attributes
- Max 400 KB per item in table
	- Use S3 for large objects and DynamoDB for smaller objects

## DynamoDB - Keys

![](/images/aws/rds-diagrams/xx-rds-dynamodb-partition.png)

- Two parts:
	- (Mandatory) Partition key
	- (Optional) Sort key
- Primary key should be unique
- Partition key decides the partition (input to hash function)
- Same partition key items stored together (sorted by sort key)

## DynamoDB - Indexes

![](/images/aws/rds-diagrams/xx-rds-dynamodb-partition.png)
- (Optional) Secondary indexes to query on keys other than primary key
- Local secondary index 
	- Same partition key as primary key but different sort key
	- Should be created at the table creation
- Global secondary index 
	- Partition and sort key different from primary key
	- Can be added and removed at any point in time
	- Stored separately from the original table

## DynamoDB Query vs Scan

![](/images/aws/00-icons/dynamodb.png) 

- Query 
	- Search using a partition key attribute and a distinct value to search
	- Optional - sort key and filters
	- Results are sorted by primary key
	- Max 1 MB
- Scan 
	- Reads every item in a table
	- Expensive compared to query
	- Returns all attributes by default
	- Supports paging above 1 MB
	- Filter items using expressions

## DynamoDB Consistency Levels

![](/images/aws/00-icons/dynamodb.png) 

- By default, eventually consistent (lag of about a second)
- Request for strongly consistent reads 
	- Set `ConsistentRead` to true
	- Slow and more expensive
- Supports transactions
	- All-or-nothing changes to multiple items both within and across tables
	- Twice the cost

## DynamoDB Read/Write Capacity Modes

![](/images/aws/00-icons/dynamodb.png) 

- Provisioned 
	- Provision read and write capacity 
	- Dynamically adjustable
	- Unused capacity can be used in bursts
	- You are billed for the provisioned capacity irrespective of whether you make use of it or not
- On Demand
	- Truly serverless and expensive
	- For unknown workloads or traffic with huge spikes
	- Use On Demand only when your  
		- Workloads are really spiky causing low utilization of Provisioned Capacity OR
		- Usage is very low (for example, in test environments) making manual adjustments expensive

## DynamoDB Read/Write Capacity Used

![](/images/aws/00-icons/dynamodb.png) 
- Capacity used depends on size of item, read consistency, transactions etc
- 1 capacity unit to read 4 KB or smaller (more for bigger items)
- 1 capacity unit to write 1 KB or smaller (more for bigger items)
- Twice the capacity for a strongly consistent or transactional requests
- On-demand RCU is almost 8 times the cost of Provisioned RCU
- Example: $0.2500 per million vs $0.0361 per million

Note:
- RCU vs WCU (RCU is cheaper than WCU. So, it is cheaper for read workloads.)

## DynamoDB - Operations

![](/images/aws/00-icons/dynamodb.png) 

- Performance Monitoring - CloudWatch
- Alerts on RCU, WCU and Throttle Requests - CloudWatch Alarms
- Migrate data from RDS or MongoDB to DynamoDB - AWS Database Migration Service
- (Feature) Enable point-in-time recovery (max 35 days)
- Use Time to Live (TTL) to automatically expire items

## DynamoDB - IAM and Encryption

![](/images/aws/00-icons/dynamodb.png) 
- Server-side encryption in integration with keys from KMS
	- Always enabled
	- Automatically encrypts tables, DynamoDB streams, and backups
- Client-side encryption with DynamoDB Encryption Client
	- You can manage your keys with KMS or CloudHSM
- Use IAM roles to provide EC2 instances or AWS services access to DynamoDB tables
	- Predefined policies available for DynamoDB
		- AmazonDynamoDBReadOnlyAccess
		- AmazonDynamoDBFullAccess etc
	- Fine-grained control at the individual item level

##  DynamoDB vs RDS

|Feature  | DynamoDB  | RDS|
|--|:--|:--|
| Scenario   |  Millisecond latency with millions of TPS    | Stronger consistency (schema) and transactional capabilities|
| Schema| Schemaless (needs only a primary key - Great for use cases where your schema is evolving)| Well-defined schema with relationships|
|Data Access|Using REST API provided by AWS using AWS SDKs or AWS Management Console or AWS CLI|SQL queries|
|Complex Data Queries Involving Multiple Tables|Difficult to run| Run complex relational queries with multiple entities|
|Scaling| No upper limits| 64 TB |
|Consistency| Typically lower consistency | Typically higher consistency|

## DynamoDB Accelerator (DAX)
![](/images/aws/03-serverless/07-lamdba-dax.png)
- In-memory caching for DynamoDB providing microsecond response times
	- Typical DynamoDB response times - single-digit milliseconds
- Very few changes needed to connect to DAX
	- Can reduce your costs by saving your read capacity units
- Not recommended 
	- If you need strongly consistent reads or 
	- Your application is write-intensive with very few reads

## Amazon ElastiCache 

![](/images/aws/00-icons/elasticache.png) 
- Managed service providing highly scalable and low latency in-memory data store
- Used for distributed caching
- Two Options:
	- Redis
	- Memcached

## Amazon ElastiCache for Redis

![](/images/aws/00-icons/elasticache.png) 

- Highly scalable and low latency in-memory data store
- Can be used as a cache, database or message broker
- Automatic failover with Multi-AZ deployments (if enabled)
- Supports backup and restore
- Supports encryption at-rest (KMS) and in-transit
- Use cases:
	- Caching
	- Session Store
	- Chat and Messaging
	- Gaming Leader boards
	- Geospatial Apps (Ride hailing, restaurant recommendations)
	- Queues

## Amazon ElastiCache for Redis - Cluster

![](/images/aws/00-icons/elasticache.png) 

- Shard - collection of one or more nodes
- One node acts as read/write primary
- Other nodes act as read replicas (up to five read replicas)
- In case of failure:
	- Primary node is replaced
	- If Multi-AZ replication group is enabled, read replica is promoted to primary
	- DNS entry is updated

## ElastiCache Redis - Backup and Snapshot
![](/images/aws/00-icons/elasticache.png) 
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png)
- Uses native backup feature of Redis (stored to S3)
- Recommended to perform snapshot against read replicas
- You can schedule snapshots 
	- Configure backup window and 
	- Days of backup you want to store
- Manual snapshots are available until they are manually deleted

## Amazon ElastiCache for Memcached

![](/images/aws/00-icons/elasticache.png) 
- Simple caching layer intended for use in speeding up dynamic web applications
	- Pure cache
	- Non-persistent
	- Simple key-value storage
- Ideal front-end for data stores like RDS or DynamoDB
- Can be used as a transient session store
- Create upto 20 cache nodes
- Use Auto Discovery to discover cache nodes

## Amazon ElastiCache for Memcached - Limitations

![](/images/aws/00-icons/elasticache.png) 
- Backup and restore NOT supported
- Does not support encryption or replication
- Does not support snapshots
	- When a node fails, all data in the node is lost
	- Reduce impact of failure by using large number of small nodes

## ElastiCache Memcached vs Redis

![](/images/aws/00-icons/elasticache.png) 

- Use ElastiCache Memcached for
	- Low maintenance simple caching solution
	- Easy horizontal scaling with auto discovery
- Use ElastiCache Redis for
	- Persistence 
	- Publish subscribe messaging
	- Read replicas and failover
	- Encryption

# CloudTrail, Config & CloudWatch

## AWS CloudTrail

![](/images/aws/00-icons/cloudtrail.png)
- Track events, API calls, changes made to your AWS resources: 
	- Who made the request?
	- What action was performed?
	- What are the parameters used?
	- What was the end result?
- (USE CASE) Compliance with regulatory standards
- (USE CASE) Troubleshooting. Locate a missing resource
- Delivers log files to S3 and/or Amazon cloud watch logs log group ( S3 is default )
- You can setup SNS notifications for log file delivery

## AWS Cloud Trail Types

![](/images/aws/00-icons/cloudtrail.png)
- Multi Region Trail 
	- One trail of all AWS regions
	- Events from all regions can be sent to one CloudWatch logs log group
- Single Region Trail 
	- Only events from one region
	- Destination S3 bucket can be in any region

## AWS Cloud Trail - Good to know

![](/images/aws/00-icons/cloudtrail.png)
- Log files are automatically encrypted with Amazon S3 SSE
- You can configure S3 Lifecycle rules to archive or delete log files
- Supports log file integrity 
	- You can prove that a log file has not been altered

## AWS Config

![](/images/aws/00-icons/config.png) 

- **Auditing** 
	- Create a complete inventory of your AWS resources
- **Resource history and change tracking** 
	- Find how a resource was configured at any point in time
	- Configuration of deleted resources would be maintained
	- Delivers history file to S3 bucket every 6 hours 
	- Take configuration snapshots when needed
- **Governance**
	- Customize Config Rules for specific resources or for entire AWS account
	- Continuously evaluate compliance against desired configuration
	- Get a SNS notification for every configuration change
- **Consistent rules and compliance** across AWS accounts:
	- Group Config Rules and Remediation Actions into Conformance Packs

## Predefined Config Rule Examples (80+)

![](/images/aws/00-icons/config.png) 
- **alb-http-to-https-redirection-check** - Checks whether HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancers
- **ebs-optimized-instance** - Checks whether EBS optimization is enabled for your EC2 instances that can be EBS-optimized
- **ec2-instance-no-public-ip** - Do EC2 instances have public IPs?
- **encrypted-volumes** - Are all EC2 instance attached EBS volumes encrypted?
- **eip-attached** - Are all Elastic IP addresses used?
- **restricted-ssh** - Checks whether security groups that are in use disallow unrestricted incoming SSH traffic

## AWS Config Rules

![](/images/aws/00-icons/config.png) 
- (Feature) Create Lambda functions with your custom rules
- (Feature) You can setup auto remediation for each rule
	- Take immediate action on a non compliant resource
	- (Example) Stop EC2 instances without a specific tag!
- Enable AWS Config to use the rules
	- No Free Tier
	- More rules to check => More $$$$

## AWS Config + AWS CloudTrail

![](/images/aws/00-icons/config.png) 
![](/images/aws/00-icons/cloudtrail.png) 

- AWS Config 
	- What did my AWS resource look like?
- AWS CloudTrail 
	- Who made an API call to modify this resource?

## Monitoring AWS with Amazon CloudWatch

![](/images/aws/00-icons/cloudwatch.png) 
- Monitoring and observability service
- Collects monitoring and operational data in the form of logs, metrics, and events
- Set alarms, visualize logs, take automated actions and troubleshoot issues
- Integrates with more than 70 AWS services:
	- Amazon EC2
	- Amazon DynamoDB
	- Amazon S3
	- Amazon ECS
	- AWS Lambda
	- and ....

## Amazon CloudWatch Logs

![](/images/aws/00-icons/cloudwatch.png) 
- Monitor and troubleshoot using system, application and custom log files
- Real time application and system monitoring
	- Monitor for patterns in your logs and trigger alerts based on them
	- Example : Errors in a specific interval exceed a certain threshold
- Long term log retention
	- Store logs in CloudWatch Logs for as long as you want (configurable - default:forever)
	- Or archive logs to S3 bucket (Typically involves a delay of 12 hours)
	- Or stream real time to Amazon Elasticsearch Service (Amazon ES) cluster using CloudWatch Logs subscription

## Amazon CloudWatch Logs
- **CloudWatch Logs Agent** 
	- Installed on ec2 instances to move logs from servers to CloudWatch logs
- **CloudWatch Logs Insights** 
	- Write queries and get actionable insights from your logs
- **CloudWatch Container Insights** 
	- Monitor, troubleshoot, and set alarms for your containerized applications running in EKS, ECS and Fargate

## Amazon CloudWatch Alarms
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

- Create alarms based on: 
	- Amazon EC2 instance CPU utilization
	- Amazon SQS queue length
	- Amazon DynamoDB table throughput or 
	- Your own custom metrics

## Amazon CloudWatch Alarms
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

- Take immediate action: 
	- Send a SNS event notification
		- Send an email using SNS
	- Execute an Auto Scaling policy

## Amazon CloudWatch Alarm - Example
- You set a CPU Utilization alarm on EC2 instance with a threshold of 80% over 3 periods of 10 minutes. If CPU utilization is 90% for 20 minutes, does the alarm get triggered?
	- No

## Amazon CloudWatch Dashboards
![](/images/aws/cloudwatch-ec2.png) 
- Create auto refreshed graphs around all CloudWatch metrics
- Automatic Dashboards are available for most AWS services and resources
- Each Dashboard can have graphs from multiple regions

## Amazon CloudWatch Events

![](/images/aws/00-icons/cloudwatch.png) 
- Enable you to take immediate action based on events on AWS resources
	- Call a AWS Lambda function when an EC2 instance starts
	- Send event to an Amazon Kinesis stream when an Amazon EBS volume is created
	- Notify an Amazon SNS topic when an Auto Scaling event happens
- Schedule events - Use Unix cron syntax
	- Schedule a call to Lambda function every hour
	- Send a notification to Amazon SNS topic every 3 hours

# Decoupling Applications <BR/>with SQS, SNS and MQ

## Need for Asynchronous Communication
- Why do we need asynchronous communication?

## Synchronous Communication
![](/images/aws/02-Queuing/0-SQS-00.png)
- Applications on your web server make synchronous calls to the logging service
- What if your logging service goes down?
	- Will you applications go down too?
- What if all of sudden, there is high load and there are lot of logs coming in?
	- Log Service is not able to handle the load and goes down very often

## Asynchronous Communication - Decoupled
![](/images/aws/02-Queuing/0-SQS-01.png)
- Create a queue or a topic
- Your applications put the logs on the queue
- They would be picked up when the logging service is ready
- Good example of decoupling!

## Asynchronous Communication - Scale up
![](/images/aws/02-Queuing/0-SQS-02.png)
- You can have multiple logging service instances reading from the queue!

## Asynchronous Communication - Pull Model - SQS

![](/images/aws/02-Queuing/2-sqs.png)
- Producers put messages on the queue
- Consumers poll on the queue
	- Only one of the consumers will successfully process a given message
- Scalability
	- Scale consumer instances under high load
- Availability
	- Producer up even if a consumer is down
- Reliability
	- Work is not lost due to insufficient resources
- Decoupling
	- Make changes to consumers without effect on producers worrying about them

## Asynchronous Communication - Push Model - SNS

![](/images/aws/02-Queuing/3-SNS.png)

- Subscribers subscribe to a topic
- Producers send notifications to a topic
	- Notification sent out to all subscribers
- Decoupling
	- Producers don't care about who is listening
- Availability
	- Producer up even if a subscriber is down

## Simple Queuing Service

![](/images/aws/02-Queuing/2-sqs.png)
- Reliable, scalable, fully-managed message queuing service
- High availability
- Unlimited scaling
	- Auto scale to process billions of messages per day
- Low cost (Pay for use)

## Standard and FIFO Queues

![](/images/aws/00-icons/sqs.png)

- Standard Queue 
	- Unlimited throughput
	- BUT NO guarantee of ordering (Best-Effort Ordering) 
	- and NO guarantee of exactly-once processing
		- Guarantees at-least-once delivery (some messages can be processed twice)
- FIFO (first-in-first-out) Queue
	- First-In-First-out Delivery
	- Exactly-Once Processing
	- BUT throughput is lower 
		- Upto 300 messages per second (300 send, receive, or delete operations per second)
		- If you batch 10 messages per operation (maximum), up to 3,000 messages per second 
- Choose
	- Standard SQS queue if throughput is important
	- FIFO Queue if order of events is important

## Sending and receiving a SQS Message - Best case scenario

![](/images/aws/02-Queuing/sqs-simple-flow.png)
- Producer places message on queue 
	- Receives globally unique message ID ABCDEFGHIJ (used to track the message)
- Consumer polls for messages 
	- Receives the message ABCDEFGHIJ along with a receipt handle XYZ
- Message remains in the queue while the consumer processes the message
	- Other consumers will not receive ABCDEFGHIJ even if they poll for messages
- Consumer processes the message successfully 
	- Calls delete message (using receipt handle XYZ)
	- Message is removed from the queue

## Simple Queuing Service Lifecycle of a message
![](/images/aws/02-Queuing/4-Queuing-LifeCycle.png)

Note:
- When a message is sent to queue, it is redundantly distributed among SQS servers

## SQS - Auto Scaling

![](/images/aws/00-icons/sqs.png)
![](/images/arrow.png)
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

- Use target tracking scaling policy 
- Use a SQS metric like ApproximateNumberOfMessages

## SQS Queue - Important configuration
 
| Configuration | Description  | 
|--|:--|
|Visibility timeout| Other consumers will not receive a message being processed for the configured time period (default - 30 seconds, min - 0, max - 12 hours)  <BR/> Consumer processing a message can call ChangeMessageVisibility to increase visibility timeout of a message (before visibility timeout)|
| DelaySeconds   | Time period before a new message is visible on the queue <BR/>Delay Queue = Create Queue + Delay Seconds <BR/>default - 0, max - 15 minutes<BR/>Can be set at Queue creation or updated using SetQueueAttributes<BR/>Use message timers to configure a message specific DelaySeconds value      |
| Message retention period | Maximum period a message can be on the queue <BR/>Default - 4 days, Min - 60 seconds, Max - 14 days|
| MaxReceiveCount | Maximum number of failures in processing a message|

## Simple Queuing Service Security
![](/images/aws/00-icons/sqs.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/iam.png)

- You can provide access to other AWS resources to access SQS using IAM roles (EC2 -> SQS)
- By default only the queue owner is allowed to use the queue
	- Configure SQS Queue Access Policy to provide access to other AWS accounts

## SQS - Certification and Interview Questions

|Scenario | Result |
|--|:--|
|Consumer takes more than visibility timeout to process the message | Message is visible on queue after visibility timeout and another consumer might receive the message|
|Consumer calls ChangeMessageVisibility before visibility timeout | Visibility timeout is extended to requested time|
|DelaySeconds is configured on the queue| Message is delayed for DelaySeconds before it is available|
|Receiver wants to decide how to handle the message without looking at message body | Configure Message Attributes|

## SQS - Certification and Interview Questions

|Scenario | Result |
|--|:--|
|How to reduce number of API calls to SQS?|Use Long Polling - When looking for messages, you can specify a WaitTimeSeconds upto 20 seconds|
|Your receive messages and start processing them after a week. You see that some messages are not processed at all!| Exceeded message retention period. Default message retention period is 4 days. Max 14 days.|
|Give high priority to premium customers| Create separate queues for free and premium customers|

## Amazon Simple Notification Service(SNS)

![](/images/aws/02-Queuing/3-SNS.png)
- Publish-Subscribe (pub-sub) paradigm
- Broadcast asynchronous event notifications
- Simple process
	- Create an SNS Topic
	- Subscribers can register for a Topic
	- When an SNS Topic receives an event notification (from publisher), it is broadcast to all Subscribers
- Use Cases : Monitoring Apps, workflow systems, mobile apps

## Amazon Simple Notification Service(SNS)

![](/images/aws/00-icons/sns.png)

- Provides mobile and enterprise messaging web services
	- Push notifications to Apple, Android, FireOS, Windows devices
	- Send SMS to mobile users
	- Send Emails
- REMEMBER : SNS does not need SQS or a Queue
- You can allow access to other AWS accounts using AWS SNS generated policy

## Amazon MQ
- Managed message broker service for Apache ActiveMQ
- (Functionally) Amazon MQ = Amazon SQS (Queues) + Amazon SNS (Topics)
	- BUT with restricted scalability
- Supports traditional APIs (JMS) and protocols (AMQP, MQTT, OpenWire, and STOMP)
	- Easy to migrate on-premise applications using traditional message brokers
	- Start with Amazon MQ as first step and slowly re-design apps to use Amazon SQS and/or SNS
- Scenario: An enterprise uses AMQP (standard message broker protocol). They want to migrate to AWS without making code changes 
	- Recommend Amazon MQ

# Routing and Content Delivery

## Content Delivery Network

![](/images/aws/aws-edge-locations.png)
- You want to deliver content to your global audience
- Content Delivery Networks distribute content to multiple edge locations around the world
- AWS provides 200+ edge locations around the world
- Provides high availability and performance

## Amazon CloudFront

![](/images/aws/00-icons/cloudfront.png)
- How do you enable serving content directly from AWS edge locations?
	- Amazon CloudFront (one of the options)
- Serve users from nearest edge location (based on user location)
- Source content can be from S3, EC2, ELB and External Websites
- If content is not available at the edge location, it is retrieved from the origin server and cached
- No minimum usage commitment
- Provides features to protect your private content

## Amazon CloudFront

![](/images/aws/00-icons/cloudfront.png)

- Use Cases
	- Static web apps. Audio, video and software downloads. Dynamic web apps
	- Support media streaming with HTTP and RTMP
- Integrates with 
	- AWS Shield to protect from DDoS attacks
	- AWS Web Application Firewall (WAF) to protect from SQL injection, cross-site scripting, etc
- Cost Benefits
	- Zero cost for data transfer between S3 and CloudFront
	- Reduce compute workload for your EC2 instances

## Amazon CloudFront Distribution

![](/images/aws/001-basic-drawings/cloudfrontdistribution.png)
- Create a CloudFront Distribution to distribute your content to edge locations
	- DNS domain name - example abc.cloudfront.com
	- Origins - Where do you get content from? S3, EC2, ELB, External Website
	- Cache-Control
		- By default objects expire after 24 hours
		- Customize min, max, default TTL in CloudFront distribution
		- (For file level customization) Use Cache-Control max-age and Expires headers in origin server
- You can configure CloudFront to only use HTTPS (or) use HTTPS for certain objects
	- Default is to support both HTTP and HTTPS
	- You can configure CloudFront to redirect HTTP to HTTPS

## Amazon CloudFront - Cache Behaviors

![](/images/aws/001-basic-drawings/cloudfrontdistribution.png)
- Configure different CloudFront behavior for different URL path patterns from same origin
	- Path pattern(can use wild cards - `*.php, *.jsp`), 
	- Do you want to forward query strings?
	- Should we use https?
	- TTL

## Amazon CloudFront - Private content

![](/images/aws/001-basic-drawings/cfprivatecontent.png)
- Signed URLs
- Signed cookies using key pairs
- Origin Access Identities(OAI) 
	- Ensures that only CloudFront can access S3
	- Allow access to S3 only to a special CloudFront user

## Amazon CloudFront - Signed URLs and Cookies

![](/images/aws/04-content-delivery/04-SignedUrl.png)

- Signed URLS 
	- RTMP distribution
	- Application downloads (individual files) and 
	- Situations where cookies are not supported
- Signed Cookies 
	- Multiple files (You have a subscriber website)
	- Does not need any change in application URLs

## Amazon CloudFront - Origin Access Identities(OAI)
![](/images/aws/04-content-delivery/03-OAI.png)
- Only CloudFront can access S3
- Create a Special CloudFront user - Origin Access Identities(OAI)
- Associate OAI with CloudFront distribution
- Create a S3 Bucket Policy allowing access to OAI

## Bucket Policy - S3 ONLY through Cloud Front
![](/images/aws/00-icons/user.png)
![](/images/arrow.png)
![](/images/aws/00-icons/cloudfront.png)
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png)	

```
{
    "Version": "2012-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": 
                "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity YOUR_IDENTIFIER"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mybucket/*"
        }
    ]
}
```

![](/images/aws/001-basic-drawings/cloudfrontdistribution.png)
## Amazon CloudFront - Remember
- Old content automatically expires from CloudFront
- Invalidation API - remove object from cache
	- REMEMBER : Designed for use in emergencies
- Best Practice - Use versioning in object path name 
	- Example : /images/profile.png?version=1
	- Prevents the need to invalidated content
- Do not use CloudFront for
	- all requests from single location
	- all requests from corporate VPN
- Scenario: Restrict content to users in certain countries
	- Enable CloudFront Geo restriction
	- Configure White list(countries to be allowed) and Blacklist(countries to be blocked)

## Route 53 

![](/images/aws/00-icons/route53.png) 
- What would be the steps in setting up a website with a domain name (for example, in28minutes.com)?
	- Step I : Buy the domain name in28minutes.com (Domain Registrar)
	- Step II : Setup your website content (Website Hosting)
	- Step III : Route requests to in28minutes.com to the my website host server (DNS)
- Route 53 = Domain Registrar + DNS
	- Buy your domain name
	- Setup your DNS routing for in28minutes.com

## Route 53 - DNS (Domain Name Server)

![](/images/aws/00-icons/route53.png) 

> How should traffic be routed for in28minutes.com?

- Configure Records:
	- Route api.in28minutes.com to the IP address of api server
	- Route static.in28minutes.com to the IP address of http server
	- Route email (ranga@in28minutes.com) to the mail server(mail.in28minutes.com)
	- Each record is associated with a TTL (Time To Live) - How long is your mapping cached at the routers and the client?

## Route 53 Hosted Zone

![](/images/aws/00-icons/route53.png) 
- Container for records containing DNS records routing traffic for a specific domain
- I want to use Route 53 to manage the records (Name Server) for in28minutes.com
	- Create a hosted zone for in28minutes.com in Route 53
- Hosted zones can be
	- private - routing within VPCs
	- public - routing on internet
- Manage the DNS records in a Hosted Zone

## Standard DNS Records

![](/images/aws/dns-record-types.png)

- A - Name to IPV4 address(es)
- AAAA - Name to IPV6 address(es )
- NS - Name Server containing DNS records
	- I bought in28minutes.com from GoDaddy (Domain Registrar)
	- BUT I can use Route 53 as DNS
		- Create NS records on GoDaddy 
		- Redirect to Route 53 Name Servers
- MX - Mail Exchange
- CNAME - Name1 to Name2

## Route 53 Specific Extension - Alias records

![](/images/aws/00-icons/route53.png) 

- Route traffic to selected AWS resources 
	- Elastic Beanstalk environment
	- ELB load balancer
	- Amazon S3 bucket
	- CloudFront distribution 
- Alias records can be created for 
	- root(in28minutes.com) and 
	- non root domains(api.in28minutes.com) 
- COMPARED to CNAME records which can only be created for 
	- non root domains (api.in28minutes.com)

## Route 53 - Routing

![](/images/aws/route53-routing.png)

- Route 53 can route across Regions
	- Create ALBs in multiple regions and route to them!
	- Offers multiple routing policies

## Route 53 Routing Policies 
 
| Policy | Description  | 
|--|:--|
| Simple | Maps a domain name to (one or more) IP Addresses|
|Weighted | Maps a single DNS name to multiple weighted resources <BR/>10% to A, 30% to B, 60% to C (useful for canary deployments)|
|Latency |Choose the option with minimum latency <BR/>Latency between hosts on the internet can change over time|
|Failover | Active-passive failover. <BR/>Primary Health check fails (optional cloud Watch alarm) => DR site is used|
|Geoproximity| Choose the nearest resource (geographic distance) to your user. Configure a bias.|
|Multivalue answer |Return multiple healthy records (upto 8) at random <BR/>You can configure an (optional) health check against every record|
|Geolocation | Choose based on the location of the user|

## Route 53 Routing Policies - Geolocation

![](/images/aws/00-icons/route53.png) 

- Choose based on the location of the user 
	- continent, country or a (state in USA) 
	- Send traffic from Asia to A
	- Send traffic from Europe to B etc. 
- Record set for smallest geographic region has priority
- Use case 
	- Restrict distribution of content to specific areas where you have distribution rights
- (RECOMMENDED) Configure a default policy (used if none of the location records match)
	- Otherwise, Route 53 returns a "no answer" if none of the location records match

## Need for AWS Global Accelerator

![](/images/aws/04-content-delivery/01-content-delivery.png)
- Cached DNS answers 
	- clients might cache DNS answers causing a delay in propagation of configuration updates
- High latency 
	- users connect to the region over the internet

## AWS Global Accelerator

![](/images/aws/04-content-delivery/02-global-accelerator.png)
- Directs traffic to optimal endpoints over the AWS global network
- Global Accelerator provides you with two static IP addresses
- Static IP addresses are anycast from the AWS edge network
	- Distribute traffic across multiple endpoint resources in multiple AWS Regions
- Works with Network Load Balancers, Application Load Balancers, EC2 Instances, and Elastic IP addresses

# ETL & Big Data <BR/> Redshift and EMR

## Amazon Redshift

![](/images/aws/00-icons/redshift.png) 

- Redshift is a relational database ( tables and relationships)
- What is the need for another relational database? 
	- RDS is optimized for online transaction processing
	- It is optimized to provide a balance between both reads and write operations
- OLAP workloads have exponentially larger reads on the databases compared to writes: 
	- Can we use a different approach to design the database? 
	- How about creating a cluster and splitting the execution of the same query across several nodes? 
- Redshift is a **petabyte-scale distributed data ware house** based on PostgreSQL

## Amazon Redshift 

![](/images/aws/00-icons/redshift.png) 

- Three important characteristics of Redshift:
	- Massively parallel processing (MPP) - storage and processing can be split across multiple nodes
	- Columnar data storage
	- High data compression
- As a result
	- A single row of data might be stored across multiple nodes
	- A query to Redshift leader node is distributed to multiple compute nodes for execution
- Start with a single node configuration and scale to multi node configuration
- You can dynamically add and remove nodes

## Amazon Redshift 

![](/images/aws/00-icons/redshift.png) 
- Used for traditional ETL(Extract, Transform, Load), OLAP and Business Intelligence (BI) use cases
	- Optimized for high-performance analysis and reporting of very large datasets
- Supports standard SQL 
- Integration with data loading, reporting, mining and analytics tools
- Provides high availability and durability:
	- Automatic replication (maintains 3 copies of your data)
	- Automated backups (to S3. Default retention - 1 day. Max - 35 days)
	- Automatic recovery from any node failures

## Redshift Cluster

![](/images/aws/Redshift-NodeRelationships.png) 
https://docs.aws.amazon.com/redshift/latest/dg/images/02-NodeRelationships.png 
- One leader node and multiple compute nodes
	- Add compute nodes for more performance
	- Create a cluster subnet group to use a VPC
- One or more databases in a cluster
- Clients communicate with leader node
	- Leader node divides the query execution between compute nodes
	- No direct access to compute nodes
	

## Redshift - Designing Tables

![](/images/aws/00-icons/redshift.png) 
- Compression Encoding (optional) 
	- Let Redshift choose or configure for each column
		- Examples : Raw, Bytedict, LZO, Runlength, Text255, Text32K
	- Find the right compression encoding by running tests
- Sort Keys (optional) 
	- Data is stored in sorted order (using sort key)
	- Increase efficiency of your queries
	- Example 1 : Columns used frequently in range (year > 1995 and year < 2005) or equal (year = 2015) conditions
	- Example 2 : Join columns with other tables 
	- Example 3 : Timestamp columns if you use the most recent data frequently

## Redshift - Designing Tables - Distribution Strategy

![](/images/aws/00-icons/redshift.png) 

- How are the rows of the table distributed across compute nodes? 
	- Aim to distribute data equally across nodes and minimize data movement during query execution
- EVEN (default) - data is uniformly distributed
- KEY - based on values of one column
	- Matching values are stored close together
	- Use join columns as KEY if you want matching columns to be co-located
- ALL - entire table on all nodes
	- Used for lookup tables

## Loading Data into Amazon Redshift

| Scenario | Solution  | 
|--|:--|
|Simple |Use SQL insert queries using ODBC or JDBC|
|Efficient|Use Amazon Redshift COPY command to load data from Amazon S3, Amazon DynamoDB, Amazon EMR etc|
|Data Pipelines |Load using AWS Data Pipeline|
|On-premises data|Use Storage Gateway or Import/Export to import data into S3. COPY data from S3|
|Other databases|AWS Database Migration Service : RDS, DynamoDB or another Amazon Redshift Database|
|Recommendation| Prefer COPY over INSERT for bulk operations as COPY is done in parallel|
|Recommendation| Prefer COPY from multiple files. Split large files into multiple small input files|

## Redshift Workload Management

![](/images/aws/rds-diagrams/xx-redshift-wlm.png)
- WLM can be configured to prioritize queues
- Create multiple queues with different concurrency level for different purposes
- One queue for long running queries with low concurrency
- One queue for short running queries with high concurrency (upto 50 concurrent queries)

## Redshift Security
![](/images/aws/00-icons/redshift.png)
![](/images/arrow.png)
![](/images/aws/00-icons/kms.png)
- Uses 4-tier, key-based architecture for encryption
	- master key (chosen from keys in KMS)
	- a cluster encryption key (CEK)
	- a database encryption key (DEK)
	- and data encryption keys
- Manage keys using AWS KMS or AWS Cloud HSM
- IAM to manage user permissions for cluster operations
	- Grant permissions on a per cluster basis instead of per table basis

## Redshift Operations
![](/images/aws/00-icons/redshift.png)
![](/images/aws/00-icons/cloudwatch.png)
- Add new columns by using ALTER TABLE
	- Existing columns cannot be modified
- SQL operations are logged
	- Use SQL queries to query against system tables or download to S3
- Monitor performance & queries with Cloud Watch and Redshift web console
- When deleting a Redshift cluster, take a final snapshot to Amazon S3

## Amazon Redshift Spectrum

![](/images/aws/001-basic-drawings/redshift-spectrum.png)
- Run SQL queries against datasets in Amazon S3 
	- Does need for any intermediate data stores
- Auto scales based on your queries
- Scale storage and compute independently
- Metadata defined in Amazon Redshift
	- Avro, CSV, Ion, JSON, ORC, Parquet formats supported
- Eliminate expensive data transfers from S3 to data warehousing solutions (Cost effective)
- Integrates with Amazon Athena
- Query against Amazon EMR (as well)

## Amazon EMR - Elastic MapReduce
- Managed Hadoop service with high availability and durability
- EMR gives access to underlying OS => You can SSH into it
- Important tools in Hadoop eco system are natively supported:
	- Examples: Pig, Hive, Spark or Presto
- Install others using bootstrap actions
- Use cases 
	- Log processing for insights
	- Click stream analysis for advertisers
	- Genomic and life science dataset processing

## Amazon EMR - Storage Types
 
| Feature |Hadoop Distributed File System (HDFS)  | EMR File System (EMRFS) | 
|--|:--|:--|
|  Standard for Hadoop  |   ✓    |    X     |
|  Data Storage   |   EBS or instance storage     |    S3    |
|  Data Survival on cluster shutdown| Yes for EBS. No for Instance Storage| Yes|
|Persistent Clusters running 24 X 7 analysis| ✓ (low latency on instance storage)||
|Transient Clusters running Infrequent big data jobs||✓(Run MapReduce jobs against S3 bucket)|

## Amazon Redshift and EMR Alternatives

| Alternative | Scenario  | 
|--|:--|
| Amazon EMR | For big data frameworks like Apache Spark, Hadoop, Presto, or Hbase to do large scale data processing that needs high customization <BR/> For example: machine learning, graph analytics etc|
| Amazon Redshift | Run complex queries against data warehouse - housing structured and unstructured data pulled in from a variety of sources |
| Amazon Redshift Spectrum | Run queries directly against S3 without worrying about loading entire data from S3 into a data warehouse|
| Amazon Athena | Quick ad-hoc queries without worrying about provisioning a compute cluster (serverless) <BR/> Amazon Redshift Spectrum is recommended if you are executing queries frequently against structured data|

# Handling Workflows

## Amazon Simple Workflow Service (SWF)

![](/images/aws/00-icons/swf.png) 
- Build and run background jobs with
	- parallel or sequential steps
	- synchronously or asynchronously
	- with human inputs (can indefinitely wait for human inputs)
- (Use cases) Order processing and video encoding workflows
- A workflow can start when receiving an order, receiving a request for a taxi
- Workflows can run upto 1 year
- Deciders and activity workers can use long polling

## Amazon SWF - Order Process

![](/images/aws/swf-overview.png) 
https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-actors.html
- Key Actors : Workflow starter, Decider and Activity worker
- Workflow starter calls SWF action to start workflow 
	- Example: when an order is received
- SWF receives request and schedules a decider
	- Decider receives the task and returns decision to SWF: 
		- For example, schedule an activity "Activity 1"
	- SWF schedules "Activity 1"
	- Activity worker performs "Activity 1". Returns result to SWF.
	- SWF updates workflow history. Schedules another decision task.
	- Loop continues until decider returns decision to close workflow
- SWF archives history and closes workflow

# Handling Data Streams

## Streaming Data

![](/images/datastream.png) 
- Imagine implementing analytics for a website:
	- You have a continuous stream of data (page views, link clicks etc)
- Characteristics of streaming data:
	- Continuously generated
	- Small pieces of data
	- Sequenced - mostly associated with time
- How do your process continuous streaming data originating from application logs, social media applications?

## S3 Notifications

![](/images/aws/00-icons/s3bucket.png)
![](/images/arrow.png)
![](/images/aws/00-icons/lambdafunction.png)
- Send notifications to SNS, SQS, trigger lambda functions on 
	- creation, deletion or update of an S3 object
- Setup at bucket level
	- You can use prefix and suffix to configure
- Cost efficient for simple use cases
	- S3 notification -> Lambda
	- Almost negligible cost (storage for file + invocation)

## DynamoDB Streams
![](/images/aws/001-basic-drawings/dynamodbstreams.png)
- Each event from DynamoDB (in time sequenced order) is buffered in a stream near real-time
- Can be enabled or disabled
- Use case - Send email when user registers
	- Tie a Lambda function to DynamoDB Streams
- Stream allow iteration through records (**last 24 hours**)

## Amazon Kinesis

![](/images/datastream.png) 
- Handle streaming data
	- NOT recommended for ETL Batch Jobs
- Amazon Kinesis Data Streams
	- Process Data Streams
- Amazon Kinesis Firehose
	- Data ingestion for streaming data : S3, Elasticsearch etc
- Amazon Kinesis Analytics
	- Run queries against streaming data
- Amazon Kinesis Video Streams
	- Monitor video streams

## Amazon Kinesis Data Streams

![](/images/aws/02-Queuing/4-kinesis-streams.png)
- Limitless Real time stream processing 
	- Sub second processing latency
- Alternative for Kafka
- Supports multiple clients
	- Each client can track their stream position
- Retain and replay data (max 7 days & default 1 day)

## Amazon Kinesis Data Streams - Integrations

![](/images/aws/02-Queuing/4-kinesis-streams.png)
	
- Use application integrations to generate streams
	- Toolkits : AWS SDK, AWS Mobile SDK, Kinesis Agent
	- Service Integrations : AWS IOT, CloudWatch Events and Logs
- Process streams using Kinesis Stream Applications 
	- Run on EC2 instances
	- Written using Kinesis Data Streams APIs

## Amazon Kinesis Data Firehose

![](/images/aws/02-Queuing/5-kinesis-firehose.png)
- Data ingestion for streaming data
	- Receive
	- Process ( transform - Lambda, compress, encrypt ) 
	- Store stream data to S3, Elasticsearch, Redshift and Splunk
- Use existing analytics tools based on S3, Redshift and Elasticsearch
- Pay for volume of data ingested (Serverless)

## Amazon Kinesis Analytics
![](/images/aws/02-Queuing/5-kinesis-analytics.png)
- You want to continuously find active number of users on a website in the last 5 minutes based on streaming website data
- With Amazon Kinesis Analytics, you can write SQL queries and build Java applications to continuously analyze your streaming data

## Amazon Kinesis Video Streams
![](/images/aws/02-Queuing/5-kinesis-video-streams.png)
- Monitor video streams from web-cams 
- Examples: traffic lights, shopping malls, homes etc
- Integrate with machine learning frameworks to get intelligence

# AWS Data Lakes

## AWS Data Lakes - Simplified Big Data Solutions

![](/images/aws/data-lake-architecture.png)
- Usual big data solutions are complex
- How can we make collecting, analyzing (reporting, analytics, machine learning) and visualizing huge data sets easy? 
- How to design solutions that scale? 
- How to build flexibility while saving cost?
- Data Lake 
	- Single platform with combination of solutions for data storage, data management and data analytics

## AWS Data Lakes - Storage and Ingestion
![](/images/aws/00-icons/kinesisfirehose.png)
![](/images/aws/00-icons/snowball.png)
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png)
![](/images/aws/00-icons/glacier.png)

- Storage
	- Amazon S3 and S3 Glacier provide an ideal storage solution for data lakes
- Data Ingestion
	- Streaming data - Amazon Kinesis Firehose
		- Transform and store to Amazon S3
		- Transformation operations - compress, encrypt, concatenate multiple records into one (to reduce S3 transactions cost) and execute lambda functions 
	- Bulk data from on-premises - AWS Snowball
	- Integrate on-premises platforms with Amazon S3 - AWS Storage Gateway

## Amazon S3 Query in Place

![](/images/aws/00-icons/athena.png) 
![](/images/aws/00-icons/redshift.png) 
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png)
![](/images/aws/00-icons/glacier.png)	

- Run your analytics directly from Amazon S3 and S3 Glacier
- S3 Select and Glacier Select
	- SQL queries to retrieve subset of data
		- Supports CSV, JSON, Apache Parquet formats
	- Build serverless apps connecting S3 Select with AWS Lambda
	- Integrate into big data workflows 
		- Enable Presto, Apache Hive and Apache Spark frameworks to scan and filter data
- Amazon Athena
	- Direct ad-hoc SQL querying on data stored in S3
	- Uses Presto and supports CSV, JSON,  Apache Parquet and Avro
- Amazon Redshift Spectrum 
	- Run queries directly against S3 without loading complete data from S3 into a data warehouse
	- Recommended if you are executing queries frequently against structured data

## Amazon S3 Query in Place - Recommendations
- You want to get quick insights from your cold data stored in S3 Glacier. You want to run queries against archives stored in S3 Glacier without restoring the archives.
	- Use S3 Glacier Select to perform filtering and basic querying using SQL queries 
	- Stores results in S3 bucket
	- No need to temporarily stage data and then run queries
- Recommendations:
	- Store data in Amazon S3 in Parquet format
		- Reduce storage (upto 85%) and improve querying (upto 99%) compared to formats like CSV, JSON, or TXT
	- Multiple compression standards are supported BUT GZIP is recommended
		- Supported by Amazon Athena, Amazon EMR and Amazon Redshift

## AWS Data Lakes -  Analytics with data in S3 Data Lake
 
| Service | Description  | 
|--|:--|
| Amazon EMR | EMR integrates well with Amazon S3 - Use big data frameworks like Apache Spark, Hadoop, Presto, or Hbase. For example: machine learning, graph analytics etc|
|Amazon Machine Learning (ML)|Create and run models for predictive analytics and machine learning (using data from Amazon S3, Amazon Redshift, or Amazon RDS)|
| Amazon QuickSight |For visualizations (using data from Amazon Redshift, Amazon RDS, Amazon Athena, and Amazon S3)|
|Amazon Rekognition | Build image recognition capabilities around images stored in Amazon S3. <BR/>Example use case : Face based verification|

## AWS Data Lakes -  Data Cataloging

![](/images/aws/data-cataloging.png) 
https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-cataloging.html
- 1 : What data (or assets) is stored?
- 2 : What is the format of data?
- 3 : How is the data structured?
- Question 1 - Stored in comprehensive data catalog
- Questions 2 and 3 - Stored using a Hive Meta store Catalog (HCatalog)
- AWS Glue also supports storing HCatalog

##  AWS Glue

![](/images/aws/00-icons/glue.png)

- Fully managed extract, transform, and load (ETL) service
- Simplify data preparation (capturing metadata) for analytics: 
	- Connect AWS Glue to your data on AWS (Aurora, RDS, Redshift, S3 etc)
	- AWS Glue creates a AWS Glue Data Catalog with metadata abstracted from your data
	- Your data is ready for searching and querying
- Run your ETL jobs using Apache Spark
- Metadata from AWS Glue Data Catalog can be used from:
	- Amazon Athena
	- Amazon EMR
	- Amazon Redshift Spectrum

# More Serverless

## Serverless Options - Compute
![](/images/aws/00-icons/lambda.png)
- AWS Lambda
	- Run code without provisioning servers! 
	- Also called FAAS (Function as a Service)
- Lambda@Edge
	- Run lambda functions at AWS Edge Locations
	- Integrated with CloudFront
- AWS Fargate
	- Container Orchestration without worrying about ec2 instances

## Serverless Options - Storage
![](/images/aws/00-icons/s3.png)
![](/images/aws/00-icons/efs.png)  
- Amazon S3 
	- Highly scalable object storage
	- We've talking sufficiently about it already!
- Amazon Elastic File System 
	- Elastic file storage for UNIX compatible systems

![](/images/aws/00-icons/dynamodb.png) 
## Serverless Options - Databases
- Amazon DynamoDB
	- Fast, scalable, distributed and flexible non-relational (NoSQL) database service for any scale
	- Need to configure read and write capacity for tables 
		- NOT truly serverless BUT don't tell that to AWS
		- Truly serverless mode is expensive
- Amazon Aurora Serverless
	- Use Amazon RDS with Aurora in serverless mode
	- WARNING : I would still consider this early stage
- Amazon RDS Proxy 
	- Sits between client applications (including lambdas) and your RDS database
	- Efficient management of short lived database connections (by pooling database connections)

## Serverless Options - API Proxy and Orchestration
![](/images/aws/00-icons/apigateway.png) 
![](/images/aws/00-icons/stepfunctions.png) 
- Amazon API Gateway
	- API Management platform helping you create, publish, maintain, monitor and secure your APIs
	- Provides authorization, rate limiting and versioning
- AWS Step Functions  
	- Setup workflows involving services like AWS Lambda and AWS Fargate
	- Orchestration and state management

## Serverless Options - Application Integration and Analytics

![](/images/aws/00-icons/sns.png) 
![](/images/aws/00-icons/sqs.png) 
![](/images/aws/00-icons/kinesis.png) 
![](/images/aws/00-icons/athena.png) 
- Amazon SNS
	- Follows “publish-subscribe” (pub-sub) messaging paradigm to broadcast asynchronous event notifications - SMS, e-mails, push notifications etc
- Amazon SQS
	- Fully managed queuing service
	- Helps you decouple your applications
- Amazon Kinesis
	- Multiple solutions to process streaming data
- Amazon Athena
	- Query using SQL on data in Amazon S3
	- Pay only for queries!

## Serverless Options - Others
![](/images/aws/00-icons/cognito.png) 
- Amazon Cognito
	- Fully managed solution providing authorization and authentication solutions for web/mobile apps
- AWS Serverless Application Model
	- Open source framework for building serverless applications

## Serverless Use case 1 - Full Stack Web Application
![](/images/aws/03-serverless/01-serverless.png)
- Static content stored in S3
- API Gateway and Lambda are used for the REST API
- DynamoDB is used to store your data

## Serverless Use case 2 - Real time event processing

![](/images/aws/03-serverless/02-realtime-processing.png)
- User uploads videos to S3
- S3 notifications are used to invoke Lambda functions to optimize videos for different devices.


## Amazon Cognito

![](/images/aws/00-icons/cognito.png) 
- Want to quickly add a sign-up page and authentication for your mobile and web apps?
- Want to integrate with web identity providers (example: Google, Facebook, Amazon) and provide a social sign-in?
- Do you want security features such as multi-factor authentication (MFA), phone and email verification?
- Want to create your own user database without worrying about scaling or operations?
- Let's go : Amazon Cognito
- Support for SAML

## Amazon Cognito - User Pools

![](/images/aws/00-icons/cognito.png) 
- Do you want to create your own secure and scalable user directory?
- Do you want to create sign-up pages?
- Do you want a built-in, customizable web UI to sign in users (with option to social sign-in )?
- Create a user pool

## Amazon Cognito - Identity pools
![](/images/aws/cognito-identity-pools.png)
- Identity pools provide AWS credentials to grant your users access to other AWS services
- Connect identity pools with authentication (identity) providers 
	- Your own user pool OR
	- Amazon, Apple, Facebook, Google+, Twitter OR
	- OpenID Connect provider OR
	- SAML identity providers (SAML 2.0)
- Configure multiple authentication (identity) providers for each identity pool
- Federated Identity 
	- An external authentication (identity) provider
	- ex: Amazon, Apple, Facebook, OpenID or SAML identity providers
	

## Amazon Cognito - How does it work?

![](/images/aws/03-serverless/05-cognito.png)
- Application sends user credentials to identity provider
	- (If authenticated) Identity provider sends a token to application
- Application sends the token to Identity Pool
	- (If valid token) Identity Pool creates temporary credentials (access key, secret key, and session token) using STS
- App sends a request with the credentials to the AWS service

## Lambda@Edge
- Run lambda functions at AWS Edge Locations 
	- Lowest network latency for end users
- Use cases : Search Engine Optimization, A/B Testing, Dynamically routing to different origins
- Can be triggered on these Amazon CloudFront events:
	- Viewer Request - when request arrives at edge location
	- Origin Request - Just before sending request to origin (when object is not in cache)
	- Origin Response - After the edge location receives response from origin
	- Viewer Response - Just before a response is sent back from edge location
- LIMITATION : Supports ONLY Node.js and Python programming languages
- LIMITATION : No free tier and more expensive than Lambda

## Serverless Application Model
- 1000s of Lambda functions to manage, versioning, deployment etc 
- Serverless projects can become a maintenance headache
- How to test serverless projects with Lambda, API Gateway and DynamoDB in your local?
- How to ensure that your serverless projects are adhering to best practices?
	- Tracing (X-Ray), CI/CD(CodeBuild, CodeDeploy, CodePipeline) etc
- Welcome SAM - Serverless Application Model
	- Open source framework for building serverless applications
	- Define a YAML with all the serverless resources you want:
		- Functions, APIs, Databases etc
	- BEHIND THE SCENES : Your configuration is used to create a AWS CloudFormation syntax to deploy your application

## AWS AppSync

![](/images/aws/001-basic-drawings/appsync.png)
- We are in multi device world
	- Want to synchronize app data across devices?
	- Want to create apps which work in off-line state?
	- Want to automatically sync data once user is back online?
- Welcome AWS AppSync
- Based on GraphQL
- App data can be accessed from anywhere 
	- NoSQL data stores, RDS or Lambda
- (Alternative) Cognito Sync is limited to storing simple key-value pairs
	- AppSync recommended for almost all use cases

## AWS Step Functions 

![](/images/aws/00-icons/stepfunctions.png) 
- Create a serverless workflow in 10 Minutes using a visual approach
- Orchestrate multiple AWS services into serverless workflows:
	- Invoke an AWS Lambda function
	- Run an Amazon Elastic Container Service or AWS Fargate task
	- Get an existing item from an Amazon DynamoDB table or put a new item into a DynamoDB table
	- Publish a message to an Amazon SNS topic
	- Send a message to an Amazon SQS queue
- Build workflows as a series of steps:
	- Output of one step flows as input into next step
	- Retry a step multiple times until it succeeds
	- Maximum duration of 1 year

## AWS Step Functions 

![](/images/aws/00-icons/stepfunctions.png) 
- Integrates with Amazon API Gateway
	- Expose API around Step Functions
	- Include human approvals into workflows
- (Use case) Long-running workflows 
	- Machine learning model training, report generation, and IT automation
- (Use case) Short duration workflows 
	- IoT data ingestion, and streaming data processing
- (Benefits) Visual workflows with easy updates and less code
- (Alternative) Amazon Simple Workflow Service (SWF) 
	- Complex orchestration code  (external signals,  launch child processes)
- Step Functions is recommended for all new workflows UNLESS you need to write complex code for orchestration

# Extend and Secure Your VPCs - In AWS and To On-Premises

## VPC Peering

![](/images/aws/vpc-peering.png)
- Connect VPCs belonging to same or different AWS accounts irrespective of the region of the VPCs
- Allows private communication between the connected VPCs
- Peering uses a request/accept protocol
	- Owner of requesting VPC sends a request 
	- Owner of the peer VPC has one week to accept
- Remember : Peering is not transitive
- Remember : Peer VPCs cannot have overlapping address ranges

## VPC Endpoint 

![](/images/aws/00-icons/vpcendpoint.png)
- Securely connect your VPC to another service
- Gateway endpoint	
	- Securely connect to Amazon S3 and DynamoDB
	- Endpoint serves as a target in your route table for traffic
	- Provide access to endpoint (endpoint, identity and resource policies)
- Interface endpoint
	- Securely connect to AWS services EXCEPT FOR Amazon S3 and DynamoDB
	- Powered by PrivateLink (keeps network traffic within AWS network)
	- Needs a elastic network interface (ENI) (entry point for traffic)
- (Avoid DDoS & MTM attacks) Traffic does NOT go thru internet
- (Simple) Does NOT need Internet Gateway, VPN or NAT

## VPC Flow Logs

![](/images/aws/00-icons/vpcflowlogs.png) 
- Monitor network traffic 
- Troubleshoot connectivity issues (NACL and/or security groups misconfiguration)
- Capture traffic going in and out of your VPC (network interfaces)
- Can be created for 
	- a VPC
	- a subnet
	- or a network interface (connecting to ELB, RDS, ElastiCache, Redshift etc)
- Publish logs to Amazon CloudWatch Logs or Amazon S3
- Flow log records contain ACCEPT or REJECT 
	- Is traffic is permitted by security groups or network ACLs?

## Troubleshoot using VPC Flow Logs 

![](/images/aws/00-icons/user.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/nacl.png)
![](/images/aws/00-icons/subnet.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/securitygroup.png)
![](/images/aws/00-icons/ec2.png)

- Inbound traffic rules - NACL IN, SG IN, NACL OUT (SG OUT NOT checked)
	- If inbound request is rejected, SG or NACL could be mis-configured
	- If outbound response is rejected, NACL is mis-configured
- Outbound traffic rules - SG OUT, NACL OUT, NACL IN (SG IN NOT checked)
	- If outbound request is rejected, SG or NACL could be mis-configured
	- If inbound response is rejected, NACL is mis-configured
- Problem with response => Problem with NACL
- Problem with request could be problems with NACL or SG

## AWS and On-Premises - Overview

![](/images/aws/Aws-Onpremises-01.png)
- AWS Managed VPN 
	- IPsec VPN tunnels from  VPC to customer network
- AWS Direct Connect (DX)
	- Private dedicated network connection from on-premises to AWS

## AWS Managed VPN

![](/images/aws/001-basic-drawings/sitetositevpn.png)
- IPsec VPN tunnels from  VPC to customer network
- Traffic over internet - encrypted using IPsec protocol
- VPN gateway to connect one VPC to customer network
- Customer gateway installed in customer network
	- You need a Internet-routable IP address of customer gateway

## AWS Direct Connect (DC)

![](/images/aws/00-icons/datacenter.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/directconnect.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/aws.png)	
- Private dedicated network connection from on-premises to AWS
- Advantages:
	- Private network 
	- Reduce your (ISP) bandwidth costs
	- Consistent Network performance because of private network
- Connection options:
	- Dedicated: Dedicated 1 Gbps or 10 Gbps network connections
	- Hosted: Shared 50Mbps to 10 Gbps network connections
- (REMEMBER) Establishing DC connection can take more than a month
- (REMEMBER) Establish a redundant DC for maximum reliability
- (REMEMBER) Direct Connect DOES NOT encrypt data (Private Connection ONLY)

## AWS Direct Connect Plus VPN

![](/images/aws/aws-direct-connect-vpn.png)
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-plus-vpn-network-to-amazon.html

- IPsec Site-to-Site VPN tunnel from an direct connect location to customer network
- Traffic is encrypted using IPsec protocol

## Software VPN

![](/images/aws/aws-software-vpn.png)
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-vpn-cloudhub-network-to-amazon.html
- Provides flexibility to fully manage both sides of your Amazon VPC connectivity
- Run software VPN appliance in your VPC
- Recommended for compliance - You need to manage both sides of connection
- Recommended when you use gateway devices which are not supported by Amazon VPN solution
- You are responsible for patches and updates to Software VPN appliance
- Software VPN appliance becomes a Single Point of Failure 

## AWS VPN CloudHub

![](/images/aws/aws-vpn-cloudhub.png) 
https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-vpn-cloudhub-network-to-amazon.html
- Use either VPN or AWS Direct Connect to setup connectivity between multiple branch offices
- Operates on a simple hub-and-spoke model 
- Uses Amazon VPC virtual private gateway with multiple gateways

## VPC Connections - Review
- VPC peering: Connect to other VPCs
- NAT gateways: Allow internet traffic from private subnets
- Internet gateway: Connect to internet
- AWS Direct Connect: Private pipe to on-premises
- AWS VPN: Encrypted (IPsec) tunnel over internet to on-premises

# Moving Data between AWS and On-premises

## Amazon S3 Transfer Acceleration

![](/images/aws/01-S3/1-S3-EdgeLocation.png)
- Most basic option when you are transferring less data (upto a few terabytes) into S3
- Uses Amazon CloudFront's Edge Locations to enable fast transfer of files to/from your clients
- Enable S3 Transfer Acceleration and use endpoints 
	- s3-accelerate.amazonaws.com or 
	- .s3-accelerate.dualstack.amazonaws.com

## AWS Snowball

![](/images/aws/01-S3/8-snowball.png)
- Transfer dozens of terabytes to petabytes of data from on-premises to AWS
- 100TB (80 TB usable) per appliance
	- If needed, request multiple appliances
- Involves physical shipping
- Simple Process 
	- Request for Snowball
	- Copy data 
	- Ship it back
- Manage jobs with AWS Snowball console
- Data is automatically encrypted with KMS (AES-256)

## AWS Snowball

![](/images/aws/00-icons/snowball.png) 
- Current versions of AWS Snowball use Snowball Edge devices 
	- Provide both compute and storage
	- Pre-process data (using Lambda functions)
- Choose between 
	- Storage optimized (24 vCPUs, 32 GiB RAM)
	- Compute optimized(52 vCPUs, 208 GiB RAM)
	- Compute optimized with GPU
- Choose Snowball if direct transfer takes over a week
	- 5TB can be transferred on 100Mbps line in a week at 80% utilization

## AWS Snowmobile
![](/images/aws/snowmobile.jpeg)
- How do I transfer dozens of petabytes to exabytes of data from on-premises to AWS for cloud migration?
- 100PB storage per truck
- If needed, use multiple trucks in parallel
- Data is automatically encrypted with KMS (AES-256)

## AWS DataSync - Transfer File Storage to Cloud
- Secure and 10x faster (100s of TB) data transfers from/to AWS over internet or AWS Direct Connect
- Transfer from onpremise file storage (NFS, SMB) to S3, EFS or FSx for Windows
- Monitor progress using Amazon CloudWatch
- (Use cases) Data Migration, Data replication and Cold data archival
- (Alternative) Use AWS Snowball if you are bandwidth constrained or transferring data from remote, or disconnected 
- (Alternative) Use S3 Transfer Acceleration when your applications are integrated with S3 API. If not, prefer AWS DataSync(Supports multiple destinations, built-in retry)
- (Integration) Migrate data using DataSync and use AWS Storage Gateway for ongoing updates from on-premises applications

## AWS Data Pipeline
![](/images/aws/01-S3/9-datapipeline.png)
- Process and move data (ETL) between S3, RDS, DynamoDB, EMR, On-premise data sources
- Create complex data processing workloads that are fault tolerant, repeatable, and highly available
- Launches required resources and tear them down after execution
- REMEMBER : NOT for streaming data!

## AWS Database Migration Service
![](/images/aws/00-icons/datacenter.png)
![](/images/arrow.png)
![](/images/aws/00-icons/aws.png)

- Migrate databases to AWS while keeping source databases operational
	- Homogeneous Migrations (ex: Oracle to Oracle)
	- Heterogeneous Migrations (ex: Oracle to Amazon Aurora, MySQL to Amazon Aurora)
- Free for first 6 months when migrating to  Aurora,  Redshift or  DynamoDB
- (AFTER MIGRATION) Keep databases in sync and pick right moment to switch
- (Use case) Consolidate multiple databases into a single target database
- (Use case) Continuous Data Replication can be used for Disaster Recovery

## AWS Schema Conversion Tool

![](/images/aws/00-icons/database.png) 

- Migrate data from commercial databases and data warehouses to open source or AWS services
	- Preferred option for migrating data warehouse data to Amazon Redshift
- Migrate database schema (views, stored procedures, and functions) to compatible targets
- Features:
	- SCT assessment report 
		- Analyze a database to determine the conversion complexity
	- Update source code (update embedded SQL in code)
	- Fan-in (multiple sources - single target) 
	- Fan-out (single source - multiple targets)

## Database Migration Service VS Schema Conversion Tool
![](/images/aws/00-icons/datacenter.png)
![](/images/arrow.png)
![](/images/aws/00-icons/aws.png)
- (Remember) SCT is part of DMS service
- DMS is preferred for homogeneous migrations
- SCT is preferred when schema conversion are involved
- DMS is for smaller workloads (less than 10 TB) 
- SCT preferred for large data warehouse workloads
	- Prefer SCT for migrations to Amazon Redshift
- Only DMS provides continuous data replication after migration

# DevOps

## DevOps
![](/images/aws/devops-06-teams.png)
- Getting Better at "**Three Elements of Great Software Teams**"
	- Communication - Get teams together
	- Feedback - Earlier you find a problem, easier it is to fix
	- Automation - Automate testing, infrastructure provisioning, deployment, and monitoring

## DevOps - CI, CD

![](/images/aws/devops-05-continuous-delivery.png) 
- Continuous Integration 
	- Continuously run your tests and packaging
- Continuous Deployment 
	- Continuously deploy to test environments
- Continuous Delivery 
	- Continuously deploy to production

## DevOps - CI, CD Tools
![](/images/aws/00-icons/codecommit.png) 
![](/images/aws/00-icons/codepipeline.png) 
![](/images/aws/00-icons/codebuild.png) 
![](/images/aws/00-icons/codedeploy.png) 
- AWS CodeCommit - Private source control (Git)
- AWS CodePipeline - Orchestrate CI/CD pipelines
- AWS CodeBuild - Build and Test Code (application packages and containers)
- AWS CodeDeploy - Automate Deployment (EC2, ECS, Elastic Beanstalk, EKS, Lambda etc)

## DevOps - IAAC
![](/images/aws/devops-06-iaac-2-overview.png) 

- Treat infrastructure the same way as application code
- Track your infrastructure changes over time (version control)
- Bring repeatability into your infrastructure
- Two Key Parts
	- Infrastructure Provisioning 
		- Provisioning compute, database, storage and networking
		- Open source cloud neutral - Terraform
		- AWS Service - CloudFormation
	- Configuration Management 
		- Install right software and tools on the provisioned resources
		- Open Source Tools - Chef, Puppet, Ansible
		- AWS Service - OpsWorks

## AWS Cloud​Formation - Introduction

![](/images/aws/00-icons/cloudformation.png) 
- Lets consider an example:
	- I would want to create a new VPC and a subnet
	- I want to provision a ELB, ASG with 5 EC2 instances and an RDS database in the subnet
	- I would want to setup the right security groups
- AND I would want to create 4 environments 
	- Dev, QA, Stage and Production!
- CloudFormation can help you do all these with a simple (actually NOT so simple) script!

## AWS CloudFormation - Advantages

![](/images/aws/00-icons/cloudformation.png) 

- Automate deployment and modification of AWS resources in a controlled, predictable way
- Avoid configuration drift
- Avoid mistakes with manual configuration
- Think of it as version control for your environments

![](/images/aws/00-icons/cloudformation.png) 

## AWS Cloud​Formation
- All configuration is defined in a simple text file - JSON or YAML
	- I want a VPC, a subnet, a database and ...
- CloudFormation understands dependencies
	- Creates VPCs first, then subnets and then the database
- (Default) Automatic rollbacks on errors (Easier to retry)
	- If creation of database fails, it would automatic delete the subnet and VPC
- Version control your configuration file and make changes to it over time
- Free to use - Pay only for the resources provisioned
	- Get an automated estimate for your configuration

## AWS Cloud​Formation - Example 1 - JSON
```
{
    "Resources" : {
        "MyBucket" : {
            "Type" : "AWS::S3::Bucket"
            "Properties" : {
               "AccessControl" : "PublicRead"               
            }
        }
    }
}
```

## AWS CloudFormation - Example 2 - YAML
```
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: PublicRead
```

## AWS CloudFormation - Example 3
```
Resources:
  Ec2Instance:
    Type: 'AWS::EC2::Instance'
    Properties:
      ImageId: "ami-0ff8a91507f77f867"
      InstanceType: t2.micro
      SecurityGroups:
        - !Ref InstanceSecurityGroup
  InstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      GroupDescription: Enable SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: 0.0.0.0/0
```

## AWS Cloud​Formation - Terminology
- Template 
	- A Cloud​Formation JSON or YAML defining multiple resources
- Stack 
	- A group of resources that are created from a CloudFormation template
	- In the earlier example, the stack contains an EC2 instance and a security group
- Change Sets 
	- To make changes to stack, update the template
	- Change set shows what would change if you execute
	- Allows you to verify the changes and then execute

## AWS Cloud​Formation - Important template elements

```
{
  "AWSTemplateFormatVersion" : "version date",
  "Description" : "JSON string",
  "Metadata" : {},
  "Parameters" : {},
  "Mappings" : {},
  "Resources" : {},
  "Outputs" : {}
}
```

- Resources - What do you want to create?
	- One and only mandatory element
- Parameters - Values to pass to your template at runtime 
	- Which EC2 instance to create? - ("t2.micro", "m1.small", "m1.large")
- Mappings - Key value pairs 
	- Example: Configure different values for different regions
- Outputs - Return values from execution 
	- See them on console and use in automation

## AWS CloudFormation - Mappings Example

```
"Mappings" : {
  "RegionMap" : {
    "us-east-1"      : { "AMI" : "AMI-A"},
    "us-west-1"      : { "AMI" : "ami-B"},
    "eu-west-1"      : { "AMI" : "ami-C"},
    "ap-southeast-1" : { "AMI" : "ami-D"},
    "ap-northeast-1" : { "AMI" : "ami-E"}
  }
}
```

## AWS Cloud​Formation - Remember

![](/images/aws/00-icons/cloudformation.png)  
- Deleting a stack deletes all the associated resources
	- EXCEPT for resources with DeletionPolicy attribute set to "Retain"
	- You can enable termination protection for the entire stack
- Templates are stored in S3
- Use CloudFormation Designer to visually design templates
- AWS CloudFormation StackSets 
	- Create, update, or delete stacks across multiple accounts and regions with a single operation

## Cloud​Formation vs AWS Elastic Beanstalk
![](/images/aws/00-icons/elastic-beanstalk.png) 
![](/images/arrow.png)
![](/images/aws/00-icons/cloudformation.png)  

- (Do you know?) You can create an Elastic Beanstalk environment using CloudFormation!
- Think of Elastic Beanstalk as a pre-packaged CloudFormation template with a User Interface
	- You choose what you want
	- (Background) A Cloud Formation template is created and executed
	- The environment is ready!

## AWS OpsWorks - Configuration Management

![](/images/aws/00-icons/opsworks.png) 
- OpsWorks is used for Configuration Management 
	- How do you ensure that 100 servers have the same configuration?
	- How can I make a change across 100 servers?
- Managed service based on Chef & Puppet
- One service for deployment and operations in cloud and on-premise environments
- Configuration - Chef recipes or cookbooks, Puppet manifests
- All metrics are sent to Amazon CloudWatch
- (IMPORTANT) All configuration management tools can also do infrastructure provisioning
	- However, I would recommend NOT doing that as they are not good at infrastructure provisioning

# AWS Certification - FAQ

## High Availability 
- High Availability - 99.99% or 99.9% - You can fail a few times
- Consider this problem:
	- You have an application deployed on EC2 instances (Load distribution using an ALB)
- How do you design for high availability in a single region (survive a loss of AZ) while being cost effective?
	- Need : 2 EC2 instances running all the time
		- 2 instances in AZ1 and 2 instances in AZ2
	- Need : 4 EC2 instances running all the time
		- 2 instances in AZ1 and 2 instances in AZ2 and 2 instances in AZ3

## High Availability vs Fault Tolerance
- Fault Tolerant - Zero chance of failure
- If you want fault tolerance, you need to take additional precautions
	- 2 EC2 instances running all the time
		- 2 instances in AZ1 and 2 instances in AZ2 and 2 instances in AZ3

## Data Transfer Costs

![](/images/aws/00-icons/ec2instance.png)
![](/images/arrow.png)
![](/images/aws/00-icons/s3.png) 

- Using Public IP addresses for communication between EC2 instances can get expensive. 
	- Use Private IP Addresses
- Here are some of the relaxations that AWS provides:
	- Same Availability Zone - FREE - Data transfer between 
		- Amazon EC2, Amazon RDS, Amazon Redshift, Amazon ElastiCache instances and Elastic Network Interfaces
	- Same Region - FREE - Data transfer between your EC2 instances and 
		- Amazon S3, Amazon Glacier, Amazon DynamoDB
		- Amazon SNS, Amazon SQS, Amazon Kinesis
- (Best Practice) Maximize traffic that stays with an AZ (at least with a Region)

# More AWS Services

## AWS Shield
![](/images/aws/00-icons/shield.png) 
![](/images/aws/00-icons/route53.png) 
![](/images/aws/00-icons/cloudfront.png) 
![](/images/aws/00-icons/ec2.png) 
![](/images/aws/00-icons/elb.png) 

- Shields from Distributed Denial of Service (DDoS) attacks
	- Disrupt normal traffic of a server by overwhelming it with a flood of Internet traffic
- Protect
	- Amazon Route 53
	- Amazon CloudFront
	- AWS Global Accelerator
	- Amazon Elastic Compute Cloud (EC2) instances
	- Elastic Load Balancers (ELB)

## AWS Shield - Standard and Advanced

![](/images/aws/00-icons/shield.png) 
![](/images/aws/00-icons/cloudfront.png)

- AWS Shield Standard
	- Zero Cost. Automatically enabled.
	- Protection against common infrastructure (layer 3 and 4) DDoS attacks
- AWS Shield Advanced
	- Paid service
	- Enhanced protection for Amazon EC2, Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53
	- 24x7 access to the AWS DDoS Response Team (DRT)
	- Protects your AWS bill from usage spikes as a result of a DDoS attack
- Protect any web application (from Amazon S3 or external) from DDoS by putting Amazon CloudFront enabled with AWS Shield in front of it

## AWS WAF - Web Application Firewall

![](/images/aws/00-icons/waf.png) 
- AWS WAF protect your web applications from OWASP Top 10 exploits, CVE and a lot more!
	- OWASP (Open Web Application Security Project) Top 10 
		- List of broadly agreed "**most critical security risks to web applications**" 
		- Examples : SQL injection, cross-site scripting etc
	- Common Vulnerabilities and Exposures (CVE) is a list of information-security vulnerabilities and exposures
- Can be deployed on Amazon CloudFront, Application Load Balancer, Amazon API Gateway
- Customize rules & trigger realtime alerts (CloudWatch Alarms)
- Web traffic filtering : block attacks
	- Filter traffic based on IP addresses, geo locations, HTTP headers and body (block attacks from specific user-agents, bad bots, or content scrapers)

![](/images/aws/00-icons/organizations.png) 
## AWS Organizations 
- Organizations typically have multiple AWS accounts 
	- Different business units 
	- Different environments
- How do you centralize your management (billing, access control, compliance and security) across multiple AWS accounts? 
- Welcome AWS Organizations!
- Organize accounts into Organizational Units (OU)
- Provides API to automate creation of new accounts

## AWS Organizations - Features

![](/images/aws/00-icons/organizations.png) 
- One consolidated bill for all AWS accounts
- Centralized compliance management for AWS Config Rules
- Send AWS CloudTrail data to one S3 bucket (across accounts)
- AWS Firewall Manager to manage firewall rules (across accounts)
	- AWS WAF, AWS Shield Advanced protections and Security Groups
- Use Service control policies (SCPs) to define restrictions for actions (across accounts):
	- Prevent users from disabling AWS Config or changing its rules
	- Require Amazon EC2 instances to use a specific type
	- Require MFA to stop an Amazon EC2 instance
	- Require a tag upon resource creation

## AWS Resource Access Manager
- Share AWS resources with any AWS account or within your AWS Organization
	- AWS Transit Gateways
	- Subnets
	- AWS License Manager configurations 
	- Amazon Route 53 Resolver rules
- Reduce Operational Overhead
- Optimize Costs

## AWS Trusted Advisor

![](/images/aws/00-icons/trustedadvisor.png) 
- Recommendations for cost optimization, performance, security and fault tolerance
	- Red - Action recommended Yellow - investigate and Green - Good to go
- All AWS customers get 4 checks for free:
	- Service limits (usage > 80%)
	- Security groups having unrestricted access (0.0.0.0/0)
	- Proper use of IAM
	- MFA on Root Account
- Business or Enterprise AWS support plan provides over 50 checks
	- Disable those you are not interested in
	- How much will you save by using Reserved Instances?
	- How does your resource utilization look like? Are you right sized?

## AWS Trusted Advisor Recommendations

![](/images/aws/00-icons/trustedadvisor.png) 

- Cost Optimization
	- Highlight unused resources 
	- Opportunities to reduce your costs
- Security 
	- Settings that can make your AWS solution more secure
- Fault Tolerance 
	- Increase resiliency of your AWS solution 
	- Redundancy improvements, over-utilized resources
- Performance 
	- Improve speed and responsiveness of your AWS solutions
- Service Limits 
	- Identify if your service usage is more than 80% of service limits

## AWS Service Quotas
- AWS account has Region-specific default quotas or limits for each service
	- You don't need to remember all of them :)
- Service Quotas allows you to manage your quotas for over 100 AWS services, from one location

## AWS Directory Service

![](/images/aws/00-icons/directoryservice.png) 
- Provide AWS access to on-premise users without IAM users
- Managed service deployed across multiple AZs
- Option 1 : AWS Directory Service for Microsoft AD
	- More than 5000 Users
	- Trust relationship needed between AWS and on-premise directory
- Option 2 : Simple AD
	- Less than 5000 users
	- Powered by Samba4 and compatible with Microsoft AD
	- Does not support trust relationships with other AD domains
- Option 3 : AD Connector
	- Use your existing on-premise directory with AWS cloud services
	- Your users use existing credentials to access AWS resources

## AWS Workspaces
- Desktop-as-a-Service (DaaS)
- Provision Windows or Linux desktops in minutes
- Eliminate traditional desktop management - Virtual Desktop Infrastructure (VDI)

## AWS Systems Manager Parameter Store 
- Manage application environment configuration and secrets 
	- database connections, password etc
- Supports hierarchical structure 
- Store configuration at one place 
	- multiple applications 
	- multiple environments
- Maintains history of configuration over a period of time
- Integrates with KMS, IAM, CloudWatch and SNS

## AWS Secrets Manager
- Rotate, Manage and retrieve database credentials, API keys, and other secrets for your applications
- Integrates with KMS(encryption), Amazon RDS, Amazon Redshift, and Amazon DocumentDB
- (KEY FEATURE) Rotate secrets automatically without impacting applications
- (KEY FEATURE) Service dedicated to secrets management
- Recommended for workloads needing HIPAA, PCI-DSS compliance

## AWS Elemental MediaConvert
- New video transcoding service
- Create high-quality video processing workflows
- Optimize video files for playback on virtually any device
- Convert between multiple media formats (MPEG-2, AVC, Apple ProRes, and HEVC)
- (Alternative) AWS Elastic Transcoder
	- Use AWS Elastic Transcoder to create WebM video, MP3 audio, or animated GIF files
	- For all other video processing use cases, AWS Elemental MediaConvert is recommended
- (Alternative) For live video, use AWS Elemental MediaLive

## Amazon Macie
- Fully managed data security and data privacy service
- Automatically discover, classify, and protect sensitive data in Amazon S3 buckets
- When migrating data to AWS use S3 for staging 
	- Run Macie to discover secure data
- Uses machine learning 
- Recognizes sensitive data 
	- Example: personally identifiable information (PII) or intellectual property
- Provides you with dashboards and alerts 
	- Gives visibility into how data is being accessed or moved

## AWS Single Sign On
- Cloud-based single sign-on (SSO) service
- Centrally manage SSO access to all of your AWS accounts
- Integrates with Microsoft AD (Supports using your existing corporate accounts)
- Supports Security Assertion Markup Language (SAML) 2.0
- Deep integration with AWS Organizations (Centrally manage access to multiple AWS accounts)
- One place auditing in AWS CloudTrail

## AWS Elasticsearch
- AWS Managed Service around Elasticsearch
- Supports the popular ELK stack
	- Elasticsearch for search and analytics
	- Logstash to ingest data from multiple sources
	- Kibana for visualization
- Use cases 
	- Search (Provide fast search for websites)
	- Application monitoring (Get intelligence from your application logs)
	- Infrastructure monitoring (Get intelligence from your server logs)

# Architecture and Best Practices

## Well Architected Framework

![](/images/aws/00-icons/aws.png) 
- Helps cloud architects build application infrastructure which is:
	- Secure
	- High-performing
	- Resilient and
	- Efficient
- Five Pillars
	- Operational Excellence
	- Security
	- Reliability
	- Performance Efficiency
	- Cost Optimization

## Operational Excellence
![](/images/aws/00-icons/lambda.png)
![](/images/aws/00-icons/cloudformation.png)
![](/images/aws/00-icons/codepipeline.png) 
![](/images/aws/00-icons/config.png) 
![](/images/aws/00-icons/cloudwatch.png) 

- Avoid/Minimize effort and problems with
	- Provisioning servers
	- Deployment
	- Monitoring
	- Support

## Operational Excellence - Solutions and AWS services

 
![](/images/aws/00-icons/lambda.png)
![](/images/aws/00-icons/cloudformation.png)
![](/images/aws/00-icons/codepipeline.png) 
![](/images/aws/00-icons/codebuild.png)
![](/images/aws/00-icons/codedeploy.png)

- Use Managed Services
	- You do not need to worry about managing servers, availability, durability etc
- Go serverless
	- Prefer Lambda to EC2!
- Automate with Cloud Formation 
	- Use Infrastructure As Code
- Implement CI/CD to find problems early
	- CodePipeline
	- CodeBuild
	- CodeDeploy
- Perform frequent, small reversible changes

## Operational Excellence - Solutions and AWS services
 
![](/images/aws/00-icons/config.png) 
![](/images/aws/00-icons/cloudwatch.png)
![](/images/aws/00-icons/cloudtrail.png)
![](/images/aws/00-icons/xray.png)
![](/images/aws/00-icons/es.png)

- Prepare: for failure 
	- Game days 
	- Disaster recovery exercises
	- Implement standards with AWS Config rules 
- Operate: Gather Data and Metrics
	- CloudWatch (Logs agent), Config, Config Rules, CloudTrail, VPC Flow Logs and X-Ray (tracing)
- Evolve: Get intelligence
	- Use Amazon Elasticsearch to analyze your logs

## Security Pillar
![](/images/aws/00-icons/iam.png) 
![](/images/aws/00-icons/shield.png) 
![](/images/aws/00-icons/waf.png) 
![](/images/aws/00-icons/kms.png) 
![](/images/aws/00-icons/cloudhsm.png) 

- Principle of least privilege for least time
- Security in Depth - Apply security in all layers
- Protect Data in Transit and at rest
- Actively monitor for security issues
- Centralize security policies for multiple AWS accounts

## Security Pillar - Principle of least privilege for least time
![](/images/aws/00-icons/iam.png)
- Use temporary credentials when possible (IAM roles, Instance profiles)
- Use IAM Groups to simplify IAM management
- Enforce strong password practices
- Enforce MFA
- Rotate credentials regularly

## Security Pillar - Security in Depth 

![](/images/aws/00-icons/vpc.png) 
![](/images/aws/00-icons/ami.png) 
![](/images/aws/00-icons/shield.png) 
![](/images/aws/00-icons/waf.png) 
![](/images/aws/00-icons/cloudformation.png) 

- VPCs and Private Subnets
	- Security Groups
	- Network Access Control List (NACL)
- Use hardened EC2 AMIs (golden image)
	- Automate patches for OS, Software etc
- Use CloudFront with AWS Shield for DDoS mitigation
- Use WAF with CloudFront and ALB 
	- Protect web applications from CSS, SQL injection etc
- Use CloudFormation
	 - Automate provisioning infrastructure that adheres to security policies

## Security Pillar - Protecting Data at Rest

![](/images/aws/00-icons/kms.png) 
![](/images/aws/00-icons/cloudhsm.png)
- Enable Versioning (when available)
- Enable encryption - KMS and Cloud HSM
	- Rotate encryption keys
- Amazon S3
	- SSE-C, SSE-S3, SSE-KMS
- Amazon DynamoDB
	- Encryption Client, SSE-KMS
- Amazon Redshift
	- AWS KMS and AWS CloudHSM
- Amazon EBS, Amazon SQS and Amazon SNS
	- AWS KMS
- Amazon RDS
	- AWS KMS, TDE

## Security Pillar - Protecting Data in Transit 
![](/images/aws/00-icons/certificatemanager.png)
- Data coming in and going out of AWS
- By default, all AWS API use HTTPS/SSL
- You can also choose to perform client side encryption for additional security
- Ensure that your data goes through AWS network as much as possible
	- VPC Endpoints and AWS PrivateLink

## Security Pillar - Detect Threats
![](/images/aws/00-icons/cloudwatch.png)
![](/images/aws/00-icons/organizations.png)
- Actively monitor for security issues:
	- Monitor CloudWatch Logs
	- Use Amazon GuardDuty to detect threats and continuously monitor for malicious behavior
- Use AWS Organization to centralize security policies for multiple AWS accounts

## Reliability
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/sqs.png) 
![](/images/aws/00-icons/sns.png) 
![](/images/aws/00-icons/apigateway.png) 
![](/images/aws/00-icons/autoscaling.png)
- Ability to
	- Recover from infrastructure and application issues
	- Adapt to changing demands in load

## Reliability - Best Practices
![](/images/aws/00-icons/autoscaling.png)
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/aws/00-icons/cloudwatch.png)
- Automate recovery from failure
	- Health checks and Auto scaling
	- Managed services like RDS can automatically switch to standby
- Scale horizontally
	- Reduces impact of single failure
- Maintain Redundancy
	- Multiple Direct Connect connections
	- Multiple Regions and Availability Zones

## Reliability - Best Practices
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/sqs.png) 
![](/images/aws/00-icons/sns.png) 
![](/images/aws/00-icons/apigateway.png) 

- Prefer serverless architectures
- Prefer loosely coupled architectures
	- SQS, SNS
- Distributed System Best Practices
	- Use Amazon API Gateway for throttling requests
	- AWS SDK provides retry with exponential backoff

## Loosely coupled architectures

![](/images/aws/00-icons/elb.png) 
![](/images/aws/00-icons/sns.png) 
![](/images/aws/00-icons/sqs.png) 
![](/images/aws/00-icons/kinesis.png) 

- ELB
	- Works in tandem with AWS auto scaling
- Amazon SQS
	- Polling mechanism
- Amazon SNS
	- Publish subscribe pattern
	- Bulk notifications and Mobile push support
- Amazon Kinesis
	- Handle event streams
	- Multiple clients
	- Each client can track their stream position

## Troubleshooting on AWS - Quick Review
 
| Option | Details  | When to Use |
|--|:--|:--|
|Amazon S3 Server Access Logs | S3 data request details - request type, the resources requested, and the date and time of request      |  Troubleshoot bucket access issues and data requests       |
|Amazon ELB Access Logs|Client's IP address, latencies, and server responses|Analyze traffic patterns and troubleshoot network issues|
|Amazon VPC Flow Logs|Monitor network traffic|Troubleshoot network connectivity and security issues|

## Troubleshooting on AWS - Quick Review
| Option | Details  | When to Use |
|--|:--|:--|
|Amazon CloudWatch | Monitor metrics from AWS resources | Monitoring|
|Amazon CloudWatch Logs|Store and Analyze log data from Amazon EC2 instances and on-premises servers | Debugging application issues and Monitoring|
|AWS Config|AWS resource inventory. History. Rules.|Inventory and History|
|Amazon CloudTrail|History of AWS API calls made via AWS Management Console, AWS CLI, AWS SDKs etc.|Auditing and troubleshooting. Determine who did what, when, and from where.|

## Performance Efficiency
- Meet needs with minimum resources (efficiency)
- Continue being efficient as demand and technology evolves

## Performance Efficiency - Best Practices
![](/images/aws/00-icons/cloud.png) 
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/apigateway.png)
![](/images/aws/00-icons/cloudwatch.png) 
![](/images/aws/00-icons/sqs.png) 

- Use Managed Services
	- Focus on your business instead of focusing on resource provisioning and management
- Go Serverless
	- Lower transactional costs and less operational burden
- Experiment
	- Cloud makes it easy to experiment
- Monitor Performance
	- Trigger CloudWatch alarms and perform actions through Amazon SQS and Lambda

## Performance Efficiency - Choose the right solution

![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/s3.png) 
![](/images/aws/00-icons/dynamodb.png) 
![](/images/aws/00-icons/elasticache.png) 
![](/images/aws/00-icons/cloudfront.png) 

- Compute
	- EC2 instances vs Lambda vs Containers
- Storage
	- Block, File, Object
- Database
	- RDS vs DynamoDB vs RedShift ..
- Caching
	- ElastiCache vs CloudFront vs DAX vs Read Replicas
- Network
	- CloudFront, Global Accelerator, Route 53, Placement Groups, VPC endpoints, Direct Connect 
- Use product specific features 
	- Enhanced Networking, S3 Transfer Acceleration, EBS optimized instances

## Cost Optimization

![](/images/aws/00-icons/autoscaling.png) 
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/trustedadvisor.png) 
![](/images/aws/00-icons/cloudwatch.png) 
![](/images/aws/00-icons/cloudfront.png) 
- Run systems at lowest cost

## Cost Optimization - Best Practices

![](/images/aws/00-icons/autoscaling.png) 
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/trustedadvisor.png) 
![](/images/aws/00-icons/cloudwatch.png) 
![](/images/aws/00-icons/cloudfront.png) 
- Match supply and demand
	- Implement Auto Scaling
	- Stop Dev/Test resources when you don't need them
	- Go Serverless
- Track your expenditure
	- Cost Explorer to track and analyze your spend
	- AWS Budgets to trigger alerts
	- Use tags on resources

## Cost Optimization - Choose Cost-Effective Solutions

![](/images/aws/00-icons/autoscaling.png) 
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/trustedadvisor.png) 
![](/images/aws/00-icons/cloudwatch.png) 
![](/images/aws/00-icons/cloudfront.png) 
- Right-Sizing : Analyze 5 large servers vs 10 small servers
	- Use CloudWatch (monitoring) and Trusted Advisor (recommendations) to right size your resources
- Email server vs Managed email service (charged per email)
- On-Demand vs Reserved vs Spot instances
- Avoid expensive software : MySQL vs Aurora vs Oracle
- Optimize data transfer costs using AWS Direct Connect and Amazon CloudFront


# Get Ready

## Certification Resources

| Title |Link  | 
|--|:--|
| Certification - Home Page | https://aws.amazon.com/certification/certified-solutions-architect-associate/ |
| AWS Architecture Home Page |  https://aws.amazon.com/architecture/     |
| AWS FAQs   |   https://aws.amazon.com/faqs/ (EC2, S3, VPC, RDS, SQS etc)   |

## Certification Exam 
- Multiple Choice Questions
	- Type 1 : Single Answer - 4 options and 1 right answer
	- Type 2 : Multiple Answer - 5 options and 2 right answers
- No penalty for wrong answers
	- Feel free to guess if you do not know the answer
- 65 questions and 130 minutes
	- Ask for 30 extra minutes BEFORE registering if you are non native English speaker
- Result immediately shown after exam completion
- Email with detailed scores (a couple of days later)

## Certification Exam - My Recommendations
- Read the entire question 
- Read all answers at least once
- Identify and write down the key parts of the question:
	- Features: serverless, key-value, relational, auto scaling
	- Qualities: cost-effective, highly available, fault tolerant
- If you do NOT know the answer, eliminate wrong answers first
- Mark questions for future consideration and review them before final submission

## Registering for Exam

- Certification - Home Page - https://aws.amazon.com/certification/certified-solutions-architect-associate/ |

# You are all set!

## Let's clap for you!
- You have a lot of patience! Congratulations
- You have put your best foot forward to be an AWS Solution Architect
- Make sure you prepare well and 
- Good Luck!

## Do Not Forget!
- Recommend the course to your friends!
	- Do not forget to review!
- Your Success = My Success
	- Share your success story with me on LinkedIn (Ranga Karanam)
	- Share your success story and lessons learnt in Q&A with other learners!