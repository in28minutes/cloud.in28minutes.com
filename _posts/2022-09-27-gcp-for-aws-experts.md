---
layout:     post
title:      Introduction to Google Cloud - For AWS Professionals
date:       2022-09-26 12:31:19
summary:    If you are familiar with AWS, this article is the shortcut you need to get quickly started with understanding Google Cloud
categories:  GOOGLE_CLOUD
permalink:  /google-cloud-for-aws-professionals
---

Learning a cloud platform takes a long time.  Google Cloud and AWS have *200+ services* each. 

If you are familiar with AWS, this article is the shortcut you need to get quickly started with understanding Google Cloud.

**Our Goal**: Give you a quick start for Google Cloud!

## Table of Contents

<!-- MarkdownTOC levels="3" -->

- 1: Quick Overview - Google Cloud vs AWS
- 2: Let's dig deeper - Google Cloud vs AWS
- 3: Compute Services
- 4: Databases
- 5: IAM - Identity and Access Management
- 6: Networking
- 7: Organizing Resources
- 8: What's Next?

<!-- /MarkdownTOC -->


### 1: Quick Overview - Google Cloud vs AWS

What is best way to learn a cloud when you are an expert at a different cloud platform? 

I doubt if there is one answer to this question!

All cloud platforms are similar. They have a wide variety of services under different categories - compute, database, networking, storage, security, machine learning, .

We will get started with a quick overview using Q&A kind of approach.

We will look at the question (or context or a problem), the AWS solution, and the comparable Google Cloud solution.

> We are taking a 10,000 feet overview. While services are comparable, when you go deeper, you will find significant differences in terms of the details.

#### Compute Services

| Question | AWS  | Google Cloud | 
|--|:--|:--|
| How do you create Virtual Machines?|Amazon EC2 |Compute Engine|
| How do you attach permanent storage (block storage) with Virtual Machines?|Amazon EBS|Persistent Disk|
| How do you simplify setting up web applications?|AWS Elastic Beanstalk|App Engine|
| How do you orchestrate containers?|Amazon EKS, Amazon ECS|Google Kubernetes Engine (GKE)|
| How do you build serverless applications?| AWS Lambda| Cloud Functions|

#### Database Services

| Question | AWS  | Google Cloud | 
|--|:--|:--|
| How do you create relational OLTP databases?|Amazon RDS (Amazon Aurora)|Cloud SQL, Cloud Spanner|
| What is the relational data warehouse solution?|Amazon Redshift|BigQuery|
| What are the NoSQL database options?|Amazon DynamoDB, Amazon DocumentDB|Datastore/Firestore, Cloud Bigtable|
| How do you cache data from a database?| Amazon ElastiCache| Memorystore|

#### Networking Services

| Question | AWS  | Google Cloud | 
|--|:--|:--|
| How do distribute load among VMs?|Elastic Load Balancer|Cloud Load Balancing|
| How do you build private networks?|Amazon VPC|Cloud VPC|
| How do you connect on-premise with the cloud?|AWS VPN(shared), AWS Direct Connect (dedicated)|Cloud VPN(shared), Cloud Interconnect (dedicated)|

#### Storage Services

|Type|AWS|Google Cloud|
|:--:|:--|:--|
|Persistent Block storage|Amazon Elastic Block Store|Persistent Disk|
|Ephemeral Block storage|Instance Store|Local SSDs|
|Object storage|Amazon S3 (Simple Storage Service)|Cloud Storage|
|Infrequent Access Object Storage|Amazon S3 - Standard-IA, One Zone-IA|Cloud Storage - Nearline and Coldline classes|
|Archival Object Storage|Amazon Glacier|Cloud Storage - Archive class|
|File storage|Amazon Elastic File System|Filestore|


#### DevOps Services

