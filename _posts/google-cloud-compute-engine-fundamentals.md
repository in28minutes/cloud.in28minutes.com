---
layout:     post
title:      Google Cloud Compute Engine Fundamentals - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Compute Engine Fundamentals in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Compute Engine Fundamentals in Google Cloud Platform.
categories:  GCP_General GCP_Computing_Services
permalink:  /google-cloud-compute-engine-fundamentals
---
Let's get a quick overview of Compute Engine Fundamentals in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Compute Engine Fundamentals in Google Cloud Platform.


## You will learn

- Google Compute Engine (GCE)
- Compute Engine - Features
- Compute Engine Machine Family & Machine Types
- Image
- Compute Engine Hands-on : Setting up a HTTP server
- Internal and External IP Addresses
- Static IP Addresses
- Simplify VM HTTP server setup
- Instance templates
- Reducing Launch Time with Custom Image

## Google Compute Engine (GCE)

![compute-engine](https://user-images.githubusercontent.com/57451228/146007819-3d19ae5d-2ccf-4c5d-92c3-dd79525fb648.png)

- In corporate data centers, applications are deployed to physical servers
- Where do you deploy applications in the cloud?
   - Rent virtual servers
   - **Virtual Machines** - Virtual servers in GCP
   - **Google Compute Engine (GCE)** - Provision & Manage Virtual Machines

### Compute Engine - Features



![compute-engine-1](https://user-images.githubusercontent.com/57451228/146008143-1fc751d7-8b38-471d-89f6-6d696b42117b.png) ![persistent-disk](https://user-images.githubusercontent.com/57451228/146008163-dd005ccb-d8cb-42b1-b975-6055f6144173.png) ![load-balancing](https://user-images.githubusercontent.com/57451228/146008179-8179220b-bf74-4a29-87e1-90045a94200c.png)

- Create and manage lifecycle of Virtual Machine (VM) instances
- **Load balancing and auto scaling** for multiple VM instances
- **Attach storage** (& network storage) to your VM instances
- Manage **network connectivity and configuration** for your VM instances
- **Our Goal:**
   - Setup VM instances as HTTP (Web) Server
   - Distribute load with Load Balancers


## Compute Engine Machine Family

- What type of hardware do you want to run your workloads on?
- Different Machine Families for Different Workloads:
   - **General Purpose (E2, N2, N2D, N1) :** Best price-performance ratio
       - Web and application servers, Small-medium databases, Dev environments
   - **Memory Optimized (M2, M1):** Ultra high memory workloads
       - Large in-memory databases and In-memory analytics
   - **Compute Optimized (C2):** Compute intensive workloads
       - Gaming applications


## Compute Engine Machine Types

![machine-types](https://user-images.githubusercontent.com/57451228/146008734-31c3443a-ccb0-4479-90d0-0ce21244067f.png)


- How much CPU, memory or disk do you want?
   - Variety of machine types are available for each machine family
   - Let's take an example : e2-standard-2:
       - **e2 -** Machine Type Family
       - **standard -** Type of workload
       - **2 -** Number of CPUs
- Memory, disk and networking capabilities increase along with vCPUs


## Image

![image-card](https://user-images.githubusercontent.com/57451228/146009000-8f58bbf3-9d93-4cd3-9137-a4198e5e8b5f.png) ![arrow-card](https://user-images.githubusercontent.com/57451228/146009041-39360ae6-b823-4a24-a614-1e56a578f78b.png) ![compute-instances-card](https://user-images.githubusercontent.com/57451228/146009053-0e54df13-aa4a-4666-b619-27861282e361.png)

- What operating system and what software do you want on the instance?
- Type of Images:
   - **Public Images:** Provided & maintained by Google or Open source communities or third party vendors
   - **Custom Images:** Created by you for your projects

## Compute Engine Hands-on : Setting up a HTTP server
```sh
#! /bin/bash
sudo su
apt update 
apt -y install apache2
sudo service apache2 start
sudo update-rc.d apache2 enable
echo "Hello World" > /var/www/html/index.html
echo "Hello world from $(hostname) $(hostname -I)" > /var/www/html/index.html
```

- Commands:
  - sudo su - execute commands as a root user
  - apt update - Update package index - pull the latest changes from the APT repositories
  - apt -y install apache2 - Install apache 2 web server
  - sudo service apache2 start - Start apache 2 web server
  - echo "Hello World" > /var/www/html/index.html - Write to index.html
  - $(hostname) - Get host name
  - $(hostname -I) - Get host internal IP address


## Internal and External IP Addresses

- **External** (Public) IP addresses are **Internet addressable.**
- **Internal** (Private) IP addresses are **internal** to a corporate network
- You CANNOT have two resources with same public (External) IP address.
   - HOWEVER, two different corporate networks CAN have resources with same Internal (private) IP address
- All **VM instances** are assigned at least one Internal IP address
- Creation of External IP addresses can be enabled for VM instances
   - (Remember) When you stop an VM instance, External IP address is lost
- **DEMO:** VM instances - Internal and External IPs

## Static IP Addresses

- Scenario : How do you get a constant External IP address for a VM instance?
   - Quick and dirty way is to assign an Static IP Address to the VM!
- **DEMO:** Using Static IP Address with an VM instance

### Static IP Addresses - Remember

- Static IP **can be switched** to another VM instance in same project
- Static IP **remains attached** even if you stop the instance. You have to manually detach it.
- Remember : You are **billed** for an Static IP when **you are NOT using it** as well!
   - Make sure that you explicitly release an Static IP when you are not using it.

## Simplify VM HTTP server setup

- How do we **reduce the number of steps** in creating an VM instance and setting up a HTTP Server?
- Let's explore a few options:
   - **Startup script**
   - **Instance Template**
   - **Custom Image**

## Bootstrapping with Startup script

```sh
#!/bin/bash
apt update 
apt -y install apache2
echo "Hello world from $(hostname) $(hostname -I)" > /var/www/html/index.html
```

- **Bootstrapping:** Install OS patches or software when an VM instance is launched.
- In VM, you can configure **Startup script** to bootstrap
- **DEMO** - Using Startup script

## Instance templates

![compute-instance-card](https://user-images.githubusercontent.com/57451228/146011415-e47b7713-4303-4a72-8772-22f9e2d8f72a.png)

&emsp; &emsp; &emsp; &emsp; ![arrowtd](https://user-images.githubusercontent.com/57451228/146011427-967f8985-27d2-4535-a105-e751932c9838.png)
![instance-template-card](https://user-images.githubusercontent.com/57451228/146011437-acf8a26e-3a7f-4623-b2ed-a78a534e3306.png)


&emsp; &emsp; &emsp; &emsp; ![arrowtd](https://user-images.githubusercontent.com/57451228/146011445-a76b8e59-101a-4166-b64e-b0eda3e9ee68.png)

![compute-instances-card](https://user-images.githubusercontent.com/57451228/146011487-c5af68cb-ecb5-4654-9a71-0414379136e0.png)

- Why do you need to specify all the VM instance details (Image, instance type etc) **every time** you launch an instance?
  - How about creating a **Instance template?**
  - Define **machine type, image, labels, startup script** and other properties
- Used to create **VM instances and managed instance groups**
  - Provides a **convenient way** to create similar instances
- **CANNOT** be updated
  - To make a change, copy an existing template and modify it
- (Optional) Image family can be specified (example - debian-9):
  - Latest non-deprecated version of the family is used
- **DEMO** - Launch VM instances using Instance templates

## Reducing Launch Time with Custom Image
    
- Installing OS patches and software at launch of VM **instances increases boot up** time
- How about creating a custom image with OS patches and software **pre-installed?**
   - Can be created from an instance, a persistent disk, a snapshot, another image, or a file in Cloud Storage
   - Can be shared across projects
   - (Recommendation) Deprecate old images (& specify replacement image)
   - (Recommendation) **Hardening an Image** - Customize images to your corporate security standards
- **Prefer using Custom Image to Startup script**
- **DEMO :** Create a Custom Image and using it in an Instance Template


<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
