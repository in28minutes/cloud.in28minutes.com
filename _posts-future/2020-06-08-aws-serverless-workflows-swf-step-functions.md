---
layout:     post
title:      Handling Workflows - SWF and Step Functions - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Handling Workflows in AWS using SWF and Step Functions. 
categories:  AWS_CLOUD AWS_SERVERLESS
permalink:  /aws-certification-handling-workflows-swf-and-step-functions
---

Let's get a quick overview of Handling Workflows in AWS using SWF and Step Functions. 

## You will learn
- What are the popular AWS options for Handling Workflows?
- What is Amazon Simple Workflow Service (SWF)?
- What are AWS Step Functions?
- Compare - AWS Step Functions vs Amazon Simple Workflow Service (SWF)

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


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