| Question | AWS  | Google Cloud | 
|--|:--|:--|
|How do you automate deployment?|AWS CloudFormation|Cloud Deployment Manager|
|How do you monitor metrics around your applications?|Amazon CloudWatch|Cloud Monitoring|
|How do you manage application and service logs?|Amazon CloudWatch Logs|Cloud Logging|
|How do you trace requests across applications and services?|AWS X-Ray|Cloud Trace|
|How do you implement Continuous Integration?|AWS CodePipeline, CodeDeploy|Cloud Build|

#### Other Services

| Question | AWS  | Google Cloud | 
|--|:--|:--|
|What are the messaging services?|Amazon SNS, Amazon SQS|Cloud Pub/Sub|
|How do you manage authentication and authorization to Cloud?|Amazon IAM|Cloud IAM|
|How do you manage keys used for encrypting data?|AWS KMS|Cloud KMS|


### 2: Let's dig deeper - Google Cloud vs AWS

Let's now dig deeper into a few specific important groups of services.


### 3: Compute Services

There is a variety of compute services offered by each cloud platform. 

If you want complete flexibility to manage OS, software and hardware used to run your applications, you want to go with the Infrastructure as a Service option. However, with flexibility, you get a lot of responsibility. 

If you want to reduce your responsibilities (concerning scaling, availability, and durability), you might want to use managed services in the cloud.

If you want to run a simple web application in Google Cloud, you might want to go with either App Engine or Cloud Run (if you want to use containers).

If you want to implement microservices architecture with Kubernetes, you can go with Google Kubernetes Engine.

Cloud Functions is the Serverless, Function as a Service offering in Google Cloud.

|Category|AWS|Google Cloud|
|:--:|--|--|
|IAAS|Amazon EC2| Google Compute Engine|
|PAAS|AWS Elastic Beanstalk|App Engine|
|CAAS - Kubernetes|Amazon EKS|Google Kubernetes Engine|
|CAAS - Custom|Amazon ECS| |
|CAAS - Serverless|AWS Fargate|Cloud Run|
|FAAS - Serverless | AWS Lambda |Cloud Functions|

#### Google Compute Engine

In AWS, we use EC2 service to provision Virtual Instances.

In Google Cloud, the corresponding service is GCE or Google Compute Engine 

To create a VM, you need to choose OS, Software (Image), and Hardware (Machine Family and Machine Type). In addition, you can configure Firewall Rules to restrict inbound and outbound traffic to/from your VM. Persistent Disk is the service to manage block storage attached with Compute Engine VMs.

| Feature | AWS  | Google Cloud | 
|--|:--|:--|
| Create Virtual Machines| Amazon EC2| Google Compute Engine (GCE) |
| Choose Operating System and Software| AMI (Amazon Machine Image)| Image|
| Choose the right family of hardware (Generic or high memory or high compute)| Instance Family| Machine Family|
| Choose the right quantity of hardware (2 vCPUs, 4GB of memory)| Instance Type| Machine Type|
| Restrict inbound and outbound traffic| Security Groups| Firewall Rules|
| Attach Permanent Hard Disks (Block Storage)| Amazon EBS| Persistent Disks|


#### IP Addresses - Virtual Machines

Almost all cloud platforms offer solutions to create public, private, and static IP addresses for your resources. In AWS and GCP, the names used to refer to these are different. Other than that, the concepts remain similar.

| Feature | AWS  | Google Cloud | 
|--|:--|:--|
|Permanent Internal IP Address that does not change during the lifetime of an instance| Private IP Address| Internal IP Address|
|Ephemeral External IP Address that changes when an instance is stopped| Public IP Address| External or Ephemeral IP Address|
|Permanent External IP Address that can be attached to a VM|Elastic IP Address|Static IP Address|

#### Managing Virtual Machines

One virtual machine does not provide sufficient scalability and availability for your solution. We need multiple virtual machines. Here are some of the important features that simplify the management of your virtual machines.

