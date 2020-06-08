---
layout:     post
title:      Amazon CloudWatch - Logs, Events, Alarms and Dashboards - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon CloudWatch - Logs, Events, Alarms and Dashboards. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-amazon-cloudwatch-logs-events-alarms-and-dashboards
---

Let's get a quick overview of Amazon CloudWatch - Logs, Events, Alarms and Dashboards. 

## You will learn
- What is Amazon CloudWatch?
- What are the different Amazon CloudWatch Components - Logs, Events, Alarms and Dashboards?
- When do we use Amazon CloudWatch?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


## Monitoring AWS with Amazon CloudWatch

![](/images/aws/00-icons/cloudwatch.png) 
- Monitoring and observability service
- Collects monitoring and operational data in the form of logs, metrics, and events
- Set alarms, visualize logs, take automated actions and troubleshoot issues
- Integrates with more than 70 AWS services:
	- Amazon EC2
	- Amazon DynamoDB
	- Amazon S3
	- Amazon ECS
	- AWS Lambda
	- and ....

## Amazon CloudWatch Logs

![](/images/aws/00-icons/cloudwatch.png) 
- Monitor and troubleshoot using system, application and custom log files
- Real time application and system monitoring
	- Monitor for patterns in your logs and trigger alerts based on them
	- Example : Errors in a specific interval exceed a certain threshold
- Long term log retention
	- Store logs in CloudWatch Logs for as long as you want (configurable - default:forever)
	- Or archive logs to S3 bucket (Typically involves a delay of 12 hours)
	- Or stream real time to Amazon Elasticsearch Service (Amazon ES) cluster using CloudWatch Logs subscription

## Amazon CloudWatch Logs
- **CloudWatch Logs Agent** 
	- Installed on ec2 instances to move logs from servers to CloudWatch logs
- **CloudWatch Logs Insights** 
	- Write queries and get actionable insights from your logs
- **CloudWatch Container Insights** 
	- Monitor, troubleshoot, and set alarms for your containerized applications running in EKS, ECS and Fargate

## Amazon CloudWatch Alarms
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

- Create alarms based on: 
	- Amazon EC2 instance CPU utilization
	- Amazon SQS queue length
	- Amazon DynamoDB table throughput or 
	- Your own custom metrics

## Amazon CloudWatch Alarms
![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

- Take immediate action: 
	- Send a SNS event notification
		- Send an email using SNS
	- Execute an Auto Scaling policy

## Amazon CloudWatch Alarm - Example
- You set a CPU Utilization alarm on EC2 instance with a threshold of 80% over 3 periods of 10 minutes. If CPU utilization is 90% for 20 minutes, does the alarm get triggered?
	- No

## Amazon CloudWatch Dashboards
![](/images/aws/cloudwatch-ec2.png) 
- Create auto refreshed graphs around all CloudWatch metrics
- Automatic Dashboards are available for most AWS services and resources
- Each Dashboard can have graphs from multiple regions

## Amazon CloudWatch Events

![](/images/aws/00-icons/cloudwatch.png) 
- Enable you to take immediate action based on events on AWS resources
	- Call a AWS Lambda function when an EC2 instance starts
	- Send event to an Amazon Kinesis stream when an Amazon EBS volume is created
	- Notify an Amazon SNS topic when an Auto Scaling event happens
- Schedule events - Use Unix cron syntax
	- Schedule a call to Lambda function every hour
	- Send a notification to Amazon SNS topic every 3 hours
