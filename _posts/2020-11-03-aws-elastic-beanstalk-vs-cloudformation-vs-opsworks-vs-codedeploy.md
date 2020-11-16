---
layout:     post
title:      Elastic Beanstalk vs Cloudformation vs Opswork vs Codedeploy - A Difference - AWS Certification
date:       2020-11-03 18:45:00
summary:    Let's compare the different EBS HDD Storage types
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-elastic-beanstalk-cloud-formation-opswork-codedeploy-differences
---

# Difference between Elastic Beanstalk vs Cloudformation vs Opswork vs Codedeploy

Greetings from [in28minutes.com](https://courses.in28minutes.com/). In this read, we will take a good look at the different AWS services like Elastic Beanstalk, Cloudformation, Opswork, and Codedeploy. Let us get started.

| **Elastic Beanstalk** | **Cloudformation** | **Opswork** | **Codedeploy** |
|--|--|--|--|
| Elastic Beanstalk AWS service makes it easy for the developer to deploy hosted on AWS environment  | Cloud formation provides an easy way to create and manage the aws resources and provision them in a predictable fashion | It is a configuration management service that provides managed instances of Chef and Puppet | Coordinates the application deployment across ec2 instances |
| Elastic Beanstalk automatically handles the scaling, load-balancing, and application monitoring| It only deals with the application infrastructure and not the application itself | Offers three services i.e. Chef Automate, Puppet Enterprise, and OpsWorks Stacks | Does not scale automatically or handle the application monitoring |
| It is popularly called the ***platform as a service*** where you only focus on the application and code while the infrastructure is managed by AWS | Cloudformation support elastic beanstalk application environments i.e. creating and managing an aws elastic beanstalk hosted application along with rds to store the application related data | Focuses more on orchestration and software configuration and less on what and how AWS resources are procured | Does not handle infrastructure configuration or orchestration |
| Support deployment versioning where it maintains a copy of older deployments. Offer easiness to rollback to previous versions in case of current deployment failure | Supports rollback feature through template version controls while updating the stack but deployment failed midway |  |  |
