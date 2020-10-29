---
layout:     post
title:      ALB Auto Scaling Groups and Dynamic Scaling Policies - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Auto Scaling Groups and Dynamic Scaling Policies from an AWS certification perspective. We will look at important certification questions regarding Auto Scaling Groups and Dynamic Scaling Policies. 
categories:  AWS_CLOUD ELB
permalink:  /aws-certification-auto-scaling-group-dynamic-scaling-policy
---

Let's get a quick overview of Auto Scaling Groups and Dynamic Scaling Policies from an AWS certification perspective. We will look at important certification questions regarding Auto Scaling Groups and Dynamic Scaling Policies.

## You will learn
- What is Auto Scaling Group in an Elastic Load Balancer?
- Why do we need Dynamic Scaling?
- What are the different Dynamic Scaling Policies available?
- What are the Certification and Interview Questions for Auto Scaling Groups and Dynamic Scaling Policies ?
- What role does CloudWatch play in Auto Scaling Groups and Dynamic Scaling Policies?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Introducing ALB Auto Scaling Groups
Target Groups are configured with a static set of instances. How do you scale out and scale in **automatically**?
- Configure a Auto Scaling Group

![](/images/aws/ec2/4-elb-target-groups.png)

## ALB Auto Scaling Groups
Here are some of the important Auto Scaling Group responsibilities:
- **Maintain** configured number of instances (using periodic health checks)
	- If an instance goes down, ASG launches replacement instance
- **Auto scale** to adjust to load (scale-in and scale-out based on auto scaling policies)

![](/images/aws/ec2/5-elb-autoscaling-groups_new.png)

Important things to note:
- ASG can launch On-Demand Instances, Spot Instances, or both 
	- **Best Practice**: Use Launch Template
- An ELB can distribute load to **active instances** as ASG expands and contracts based on the load

## Auto Scaling Components

![](/images/aws/ec2/5-elb-autoscaling-groups_new.png)

Important Auto Scaling Components include:
- **Launch Configuration/Template**
	- EC2 instance size and AMI
- **Auto Scaling Group**
	- Reference to Launch Configuration/Template
	- Min, max and desired size of ASG
	- EC2 health checks by default. Optionally enable ELB health checks.
	- **Auto Scaling Policies**
		- When and How to execute scaling?

## Auto Scaling Group - Use Cases

![](/images/aws/asg.png) 

| ASG Use case | Description  | More details | 
|--|--|--|
| Maintain current instance levels at all times   |  min = max = desired = CONSTANT<BR/> When an instance becomes unhealthy, it is replaced.     |   Constant load |
| Scale manually    |   Change desired capacity as needed   |  You need complete control over scaling  |
| Scale based on a schedule |  Schedule a date and time for scaling up and down. | Batch programs with regular schedules|
| Scale based on demand (Dynamic/Automatic Scaling) | Create scaling policy (what to monitor?) and scaling action (what action?) | Unpredictable load |

## Dynamic Scaling Policy Types

![](/images/aws/asg.png) 

| Scaling Policy | Example(s)  | Description | 
|--|--|--|
| Target tracking scaling   |  Maintain CPU Utilization at 70%.|  Modify current capacity based on a target value for a specific metric.    |
|  Simple scaling   | +5 if CPU utilization > 80% <BR/> -3 if CPU utilization < 60%| Waits for cooldown period before triggering additional actions. | 
|  Step scaling   | +1 if CPU utilization between 70% and 80%<BR/> +3 if CPU utilization between 80% and 100%<BR/> Similar settings for scale down| Warm up time can be configured for each instance| 

## Scaling Policies - Background

![](/images/aws/00-icons/cloudwatchalarm.png)
![](/images/arrow.png)
![](/images/aws/00-icons/autoscaling.png)
![](/images/arrow.png)
![](/images/aws/00-icons/ec2instances.png)

- Two parts:
	- CloudWatch alarm (Is CPU utilization >80%? or < 60%). 
	- Scaling action (+5 EC2 instances or -3 EC2 instances)

## Quick Review

##### Concepts
- **Auto Scaling Group** - Maintain configured number of instances (using periodic health checks). Auto scale to adjust to load.
- **Dynamic Scaling Policies** - Target tracking scaling, Simple scaling and Step scaling.
- **CloudWatch alarms** track the metric (Is CPU utilization >80%? or < 60%) and trigger the auto scaling action (+5 EC2 instances or -3 EC2 instances)

## Auto Scaling - Certification and Interview Questions
| Scenario | Solution | 
|--|--|
|Change instance type or size of ASG instances|Launch configuration or Launch template cannot be edited. Create a new version and ensure that the ASG is using the new version. Terminate instances in small groups.|
|Roll out a new security patch (new AMI) to ASG instances| Same as above.|
| Perform actions before an instance is added or removed| Create a Lifecycle Hook. You can configure CloudWatch to trigger actions based on it. |
|Which instance in an ASG is terminated first when a scale-in happens?| (**Default Termination Policy**) Within constraints, goal is to distribute instances evenly across available AZs. Next priority is to terminate older instances.|
| Preventing frequent scale up and down | Adjust cooldown period to suit your need (default - 300 seconds). Align CloudWatch monitoring interval |
| I would want to protect newly launched instances from scale-in|Enable instance scale-in protection|