| Feature | AWS  | Google Cloud | 
|--|:--|:--|
|Templates to simplify creation of Virtual Machines|Launch Templates/ Configuration|Instance templates|
|Simplify the creation of multiple Virtual Machines|Auto Scaling Group|Instance Groups|
|Simplify management (software, OS patches, etc) of 1000's Virtual Machines|Systems Manager| VM Manager|
|Physical hosts dedicated to one customer|EC2 Dedicated Hosts|Sole-tenant nodes|


#### Manage Costs for Virtual Machines

You want to run your VMs at the lowest cost possible. Here are some of the options provided by AWS and Google Cloud to reduce your costs.

|Feature| Amazon EC2  | GCE |
|--|--|--|--|
|Billing|Billed by second|Billed by second <BR/>(after 1st minute)|
|Create cheaper, temporary instances for non-critical workloads|Spot instances|Preemptible VMs <BR/>(Fixed pricing, Max 24 hrs)|
|Reserve compute instances ahead of time|Reserved instances|Committed use discounts|
|Get discounts for using resources for long periods |None|Sustained use discounts|
|Budget Management|Budget alerts|Budget alerts|


#### App Engine vs AWS Elastic Beanstalk

Google Cloud App Engine and AWS Elastic Beanstalk are the recommended options to run simple web applications and/or REST API.

Here is a comparison of some of the important features of these two services:

|Feature|AWS Elastic Beanstalk| App Engine|
|--|:--|:--|
|Recommended for| Simple Web Apps and Batch Apps|Simple Web Apps and Batch Apps (For simple microservices)|
|Database Integrations|Amazon RDS, Amazon DynamoDB| Firestore, Cloud SQL|
|Batch Programs|Worker Tier with SQS integration|Asynchronous task queues - Pub Sub|
|Hierarchy|Application > Application version > Environment| Application > Service > Version|
|Run Containers| Yes| Yes (App Engine flexible)|
|New Releases|Rolling updates, blue/green deployment (using Swap URL)|Rolling updates, blue/green deployment|

### 4: Databases

Let's look at the different types of databases in AWS and Google Cloud.

#### Relational Databases - OLTP - Online Transaction Processing

Let's start with applications where a large number of users make a large number of small transactions ( small reads & updates). Typical use cases include CRM, e-commerce, and banking applications. The most popular databases are MySQL, Oracle, SQL Server, etc.

Recommended AWS Services in this space is Amazon RDS. Amazon RDS supports Amazon Aurora, PostgreSQL, MySQL, MariaDB (Enhanced MySQL), Oracle Database, and SQL Server. Amazon Aurora provides a "Global Database" option.

Recommended GCP Services are:
- Cloud SQL: Supports PostgreSQL, MySQL, and SQL Server for regional relational databases (up to a few TBs)
- Cloud Spanner: Unlimited scale (multiple PBs) and 99.999% availability for global applications with horizontal scaling

#### Relational Database - OLAP - Online Analytics Processing

OLAP Applications allow users to analyze petabytes of data. Examples include Reporting applications, Data warehouses, Business intelligence applications, and Analytics systems.

Recommended AWS Managed Service is Amazon Redshift.

Recommended GCP Managed Service is BigQuery.

#### NoSQL Databases
NoSQL represents a new approach (actually NOT so new!) to building your databases.

NoSQL stands for "not only SQL". You would use NoSQL databases when you need flexible schema - structure data the way your application needs it and you want to let the schema evolve with time.

Most NoSQL databases can scale horizontally to petabytes of data with millions of TPS.

AWS Managed Services are Amazon DynamoDB & Amazon DocumentDB.

Google Managed Services are Cloud Firestore (Datastore) &  Cloud BigTable.

#### Choosing between Cloud Firestore, Datastore vs Cloud BigTable
Cloud Datastore is managed serverless NoSQL document database. It provides ACID transactions, SQL-like queries, and indexes. It is designed for transactional mobile and web applications.

Firestore is the next version of Datastore with additional capabilities like Strong consistency and Mobile and Web client libraries.

Firestore and Datastore are recommended for small to medium databases (0 to a few Terabytes).

