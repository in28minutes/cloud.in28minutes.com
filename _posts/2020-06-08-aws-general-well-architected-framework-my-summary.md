---
layout:     post
title:      AWS Well Architected Framework - My summary for AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of AWS Well Architected Framework. 
categories:  AWS_CLOUD General
permalink:  /aws-certification-aws-well-architected-framework-my-summary
---

Let's get a quick overview of AWS Well Architected Framework. 

## You will learn
- What is AWS Well Architected Framework?
- What are the important components of AWS Well Architected Framework?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## Well Architected Framework

![](/images/aws/00-icons/aws.png) 
- Helps cloud architects build application infrastructure which is:
	- Secure
	- High-performing
	- Resilient and
	- Efficient
- You can find the complete framework here - https://aws.amazon.com/architecture/well-architected/
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

- Avoid/Minimize effort and problems with
	- Provisioning servers
	- Deployment
	- Monitoring
	- Support

## Operational Excellence - Solutions and AWS services

 
![](/images/aws/00-icons/lambda.png)
![](/images/aws/00-icons/cloudformation.png)
![](/images/aws/00-icons/codepipeline.png) 

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
- Run systems at lowest cost

## Cost Optimization - Best Practices

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

![](/images/aws/00-icons/trustedadvisor.png) 
![](/images/aws/00-icons/cloudwatch.png) 
![](/images/aws/00-icons/cloudfront.png) 
- Right-Sizing : Analyze 5 large servers vs 10 small servers
	- Use CloudWatch (monitoring) and Trusted Advisor (recommendations) to right size your resources
- Email server vs Managed email service (charged per email)
- On-Demand vs Reserved vs Spot instances
- Avoid expensive software : MySQL vs Aurora vs Oracle
- Optimize data transfer costs using AWS Direct Connect and Amazon CloudFront

