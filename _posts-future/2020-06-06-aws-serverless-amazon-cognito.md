---
layout:     post
title:      Amazon Cognito - User Pools, Identity Pools - AWS Certification
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon Cognito from an AWS certification perspective. 
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-amazon-cognito-user-authentication-and-authorization
---

Let's get a quick overview of Amazon Cognito from an AWS certification perspective. 

## You will learn
- What is Amazon Cognito?
- Why do we need Amazon Cognito?
- How can you do authorization and authentication with Amazon Cognito?
- What are User Pools and Identity Pools?

## AWS Certification - Download 25 PDF Cheat Sheets and a Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

**Download Now** - [25 AWS Cheat Sheets and Free Course - Getting Started](https://links.in28minutes.com/cloud-in28minutes-teachable-free-link){:target=""_blank""}


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

