---
layout:     post
title:      AWS Serverless Use Cases - Compute, Storage and Databases - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of AWS Serverless Options - Compute, Storage and Databases.
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-aws-serverless-compute-storage-databases
---

Let's get a quick overview of AWS Serverless Options - Compute, Storage and Databases.

## You will learn
- What are the different AWS Serverless Options for Compute, Storage and Databases?
- What are the use cases for serverless in AWS?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

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

## Serverless Options - Databases
![](/images/aws/00-icons/dynamodb.png) 
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

## Serverless Use case 1 - Full Stack Web Application
![](/images/aws/03-serverless/01-serverless.png)
- Static content stored in S3
- API Gateway and Lambda are used for the REST API
- DynamoDB is used to store your data

## Serverless Use case 2 - Real time event processing

![](/images/aws/03-serverless/02-realtime-processing.png)
- User uploads videos to S3
- S3 notifications are used to invoke Lambda functions to optimize videos for different devices.