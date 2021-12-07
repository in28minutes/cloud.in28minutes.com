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

&emsp; &emsp; &emsp; &emsp; ![arrowtd](https://user-images.githubusercontent.com/57451228/144975149-f5a53302-74f2-43d7-9e24-eeebde5861fc.png)

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

![Screenshot 2021-12-07 at 11 34 13 AM](https://user-images.githubusercontent.com/57451228/144976367-3c9954aa-7e64-4a30-82f7-48cd951be70b.png)


![Screenshot 2021-12-07 at 11 35 16 AM](https://user-images.githubusercontent.com/57451228/144975581-f20fd4a5-ddee-4d35-80dd-076b477a18cf.png)

<BR/>

## Updating a Managed Instance Group (MIG)

- **Rolling update -** Gradual update of instances in an instance group to the new instance template
  - Specify new template:
     - (OPTIONAL) Specify a template for canary testing
  - Specify how you want the update to be done:
     - When should the update happen?
        - Start the update immediately (Proactive) or when instance group is resized later(Opportunistic)
     - How should the update happen?
        - **Maximum surge:** How many instances are added at any point in time?
        - **Maximum unavailable:** How many instances can be offline during the update?
- **Rolling Restart/replace**: Gradual restart or replace of all instances in the group
  - No change in template BUT replace/restart existing VMs
  - Configure Maximum surge, Maximum unavailable and What you want to do? (Restart/Replace)

<BR/>

![Screenshot 2021-12-07 at 11 38 38 AM](https://user-images.githubusercontent.com/57451228/144975880-96c373c6-cbd7-407f-bb13-cb44b974ab74.png)

![Screenshot 2021-12-07 at 11 38 51 AM](https://user-images.githubusercontent.com/57451228/144975891-722f7b49-a04f-4a6a-9d95-787d40ce349a.png)

<BR/>

## Playing with Managed Instance Groups - Command Line

![shell](https://user-images.githubusercontent.com/57451228/144976044-c6ca1c46-e4ec-4fd2-b14c-2616db79cd10.png)


### Gcloud compute instance-groups managed
- **Create instance group:** create
     - gcloud compute instance-groups managed **create** my-mig --zone us-central1-a --template my-instance-template --size 1
        - --health-check=HEALTH_CHECK: How do you decide if an instance is healthy?
        - --initial-delay: How much time should you give to an instance to start?
     - **Other similar commands** - gcloud compute instance-groups managed **delete/describe/list**
- **Setup Autoscaling:** set-autoscaling/stop-autoscaling
     - gcloud compute instance-groups managed **set-autoscaling my-mig --max-num-replicas=10**
        - --cool-down-period (default - 60s): How much time should Auto Scaler wait after initiating an autoscaling action?
        - --scale-based-on-cpu --target-cpu-utilization --scale-based-on-load-balancing --target-load-balancing-utilization
        - --min-num-replicas --mode (off/on(default)/only-scale-out)
     - gcloud compute instance-groups managed **stop-autoscaling my-mig**
- **Update existing MIG policies** (ex: auto healing policies):
     - gcloud compute instance-groups managed **update** my-mig
        - --initial-delay: How much time should you give to the instance to start before marking it as unhealthy?
        - --health-check: How do you decide if an instance is healthy?

## Managed Instance Group - Command Line - Making Updates

- **Resize the group:**
  - gcloud compute instance-groups managed **resize** my-mig -**-size=5**
- **Recreate one or more instances** (delete and recreate instances):
  - gcloud compute instance-groups managed **recreate-instances** my-mig **--instances=my-instance-1,my-instance-2**
- **Update specific instances:**
  - gcloud compute instance-groups managed **update-instances** my-mig --instances=my-instance-3,my-instance-4 (Update specific instances from the group)
     - **--minimal-action**=none(default)/refresh/replace/restart
     - **--most-disruptive-allowed-action**=none(default)/refresh/replace/restart
- **Update instance template:**
  - gcloud compute instance-groups managed **set-instance-template my-mig --template=v2-template**
     - After updating instance template, you can trigger roll out of the new template using update-instances, recreate-instances or rolling-action start-update commands


## Instance Group Scenarios

|Scenario	|Solution|
|:--:|--|
|You want MIG managed application to survive Zonal Failures	|Create multiple zone MIG (or regional MIG)|
|You want to create VMs of different configurations in the same group	|Create Un-managed Instance Group|
|You want to preserve VM state in an MIG	|Stateful MIG - Preserve VM state (Instance name, attached Persistent disks and Metadata). Recommended for stateful workloads (database, data processing apps)|
|You want high availability in an MIG even when there are hardware/software updates	| Use an instance template with availability policy <BR/> automatic restart: enabled & on-host maintenance: migrate <BR/> Ensures live migration and automatic restarts |
|You want unhealthy instances to be automatically replaced	|Configure health check on the MIG (self healing)|
|Avoid frequent scale up & downs	|Cool-down period/Initial delay|

<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
