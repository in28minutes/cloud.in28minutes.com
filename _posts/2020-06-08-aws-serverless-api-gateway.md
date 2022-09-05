---
layout:     post
title:      Amazon API Gateway - API Management - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon API Gateway from an AWS certification perspective. We will look at important certification questions regarding Amazon API Gateway. 
categories:  AWS_CLOUD AWS_SERVERLESS
permalink:  /aws-certification-amazon-api-gateway
---

Let's get a quick overview of Amazon API Gateway from an AWS certification perspective. We will look at important certification questions regarding Amazon API Gateway.

## You will learn
- What is Amazon API Gateway?
- What are the typical problems in building an API?
- Why do we need Amazon API Gateway?
- When do we use Amazon API Gateway?
- How do you implement authentication and authorization for Amazon API Gateway?



## REST API Challenges

Most applications today are built around REST API.

Management of REST API is not easy:
- You've to take care of authentication and authorization
- You've to be able to set limits (rate limiting, quotas) for your API consumers
- You've to take care of implementing multiple versions of your API
- You would want to monitor your API calls
- You would want to be able to cache API requests

## Amazon API Gateway

How about a **fully managed service** with auto scaling that can act as a **"front door"** to your APIs? Welcome **"Amazon API Gateway"**

Amazon API Gateway helps you to **"publish, maintain, monitor, and secure APIs at any scale"**

You can authorize users by integrating with:
- AWS IAM (for AWS users using signature version 4)
- Amazon Cognito
- Lambda authorizer (custom authorization with JWT tokens or SAML)


## Amazon API Gateway Features

Here are some of the important features:
- Integrates with AWS Lambda, Amazon EC2, Amazon ECS or any web application
- Supports HTTP(S) and WebSockets (two way communication - chat apps and streaming dashboards)
- Serverless. **Pay for use** (API calls and connection duration)
- Provides API Lifecycle Management for RESTful APIs and WebSocket APIs
- You can Run multiple versions of the same API
- Supports Rate Limits(request quota limits), throttling and fine-grained access permissions using API Keys for Third-Party Developers
- Lifecycle management for REST APIs 
- Versioning and multiple environments
- API keys - Generate API keys to monitor usage
	- Implement plans and quota limits for external applications (or developer)
	- WARNING - Do NOT use API keys for Authorization
- Enable caching for API calls with TTL
- Protect backends by throttling requests
- Integrates with 
	- Amazon CloudWatch - Performance metrics, API calls, latency data and error rates
	- Amazon CloudWatch Logs - Debug logging
	- AWS CloudTrail - Complete history of changes to your REST API

## Amazon API Gateway - Authentication and Authorization & Approaches

How can you implement Authentication with API Gateway?

![](/images/aws/03-serverless/04-Request-With-SecurityToken.png)

How do you authenticate a REST API call?
- Attach a signature or token with your API call


Here are some of the important options:
- AWS Signature Version 4
	- Create a signature using your AWS secret access key and send it with your API request
	- For API consumers belonging to your AWS account
- Lambda authorizers
	- Implement a Lambda function to authenticate (JWT, OAuth etc) the token and return IAM policies. 
	- Integrate with any custom user directory
- Amazon Cognito