Cloud BigTable on the other hand, is a managed, scalable NoSQL wide column database. It is NOT serverless (You need to create instances). 

BigTable is recommended for data sizes> 10 Terabytes to several Petabytes. It is usually used for large analytical and operational workloads.

BigTable is NOT recommended for transactional workloads. It does NOT support multi-row transactions - supports ONLY single-row transactions.

#### In-memory Databases

Retrieving data from memory is much faster than retrieving data from disk. In-memory databases like Redis deliver microsecond latency by storing persistent data in memory.

Recommended AWS Managed Service is Amazon ElastiCache.

Recommended GCP Managed Service is Memorystore.

Both Amazon ElastiCache and Memorystore support Redis and Memcached.

#### A Quick Summary of Databases

| Type |AWS  | GCP |
|--|:--|:--|
|RDBMS|Amazon Relational Database Service, Amazon Aurora|Cloud SQL, Cloud Spanner|
|NoSQL|Amazon DynamoDB, Amazon DocumentDB|Datastore/Firestore, Cloud Bigtable|
|In-memory|Amazon ElastiCache|Memorystore|
|Data warehouse|Amazon Redshift|BigQuery|



### 5: IAM - Identity and Access Management

Google Cloud and AWS use the same name for their authentication and authorization service - Identity and Access Management (IAM). However, the concepts of IAM are very different.

#### How does IAM work in AWS?


Here are some of the important IAM concepts in AWS:

- IAM users: Users created in an AWS account
  - Have credentials (name/password or access keys)
- IAM groups: Collection of IAM users
- Roles: Temporary identities
  - Does NOT have credentials attached
  - (Advantage) Expire after a set period
  - Use case 1: EC2 talking with S3
  - Use case 2: Cross Account Access
- Policies: Define permissions 
  - AWS managed - Standalone policy predefined by AWS
  - Customer managed - Standalone policy created by you
  - Inline - Directly embedded into a user, group, or role

#### How does IAM work in Google Cloud?

IAM in AWS is very different from Google Cloud.

My recommendation: Forget AWS IAM & Start FRESH! Example: Role in AWS is NOT the same as Role in Google Cloud.

Let's take an example: I want to provide access to manage a specific cloud storage bucket to a colleague of mine. Here are some of the important terminology to remember:

In Google Cloud IAM:
- Member: My colleague
- Resource: Specific cloud storage bucket
- Action: Upload/Delete Objects
- Roles: A set of permissions (to perform specific actions on specific resources). Roles do NOT know about members. It is all about permissions!
- Policy: Assign permissions to a member by binding a role to a member

To implement the permissions needed by our example, we need to take two simple steps: 
- 1: Choose a Role with the right permissions (Ex: Storage Object Admin)
- 2: Create a Policy binding member (your friend) with the role (permissions)

#### Few more differences: IAM in GCP vs AWS

Here are a few more important differences:

- IAM in Google Cloud is only responsible for Authorization. It does not manage user identity.
- IAM role is the programmatic identity in AWS. For example, if I want an EC2 instance to be able to talk to an S3 bucket, I will create an IAM role with the right permission and assign it to the EC2 instance. In Google Cloud, Service Account is the programmatic identity.

| Question | AWS  | Google Cloud | 
|--|:--|:--|
|Can IAM manage User Identity?|Yes|No|
|How can a VM talk with a Cloud Service (Programmatic Identities)? |IAM role|IAM service account|
|How can you track usage of IAM Identities?|AWS CloudTrail|Audit logging|


#### AWS IAM Policy Example

