
# Routing and Content Delivery

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
