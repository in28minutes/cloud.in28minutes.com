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

Why do we need Google Cloud Deployment Manager?
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

## Google Cloud Deployment Manager

- All configuration is defined in a simple text file - YAML
   - I want a VPC, a subnet, a database and ...
- Deployment Manager understands dependencies
   - Creates VPCs first, then subnets and then the database
- (Default) Automatic rollbacks on errors (Easier to retry)
If creation of database fails, it would automatic delete the subnet and VPC
- Version control your configuration file and make changes to it over time
- Free to use - Pay only for the resources provisioned
   - Get an automated estimate for your configuration

## Cloud Deployment Manager - Example

```sh
- type: compute.v1.instance
  name: my-first-vm
  properties:
    zone: us-central1-a
    machineType: <<MACHINE_TYPE>>
    disks:
    - deviceName: boot
      type: PERSISTENT
      boot: true
      autoDelete: true
      initializeParams:
        sourceImage: <<SOURCE_IMAGE>>
    networkInterfaces:
    - network: <<NETWORK>>
      # Give instance a public IP Address
      accessConfigs:
      - name: External NAT
        type: ONE_TO_ONE_NAT
```
## Cloud Deployment Manager - Image

![Screenshot 2021-12-06 at 12 04 08 PM](https://user-images.githubusercontent.com/57451228/144798844-0e627368-2f52-4ed5-a71c-04e554282603.png)



## Cloud Deployment Manager - Terminology
- **Configuration file:** YAML file with resource definitions for a single deployment
- **Templates:** Reusable resource definitions that can be used in multiple configuration files
   - Can be defined using:
       - Python (preferred) OR
       - JinJa2 (recommended only for very simple scripts)
- **Deployment:** Collection of resources that are deployed and managed together
- **Manifests:** Read-only object containing original deployment configuration (including imported templates)
  - Generated by Deployment Manager
  - Includes fully-expanded resource list
  - Helpful for troubleshooting


<BR/>


<pre>
Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>
<br/>
Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>