In AWS, a Policy is a set of permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*", //["s3:Get*","s3:List*"],
            "Resource": "*" //"arn:aws:s3:::mybucket/somefolder/*"
        }
    ]
}
```
- Policy is a JSON document with one or more permissions
  - Effect - Allow or Deny
  - Resource - Which resource are you providing access to?
  - Action - What actions are allowed on the resource?
  - Condition - Are there any restrictions on IP address ranges or time intervals?
  - Example above: AWS Managed Policy: AdministratorAccess
  - Give Read Only Access to S3 buckets - `"Action": ["s3:Get*","s3:List*"]`

#### Google Cloud IAM policy - Example

In Google Cloud, Policy is a list of bindings - Each binding binds roles with members.


```
{
  "bindings": [
    {
      "role": "roles/storage.objectAdmin",
       "members": [
         "user:you@in28minutes.com",
         "serviceAccount:myAppName@appspot.gserviceaccount.com",
         "group:administrators@in28minutes.com",
         "domain:google.com"
       ]
    },
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:you@in28minutes.com"
      ],
      "condition": {
        "title": "Limited time access",
        "description": "Only upto Feb 2022",
        "expression": "request.time < timestamp('2022-02-01T00:00:00.000Z')",
      }
    }
  ]
}
```

### 6: Networking 

Let's now dig deeper into Networking concepts.

#### Networking in AWS - Amazon VPC and Subnets

A VPC(Virtual Private Cloud) in AWS is your own isolated network in the AWS cloud. Network traffic within a VPC is isolated (not visible) from all other Amazon VPCs. You control all the traffic coming in and going outside a VPC.

A Subnet separates public resources from private resources in a VPC. 

#### Networking in Google Cloud - VPC and Subnets

VPC and Subnets in Google Cloud are very similar to AWS:
- Default VPCs are provided with default subnets
- You can create your own custom VPCs and subnets
- You can create different types of resources in different subnets
- You can use VPC flow logs to debug problems
- You can set up peering between VPCs to connect different VPCs
- You can create Shared VPCs to share resources across multiple Google Cloud projects or AWS accounts

However, it is important to note the differences:
- In AWS, VPCs are regional and Subnets belong to an Availability Zone
  - However, in Google Cloud VPCs are global and Subnets belong to a specific region
- There are significant differences in default VPCs and subnets configuration
  - In Google Cloud, default VPCs are created per project
    - Each default VPC has multiple subnets - one in each region


### 7: Organizing Resources

Typically, every enterprise creates thousands of resources in the cloud. Google Cloud and AWS take very different approaches to group and manage resources.

#### Organizing Resources in AWS

Resources in AWS are created in an AWS account. By default, you will be billed per AWS Account.

If you want to create resources for multiple environments, one of the recommended approaches is to create separate AWS accounts:
- Each AWS account provides natural security, access, and billing boundaries
- Create AWS Organization to organize accounts into Organizational Units (OU)
  - A consolidated bill for AWS accounts
- Use AWS Resource Access Manager to share AWS resources:
  - Share AWS Transit Gateways, Subnets, AWS License Manager configurations, etc

#### Organizing Resources in Google Cloud

Google Cloud has a very well defined hierarchy (Organization > Folder > Project > Resources) to help you organize your resources.

Here are some of the important things to remember:
- Resources are created in projects
- A Folder can contain multiple projects
- Organization can contain multiple Folders

Here is the recommended approach for managing resources in Google Cloud:
- Create separate projects for different environments. This ensures complete isolation between test and production environments.
- Create separate folders for each department. This will isolate production applications of one department from another. In case you need to share resources, you can create shared folders.
- Recommendation: One project per application per environment:

Let's consider two apps: "A1" and "A2" with two environments each: "DEV" and "PROD". In the ideal world you will create four projects: A1-DEV, A1-PROD, A2-DEV, and A2-PROD:
- Isolates environments from each other
- DEV changes will NOT break PROD
- Grant all developers complete access (create, delete, deploy) to DEV Projects
- Provide production access to operations teams only!

### 8: What's Next?

The next obvious step is to broaden your horizon. I would recommend you to get started here - [https://cloud.google.com/free/docs/aws-azure-gcp-service-comparison](https://cloud.google.com/free/docs/aws-azure-gcp-service-comparison)

A visit to [Cloud Architecture Center](https://cloud.google.com/architecture) can help you discover reference architectures for your workloads on Google Cloud.

