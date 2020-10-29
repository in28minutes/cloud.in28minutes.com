---
layout:     post
title:      Amazon S3 Fundamental - Simple Storage Service - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon S3 from an AWS certification perspective. We will look at important certification questions regarding Amazon S3. 
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-amazon-s3-fundamentals
---

Let's get a quick overview of Amazon S3 from an AWS certification perspective. We will look at important certification questions regarding Amazon S3.

## You will learn
- What is Amazon S3?
- Why do we need Amazon S3?
- When do we use Amazon S3?
- What is Object Storage?
- Building Blocks of Amazon S3 - Objects and Buckets
- How do you do Versioning for Amazon S3 Buckets?
- Static Website Hosting using Amazon S3
- How do you use Amazon S3 Event Notifications?
- When?

## AWS Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Amazon S3 (Simple Storage Service)
![](/images/aws/00-icons/s3.png)

- **Most popular, very flexible & inexpensive** storage service
- Store large objects using a **key-value** approach
- Also called **Object Storage**
- Provides REST API to access and modify objects
- Provides **unlimited storage**:
	- (S3 storage class) **99.99% availability** & **(11 9's - 99.999999999) durability**
	- Objects are **replicated in a single region (across multiple AZs)**
- **Store all file types** - text, binary, backup & archives:
	- Media files and archives
	- Application packages and logs
	- Backups of your databases or storage devices
	- Staging data during on-premise to cloud database migration


## Amazon S3 - Objects and Buckets
![](/images/aws/00-icons/s3.png)

- Amazon S3 is a **global service**. NOT associated with a region.
	- HOWEVER a bucket is created in a specific AWS region
- Objects are stored in buckets
	- Bucket names are **globally unique**
	- Bucket names are used as part of object URLs => Can contain ONLY lower case letters, numbers, hyphens and periods.
	- Unlimited objects in a bucket
- Each object is identified by a **key value pair**
	- **Key is unique** in a bucket
	- Max object size is **5 TB**
- (Remember) **No hierarchy** of buckets, sub-buckets or folders

## Amazon S3 Key Value Example

![](/images/aws/s3-folder-structure.png)

| Key                 |         Value        |
|:--:|:--:|
| 2030/course0.png    | image-binary-content |
| 2030/10/course1.png | image-binary-content |
| 2030/10/course2.png | image-binary-content |
| 2030/11/course2.png | image-binary-content |
| 2030/11/course3.png | image-binary-content |

## Amazon S3 Versioning

![](/images/aws/00-icons/s3bucket.png)

- Protects against **accidental deletion**
- Versioning is **optional** and is enabled at bucket level
- You can turn on versioning on a non versioned bucket
	- All old objects will have a version of null
- You cannot turn off versioning on a versioned bucket
	- You can only **suspend** versioning

## Amazon S3 Static Website Hosting
- Use S3 to host a static website using a bucket
- Step 1 : Upload website content
- Step 2 : Enable **Static website hosting**
- Step 3 : Disable "Block public access"
- Step 4 : Configure "Bucket policy" to enable public read access

## Resource-based policies - Bucket policies
```
{
	"Version":"2012-10-17",
	"Statement":[
	{
		"Sid":"PublicRead",
		"Effect":"Allow",
		"Principal": "*",
		"Action":["s3:GetObject"],
		"Resource":["arn:aws:s3:::mybucket/*"]
	}
	]
}
```

- Control access to your bucket and objects
- Can grant **cross account** and **public** access
	

## Amazon S3 - Tags
![](/images/aws/00-icons/s3bucket.png)

- Tags can be assigned to **most AWS resources**
- Can be used for **automation, security (policies), cost tracking** etc
- **Key-value pairs** applied to S3 objects:
	- Environment=Dev
	- Classification=Secure
	- Project=A
- Can be used in creating ** lifecycle policies**
- Can be **updated continuously** during the lifetime of an object

## Amazon S3 Event Notifications

![](/images/aws/00-icons/s3bucket.png)
![](/images/arrow.png)
![](/images/aws/00-icons/lambdafunction.png)
- Configure **notifications** when **certain events** happen in your bucket
- **Event Sources**
	- New object created events
	- Object removal events 
	- Reduced Redundancy Storage (RRS) object lost events
	- Replication events
- **Event Destinations**
	- Amazon SNS topic
	- Amazon SQS queue
	- AWS Lambda function

## Amazon S3 - Prefix
![](/images/aws/s3-folder-structure.png)
- Allows you to search for keys **starting with a certain prefix**
- Searching with prefix `2030/10` returns
	- `2030/10/course1.png` & `2030/10/course2.png`
- URL - http://s3.amazonaws.com/my-bucket-ranga?prefix=2030/10/
	- Above URL would work only when public access is allowed
- Supported by REST API, AWS SDK, AWS CLI and AWS Management Console
- **Used in IAM and Bucket Policies** to restrict access to specific files or group of files

## Bucket ACLs and Object ACLs 
- **Bucket/Object ACLs**
	- Access for bucket/object owner
	- Access for other AWS accounts
	- Public access
- Use **object ACLs (object level access)**
	- When bucket owner is not the object owner
	- When you need different permissions for different objects in the same bucket
- (Remember) Bucket/Object ACLs
	- **CANNOT** have conditions while policies can have conditions
	- **CANNOT** explicitly DENY access
	- **CANNOT** grant permissions to other individual users
- (Remember) ACLs are **primarily** used to grant permissions to public or other AWS accounts


## S3 Lifecycle configuration
![](/images/aws/s3-lifecycle-transitions.png)
https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html
- Files are frequently accessed when they are created
- Generally **usage reduces with time**
- How do you save costs and **move files automatically between storage classes**?
	- Solution: S3 Lifecycle configuration
- Two kinds of actions:
	- **transition** actions (one storage class to another)
	- **expiration** actions (delete objects) 
- Object can be identified by tags or prefix.

## Amazon S3 Replication - Same Region and Multiple Region

![](/images/aws/00-icons/s3bucket.png)
![](/images/arrow.png)
![](/images/aws/00-icons/s3bucket.png)
- Replicate objects between buckets in same or different regions
	- Could be **cross account**
	- Can be configured at bucket level, a shared prefix level, or an object level using S3 object tags
	- Access to destination bucket is provided using **IAM Policy**
- **Versioning should be enabled** on **BOTH** source and destination
- ONLY new objects are replicated (Explicitly copy existing objects)
- (Advantage) Reduces latency and helps you meet regulations
- (USECASE) Object replication between dev & test environments

## Amazon S3 - Object level configuration
![](/images/aws/00-icons/s3.png)
![](/images/aws/00-icons/s3bucket.png)
- You can configure these at **individual object level** (overriding bucket level configuration):
	- Storage class
	- Encryption
	- Objects ACLs

## Amazon S3 Consistency
![](/images/aws/00-icons/s3.png)

- S3 is distributed - maintains **multiple copies** of your data in a Region to ensure durability
- Distributing data **presents a challenge**
	- How do you ensure data is consistent?
- **S3 Consistency Model**
	- **READ AFTER WRITE for PUTS** of new objects
	- Eventual Consistency for Overwrites PUTS and DELETES
- (In simplified words) S3 Data is highly distributed across multiple AZs and (possibly) multiple regions:
	- When you create a new object, it is immediately available
	- You might get a previous version of data immediately after an object update using PUT/DELETE
	- You will never get partial or inconsistent data

## Amazon S3 Presigned URL
- Grant **time-limited permission** (few hours to 7 days) to download objects
- **Avoid** web site scraping and unintended access
- Specify:
	- Your security credentials
	- Bucket name
	- Object key
	- HTTP method and
	- Expiration date and time
- Created using AWS SDK API
	- Java code 
		- *GeneratePresignedUrlRequest(bucketName, objectKey).withMethod(HttpMethod.GET).withExpiration(expiration);*

## Amazon S3 Access Points
![](/images/aws/s3_access_points.png)
- **Simplifies** bucket policy configuration 
- Create **application specific access points** with an application specific policy
- Provide **multiple customized paths** with unique hostname and access policy for each bucket
- “dual-stack” endpoint supports IPv4 and IPv6 access

## Amazon S3 Certification and Interview Questions - Security 

| Scenario | Solution  | 
|--|:--|
|Prevent objects from being deleted or overwritten for a few days or for ever| Use **Amazon S3 Object Lock**. Can be enabled only on new buckets. Automatically enables versioning. Prevents deletion of objects. Allows you to meet regulatory requirements.|
|Protect against accidental deletion|  Use Versioning |
|Protect from changing versioning state of a bucket| Use MFA Delete. You need to be an owner of the bucket AND Versioning should be enabled.|
|Avoid content scraping. Provide secure access.| Pre Signed URLS. Also called Query String Authentication. |
|Enable cross domain requests to S3 hosted website (from www.abc.com to www.xyz.com)|Use Cross-origin resource sharing (CORS)|

## Amazon S3 Cost
![](/images/aws/00-icons/s3.png)

- Important **pricing elements**:
	- Cost of Storage (per GB)
	- (If Applicable) Retrieval Charge (per GB)
	- Monthly tiering fee (Only for Intelligent Tiering)
	- Data transfer fee
- **FREE of cost**:
	- Data transfer into Amazon S3
	- Data transfer from Amazon S3 to Amazon CloudFront
	- Data transfer from Amazon S3 to services in the same region

## Amazon S3 Certification and Interview Questions - Costs

| Scenario | Solution  | 
|--|:--|
|Reduce Costs | Use proper storage classes. <BR/>Configure lifecycle management. |
|Analyze storage access patterns and decide the right storage class for my data|Use Intelligent Tiering. <BR/> Use Storage Class Analysis reports to get an analysis.|
|Move data automatically between storage classes|Use Lifecycle Rules|
|Remove objects from buckets after a specified time period|Use Lifecycle Rules and configure Expiration policy|

## Amazon S3 Performance
![](/images/aws/00-icons/s3.png)

- Amazon S3 is serverless
- Recommended for large objects
- Amazon S3 supports upto 
	- **3,500 requests per second** to add data 
	- **5,500 requests per second** to retrieve data 
	- Zero additional cost
	- With each S3 prefix
- **Transfer acceleration**
	- Enable fast, easy and secure transfers of files to and from your bucket

## Amazon S3 Certification and Interview Questions - Performance

| Scenario | Solution  | 
|--|:--|
|Improve S3 bucket performance|Use **Prefixes**. Supports upto 3,500 RPS to add data and 5,500 RPS to retrieve data with each S3 prefix.|
|Upload large objects to S3 | Use **Multipart Upload** API. <BR/>**Advantages**: 1. Quick recovery from any network issues 2. Pause and resume object uploads 3. Begin an upload before you know the final object size. <BR/>**Recommended** for files **>100 MB** and **mandatory** for files **>4 GB** |
|Get part of the object | Use **Byte-Range Fetches** - Range HTTP header in GET Object request <BR/> Recommended: GET them in the same part sizes used in multipart upload |
|Is this recommended: <BR/> EC2 (Region A) <-> S3 bucket (Region B) | No. **Same region recommended**. <BR/>Reduce network latency and data transfer costs|

## Amazon S3 Certification and Interview Questions - Features

| Scenario | Solution  | 
|--|:--|
|Make user pay for S3 storage| **Requester pays** - The requester (instead of the bucket owner) will pay for requests and data transfer.|
|Create an inventory of objects in S3 bucket|Use **S3 inventory report** |
|I want to change object metadata or manage tags or ACL or invoke Lambda function for billions of objects stored in a single S3 bucket|Generate **S3 inventory report** <BR/> Perform **S3 Batch Operations** using the report|
|Need S3 Bucket (or Object) Access Logs|Enable **S3 Server Access Logs** (default: off). Configure the bucket to use and a prefix (logs/). |