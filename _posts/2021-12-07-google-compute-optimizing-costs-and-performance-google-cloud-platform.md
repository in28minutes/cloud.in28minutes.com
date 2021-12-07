---
layout:     post
title:      Google Compute - Optimizing Costs and Performance in Google Cloud Platform - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Google Compute - Optimizing Costs and Performance in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Google Compute - Optimizing Costs and Performance in Google Cloud Platform.
categories:  GCP_General GCP_Computing_Services
permalink:  /google-compute-optimizing-costs-and-performance-google-cloud-platform
---
Let's get a quick overview of Google Compute - Optimizing Costs and Performance in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Google Compute - Optimizing Costs and Performance in Google Cloud Platform.


![compute-engine](https://user-images.githubusercontent.com/57451228/144966798-ba7976a2-8a3d-4bc9-ae7b-b28925d8983e.png)


## You will learn

- Sustained use Discounts
- Committed use Discounts
- Preemptible VM
- Google Compute Engine - Billing
- Compute Engine : Live Migration & Availability Policy
- Compute Engine Features: Custom Machine Types
- Compute Engine Features: GPUs
- Virtual Machine - Quick Review
- Virtual Machine - Best Practices
- Compute Engine - Quick QNA
- Quick Review 

##

Whenever we are making use of the cloud, you'd want to keep your costs as low as possible.
What are the things that you can do, to keep the, to keep the cost of your virtual machines low?

The first thing that we would be talking about is sustained use discounts. 

## Sustained use Discounts

![sustained-use-example](https://user-images.githubusercontent.com/57451228/144966514-ffac5688-c824-4401-8eb2-9dfad0052b7b.png)

- **Automatic discounts** for running VM instances for significant portion of the billing month
  - Example: If you use N1, N2 machine types for more than 25% of a month, you get a 20% to 50% discount on every incremental minute.
  - Discount increases with usage (graph)
  - No action required on your part!
- **Applicable** for instances created by **Google Kubernetes Engine and Compute Engine**
- **RESTRICTION:** Does NOT apply on certain machine types (example: E2 and A2)
- **RESTRICTION:** Does NOT apply to VMs created by App Engine flexible and Dataflow

Now, let's look at another type of discounts which are applied on your virtual machines.

## Committed use Discounts

- For workloads with **predictable resource** needs
- **Commit** for 1 year or 3 years
- **Up to 70% discount** based on machine type and GPUs
- **Applicable** for instances created by **Google Kubernetes Engine and Compute Engine**
- **RESTRICTION:** Does NOT apply to VMs created by App Engine flexible and Dataflow
<BR/>

![Screenshot 2021-12-07 at 10 04 34 AM](https://user-images.githubusercontent.com/57451228/144966979-264c071f-bfff-4a24-b5da-94cf734d3834.png)

<BR/>

## Saving Costs with Preemptible VM

- **Short-lived cheaper** (upto 80%) compute instances
  - Can be stopped by GCP any time (preempted) within 24 hours
  - Instances get 30 second warning (to save anything they want to save)
- **Use Preempt VM's** if:
  - Your applications are **fault tolerant**
  - You are very **cost sensitive**
  - Your workload is **NOT immediate**
  - Example: Non immediate batch processing jobs
- **RESTRICTIONS:**
  - NOT always available
  - NO SLA and CANNOT be migrated to regular VMs
  - NO Automatic Restarts
  - Free Tier credits not applicable

<BR/>

![Screenshot 2021-12-07 at 10 09 06 AM](https://user-images.githubusercontent.com/57451228/144967382-a96ee4cf-8a8a-458c-a852-9c87eaf0964e.png)

## Google Compute Engine - Billing

- You are **billed by the second** (after a minimum of 1 minute)
- You are NOT billed for compute when a compute instance is stopped
  - However, you will be billed for any storage attached with it!
- (RECOMMENDATION) **Always create Budget alerts** and make use of Budget exports to stay on top of billing!
- What are the ways you can save money?
  - Choose the right machine type and image for your workload
  - Be aware of the discounts available:
     - Sustained use discounts
     - Committed use discounts
     - Discounts for preemptible VM instances

<BR/>

![Screenshot 2021-12-07 at 10 14 54 AM](https://user-images.githubusercontent.com/57451228/144967903-ad1e79d0-b847-4238-99fd-969d36b0ab76.png)

<BR/>

## Compute Engine : Live Migration & Availability Policy

- How do you keep your VM instances running when a host system needs to be updated (a software or a hardware update needs to be performed)?
- **Live Migration**
  - Your running instance is migrated to another host in the same zone
  - Does NOT change any attributes or properties of the VM
  - SUPPORTED for instances with local SSDs
  - NOT SUPPORTED for GPUs and preemptible instances
- Important Configuration - **Availability Policy:**
  - **On host maintenance:** What should happen during periodic infrastructure maintenance?
     - Migrate (default): Migrate VM instance to other hardware
     - Terminate: Stop the VM instance
  - **Automatic restart** - Restart VM instances if they are terminated due to non-user-initiated reasons (maintenance event, hardware failure etc.)
<BR/>

![Screenshot 2021-12-07 at 10 20 21 AM](https://user-images.githubusercontent.com/57451228/144968438-7d57cdb6-5184-4054-9d1b-ea06cfa1981b.png)

<BR/>

## Compute Engine Features: Custom Machine Types

- What do you do **when predefined VM options are NOT appropriate** for your workload?
  - Create a machine type customized to your needs (a Custom Machine Type)
- **Custom Machine Type: Adjust** vCPUs, memory and GPUs
  - Choose between E2, N2, or N1 machine types
  - Supports a wide variety of Operating Systems: CentOS, CoreOS, Debian, Red Hat, Ubuntu, Windows etc
  - **Billed per vCPUs, memory provisioned** to each instance
     - Example Hourly Price: $0.033174 / vCPU + $0.004446 / GB

<BR/>

![Screenshot 2021-12-07 at 10 23 10 AM](https://user-images.githubusercontent.com/57451228/144968717-e7dd4f50-5f06-4b06-a2e8-e0536be58542.png)

<BR/>

## Compute Engine Features: GPUs

- How do you accelerate math intensive and graphics-intensive workloads for AI/ML etc?
- Add a **GPU** to your virtual machine:
  - High performance for math intensive and graphics-intensive workloads
  - Higher Cost
  - (REMEMBER) Use **images with GPU libraries** (Deep Learning) installed
     - OTHERWISE, GPU will not be used
  - **GPU restrictions:**
     - **NOT supported on all machine types** (For example, not supported on shared-core or memory-optimized machine types)
     - **On host maintenance** can only have the value "Terminate VM instance"
- Recommended **Availability policy** for GPUs
  - Automatic restart - on

<BR/>

![Screenshot 2021-12-07 at 10 31 28 AM](https://user-images.githubusercontent.com/57451228/144969677-8148e352-df88-44a2-b181-308ffd76787c.png)


<BR/>

![Screenshot 2021-12-07 at 10 33 06 AM](https://user-images.githubusercontent.com/57451228/144969614-419ad32b-e23a-4988-8b50-2c58e394c8ce.png)

<BR/>

## Virtual Machine - Remember

- Associated with a **project**
- Machine type **availability can vary** from region to regions
- You can only change the machine type (adjust the number of vCPUs and memory) of a stopped instance
  - You CANNOT change the machine type of a running instance
- VM's **can be filtered** by various properties
  - Name, Zone, Machine Type, Internal/External IP, Network, Labels etc
- Instances are Zonal (Run in a **specific zone** (in a specific region))
  - Images are global (You can provide access to other projects - if needed)
  - Instance templates are global (Unless you use zonal resources in your templates)
- **Automatic Basic Monitoring** is enabled
  - Default Metrics: CPU utilization, Network Bytes (in/out), Disk Throughput/IOPS
  - For Memory Utilization & Disk Space Utilization - Cloud Monitoring agent is needed


## Virtual Machine - Best Practices

- Choose **Zone and Region** based on:
  - Cost, Regulations, Availability Needs, Latency and Specific Hardware needs
  - Distribute instances in multiple zones and regions for high availability
- Choose **right machine type** for you needs:
  - Play with them to find out the right machine type
  - Use GPUs for Math and Graphic intensive applications
- Reserve for **"committed use discounts"** for constant workloads
- Use preemptible instances for fault-tolerant, NON time critical workloads
- Use **labels** to indicate environment, team, business unit etc

## Compute Engine Scenarios

|Scenario	|Solution|
|:--:|--|
|What are the pre-requisites to be able to create a VM instance?	|1. Project <BR/> 2. Billing Account <BR/> 3. Compute Engines APIs should be enabled |
|You want dedicated hardware for your compliance, licensing, and management needs	|Sole-tenant nodes|
|I have 1000s of VM and I want to automate OS patch management,OS inventory management and OS configuration management (manage software installed)	|Use "VM Manager"|
|You want to login to your VM instance to install software	|You can SSH into it|
|You do not want to expose a VM to internet	|Do NOT assign an external IP Address|
|You want to allow HTTP traffic to your VM	|Configure Firewall Rules|

## Quick Review

- **Image:**
  - What **operating system and what software** do you want on the VM instance?
  - Reduce boot time and improve security by creating custom **hardened Images.**
  - You can share an Image with other projects  
- **Machine Types:**
  - Optimized combination of compute(CPU, GPU), memory, disk (storage) and networking for specific workloads.
  - You can **create your own Custom Machine Types** when existing ones don't fit your needs  
- **Static IP Addresses:** Get a constant IP addresses for VM instances
- **Instance Templates:** Pre-configured templates simplifying the creation of VM instances
- **Sustained use discounts: Automatic discounts** for running VM instances for significant portion of the billing month
- **Committed use discounts:** 1 year or 3 year **reservations** for workloads with **predictable resource** needs
- **Preemptible VM:** Short-lived cheaper (upto 80%) compute instances for non-time-critical fault-tolerant workloads

<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
