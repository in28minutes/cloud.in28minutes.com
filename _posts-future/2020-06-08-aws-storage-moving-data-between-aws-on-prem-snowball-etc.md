---
layout:     post
title:      Moving Data between AWS and On-premises - Snowball vs Snowmobile vs DataSync - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Moving Data between AWS and On-premises - Snowball vs Snowmobile vs DataSync. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-moving-data-aws-on-prem-snowball-vs-snowmobile-vs-datasync
---

Let's get a quick overview of Moving Data between AWS and On-premises - Snowball vs Snowmobile vs DataSync. 

## You will learn
- What are the options for moving Data between AWS and On-premises?
- How do they compare - Snowball vs Snowmobile vs DataSync?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


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
- Transfer from on-premise file storage (NFS, SMB) to S3, EFS or FSx for Windows
- Monitor progress using Amazon CloudWatch
- (Use cases) Data Migration, Data replication and Cold data archival
- (Alternative) Use AWS Snowball if you are bandwidth constrained or transferring data from remote, or disconnected 
- (Alternative) Use S3 Transfer Acceleration when your applications are integrated with S3 API. If not, prefer AWS DataSync(Supports multiple destinations, built-in retry)
- (Integration) Migrate data using DataSync and use AWS Storage Gateway for ongoing updates from on-premises applications
