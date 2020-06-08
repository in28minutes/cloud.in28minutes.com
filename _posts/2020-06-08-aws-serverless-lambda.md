---
layout:     post
title:      AWS Lambda - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of AWS Lambda from an AWS certification perspective. We will look at important certification questions regarding AWS Lambda. 
categories:  AWS_CLOUD AWS_SERVERLESS
permalink:  /aws-certification-aws-lambda
---

Let's get a quick overview of AWS Lambda from an AWS certification perspective. We will look at important certification questions regarding AWS Lambda.

## You will learn
- What is AWS Lambda?
- What is serverless?
- Why do we need AWS Lambda?
- When do we use AWS Lambda?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}



## Serverless
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/lambdafunction.png) 
![](/images/aws/00-icons/apigateway.png) 
- What are the things we think about when we develop an application?
	- Where do we deploy the application?
	- What kind of server? What OS?
	- How do we take care of scaling the application?
	- How do we ensure that it is always available?
- **What if we do not need to worry about servers and focus on building our application?**
- Enter **Serverless**

## Serverless
- Remember: **Serverless does NOT mean "No Servers"**
- **Serverless for me**:
	- You don't worry about infrastructure
	- Flexible scaling
	- Automated high availability
	- Pay for use:
		- You don't have to provision servers or capacity!
- **You focus on code** and the cloud managed service takes care of all that is needed to scale your code to serve millions of requests!

## AWS Lambda
![](/images/aws/00-icons/lambda.png) 
![](/images/aws/00-icons/lambdafunction.png) 
- World before Lambda - ELB with EC2 Servers!
- You don't worry about servers or scaling or availability
- You only worry about your code
- You pay for what you use 
	- Number of requests
	- Duration of requests
	- Memory consumed

## AWS Lambda - Supported Languages
- Java
- Go 
- PowerShell
- Node.js
- C# 
- Python, 
- Ruby
- and a lot more...

## AWS Lambda Event Sources
- Amazon API Gateway
- AWS Cognito
- Amazon DynamoDB (event)
- Amazon CloudFront (Lambda@Edge)
- AWS Step Functions 
- Amazon Kinesis (event)
- Amazon Simple Storage Service
- Amazon Simple Queue Service (event)
- Amazon Simple Notification Service
- The list is endless...


## AWS Lambda Function
- Stateless - store data to Amazon S3 or Amazon DynamoDB
- 500MB of non-persistent disk space (/tmp directory)
- Allocate memory in 64MB increments from 128MB to 3GB
	- Lambda cost increases with memory
	- CPU Power increases with memory allocated
	- Inexpensive - https://aws.amazon.com/lambda/pricing/
		- Free tier - 1M free requests per month
- Monitor function executions through Amazon CloudWatch
- Maximum allowed time for lambda execution is 900 seconds (default - 3 seconds)
- Integrates with AWS X-Ray(tracing), AWS CloudWatch (monitoring and logs)


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