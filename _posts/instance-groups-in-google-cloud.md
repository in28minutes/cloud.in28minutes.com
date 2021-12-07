---
layout:     post
title:      Instance Groups in Google Cloud Platform - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Instance Groups in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Instance Groups in Google Cloud Platform.
categories:  GCP_General GCP_Computing_Services
permalink:  /instance-groups-in-google-cloud
---
Let's get a quick overview of Instance Groups in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Instance Groups in Google Cloud Platform.


## You will learn

- Instance Groups
- Managed Instance Groups (MIG)
- Creating Managed Instance Group (MIG)
- Updating a Managed Instance Group (MIG)
- Playing with Managed Instance Groups - Command Line
- Managed Instance Group - Command Line - Making Updates
- Managed Instance Groups - Command Line - Rolling Actions
- Instance Groups - QNA

## Instance Groups


![load-balancing](https://user-images.githubusercontent.com/57451228/144972763-8b0fb7e4-1e83-40c9-a2cb-cd7bba1b580b.png)



- How do you create a group of VM instances?
  - **Instance Group** - Group of VM instances managed as a single entity
     - Manage group of similar VMs having similar lifecycle as ONE UNIT
- Two Types of Instance Groups:
  - **Managed :** Identical VMs created using a template:
     - Features: Auto scaling, auto healing and managed releases
  - **Unmanaged :** Different configuration for VMs in same group:
     - Does NOT offer auto scaling, auto healing & other services
     - NOT Recommended unless you need different kinds of VMs
- **Location** can be Zonal or Regional
  - Regional gives you higher availability (RECOMMENDED)

## Managed Instance Groups (MIG)

- **Managed Instance Group** - Identical VMs created using an **instance template**
- Important Features:
  - **Maintain** certain number of instances
     - If an instance crashes, MIG launches another instance
  - **Detect application failures** using health checks (Self Healing)
  - Increase and decrease instances based on load **(Auto Scaling)**
  - Add **Load Balancer** to distribute load
  - Create instances in multiple zones (regional MIGs)
     - Regional MIGs provide higher availability compared to zonal MIGs
  - **Release** new application versions without downtime
     - **Rolling updates**: Release new version step by step (gradually). Update a percentage of instances to the new version at a time.
     - **Canary Deployment:** Test new version with a group of instances before releasing it across all instances.

## Creating Managed Instance Group (MIG)

![mig-card](https://user-images.githubusercontent.com/57451228/144974449-71dcde2f-055a-4300-a505-95461fe194bd.png) 

&emsp; &emsp; &emsp; ![arrowtd](https://user-images.githubusercontent.com/57451228/144975149-f5a53302-74f2-43d7-9e24-eeebde5861fc.png)

![compute-instances-card](https://user-images.githubusercontent.com/57451228/144974474-f7fce25a-41c6-419d-8a1b-b4624115aa9c.png)


- **Instance template** is mandatory
- Configure **auto-scaling** to automatically adjust number of instances based on load:
  - **Minimum** number of instances
  - **Maximum** number of instances
  - **Autoscaling metrics:** CPU Utilization target or Load Balancer Utilization target or Any other metric from Stack Driver
     - **Cool-down period:** How long to wait before looking at auto scaling metrics again?
     - **Scale In Controls:** Prevent a sudden drop in no of VM instances
        - Example: Don't scale in by more than 10% or 3 instances in 5 minutes
  - **Autohealing:** Configure a Health check with Initial delay (How long should you wait for your app to initialize before running a health check?)


<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
