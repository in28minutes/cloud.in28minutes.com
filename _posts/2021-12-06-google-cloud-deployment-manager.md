---
layout:     post
title:      Google Cloud Deployment Manager - GCP Certification Cheat Sheet
date:       2021-12-06 11:13:00
summary:    Let's get a quick overview of Google Cloud Deployment Manager from an GCP certification perspective. We will look at important certification questions regarding Google Cloud Deployment Manager.
categories:  GCP_General GCP_Other_Services
permalink:  /google-cloud-deployment-manager
---

Let's get a quick overview of Google Cloud Deployment Manager from an GCP certification perspective. We will look at important certification questions regarding Google Cloud Deployment Manager.

## You will learn
- What is Google Cloud Deployment Manager?
- Advantages of Google Cloud Deployment Manager?
- Terminology of Google Cloud Deployment Manager?

## Google Cloud Deployment Manager - Need

Why do we need Regions and Zones?
Let's first understand that with a simple scenario.

### Lets consider an example:
- I would want to create a new VPC and a subnet
- I want to provision a Load balancer, Instance groups with 5 Compute Engine instances and an Cloud SQL database in the subnet
- I would want to setup the right Firewall

### AND I would want to create 4 environments
- Dev, QA, Stage and Production!

**Deployment Manager can help you do all these with a simple (actually NOT so simple) script!**

![deployment-manager](https://user-images.githubusercontent.com/57451228/144797309-997c2ae7-8f89-40ae-9818-a78702b4dffc.png)

## Google Cloud Deployment Manager - Advantages

- Automate deployment and modification of Google Cloud resources in a controlled, predictable way
   - Deploy in multiple environments easily!
- Avoid configuration drift
- Avoid mistakes with manual configuration
- Think of it as version control for your environments
- **Important Note** - Always modify the resources created by Deployment Manager using Deployment Manager

<BR/>


<pre>
Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>
<br/>
Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
