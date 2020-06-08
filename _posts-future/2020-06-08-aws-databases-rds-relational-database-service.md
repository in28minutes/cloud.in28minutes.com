---
layout:     post
title:      Amazon RDS - Relational Database Service and Amazon Aurora - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon RDS from an AWS certification perspective. We will look at important certification questions regarding Amazon RDS. 
categories:  AWS_CLOUD AWS_DATABASES
permalink:  /aws-certification-amazon-rds-relational-database-service
---

Let's get a quick overview of Amazon RDS from an AWS certification perspective. We will look at important certification questions regarding Amazon RDS.

## You will learn
- What is Amazon RDS?
- What are the different database options provided by Amazon RDS?
- What are the important features of Amazon RDS?
- What are the responsibilities of AWS/Customer when using Amazon RDS?
- When do we use Amazon RDS?
- How is Amazon Aurora different from other Amazon RDS databases ?
- What is Amazon Aurora?
- How do you implement encryption for Amazon RDS in integration with KMS?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

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

## Amazon RDS - Certification and Interview Questions

| Scenario | Solution  | 
|--|:--|
|You want full control of OS or need elevated permissions|Consider going for a custom installation (EC2 + EBS)|
|You want to migrate data from an on-premise database to cloud database of the same type|Consider using AWS Database Migration Service|
|You want to migrate data from one database engine to another (Example : Microsoft SQL Server to Amazon Aurora)|Consider using AWS Schema Conversion Tool|
|What are retained when you delete a RDS database instance?|All automatic backups are deleted<BR/>All manual snapshots are retained (until explicit deletion)<BR/>(Optional) Take a final snapshot|
|How do you reduce global latency and improve disaster recovery?|Use multi region read replicas|
|How do you select the subnets a RDS instance is launched into?|Create DB Subnet groups|
|How can you add encryption to an unencrypted database instance?|Create a DB snapshot<BR/>Encrypt the database snapshot using keys from KMS<BR/>Create a database from the encrypted snapshot|
|Are you billed if you stop your DB instance? |You are billed for storage, IOPS, backups and snapshots. You are NOT billed for DB instance hours|
|I will need RDS for at least one year. How can I reduce costs?|Use Amazon RDS reserved instances.|
|Efficiently manage database connections| Use Amazon RDS Proxy <BR/> Sits between client applications (including lambdas) and RDS|
