---
layout:     post
title:      Elastic Beanstalk - EB - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Elastic Beanstalk from an AWS certification perspective. We will look at important certification questions regarding Elastic Beanstalk. 
categories:  AWS_CLOUD AWS_COMPUTE
permalink:  /aws-certification-elastic-beanstalk-eb
---

Let's get a quick overview of Elastic Beanstalk from an AWS certification perspective. We will look at important certification questions regarding Elastic Beanstalk.

## You will learn
- What is AWS Elastic Beanstalk?
- Why do we need AWS Elastic Beanstalk?
- When do you use AWS Elastic Beanstalk?

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>

## AWS Elastic BeanStalk

AWS Elastic BeanStalk is the **Simplest way** to deploy and scale your web application in AWS. It provides end-to-end web application management.

AWS Elastic BeanStalk Supports Java, .NET, Node.js, PHP, Ruby, Python, Go, and Docker applications

AWS Elastic BeanStalk has **No usage charges** - Pay only for AWS resources you provision.

AWS Elastic BeanStalk **Features** include:
- Automatic load balancing 
- Auto scaling
- Managed platform updates 
- Application health monitoring

## AWS Elastic Beanstalk Concepts

Let's look at some of the important Elastic Beanstalk Concepts:

**Application** - A container for environments, versions and configuration

**Application Version** - A specific version of deployable code (stored in S3)

**Environment** - An application version deployed to AWS resources. You can have multiple environments running different application versions for the same application.

**Environment Tier**:
- For batch applications, use **worker tier**
- For web applications, use **web server tier**

## AWS Elastic BeanStalk - Remember

Here are a few important things that you would need to remember about AWS Elastic BeanStalk:
- You **retain full control** over AWS resources created
- **Ideal for simple web** applications
- **NOT ideal for microservices** architectures
- You can access server logs without logging into the server
- Logs can be stored in Amazon S3 or in CloudWatch Logs
- You can choose to **apply patches and platform updates** automatically
- Metrics are send to Amazon CloudWatch
- You can configure SNS notifications based on health
- Delete your environment!
