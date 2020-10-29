---
layout:     post
title:      Amazon Cognito - User Pools, Identity Pools - AWS Certification Cheat Sheet
date:       2020-07-03 12:31:19
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

## AWS Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Amazon Cognito

Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0.

## Amazon Cognito - User Pools

User Pools help you create your own secure and scalable user directory.

It also helps you to create sign-up pages and customizable web UI to sign in users (with option to social sign-in ).

## Amazon Cognito - Identity pools

Identity pools provide AWS credentials to grant your users access to other AWS services.

You can connect identity pools with authentication (identity) providers:
- Your own user pool OR
- Amazon, Apple, Facebook, Google+, Twitter OR
- OpenID Connect provider OR
- SAML identity providers (SAML 2.0)

You can configure multiple authentication (identity) providers for each identity pool.

Federated Identity is an external authentication (identity) provider.
- ex: Amazon, Apple, Facebook, OpenID or SAML identity providers
	

## Amazon Cognito - How does it work?

Here are the important steps:
- 1: Application sends user credentials to identity provider
	- (If authenticated) Identity provider sends a token to application
- 2: Application sends the token to Identity Pool
	- (If valid token) Identity Pool creates temporary credentials (access key, secret key, and session token) using STS
- 3: App sends a request with the credentials to the AWS service

![](/images/aws/03-serverless/05-cognito.png)
