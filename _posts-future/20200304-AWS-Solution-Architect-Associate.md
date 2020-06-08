
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