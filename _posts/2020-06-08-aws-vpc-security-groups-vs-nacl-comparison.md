---
layout:     post
title:      Security Groups vs NACL - A Comparison - AWS Certification Cheat Sheet
date:       2020-09-12 12:31:19
summary:    Let's compare Security Groups vs NACL from an AWS certification perspective. We will look at important certification questions regarding Security Groups and NACL. 
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-security-groups-vs-nacl-comparison
---

Let's compare Security Groups vs NACL from an AWS certification perspective. We will look at important certification questions regarding Security Groups and NACL.

## You will learn
- What is Security Groups 
- What is NACL?
- What is difference between Security Groups and NACL?
- When do you use Security Groups?
- When do you use NACL?



## EC2 Security Groups

![](./images/aws/00-icons/user.png)
![](./images/arrowbi.png)
![](./images/aws/00-icons/securitygroup.png)
![](./images/arrowbi.png)
![](./images/aws/00-icons/ec2instance.png)

An EC2 Security Groups is **Virtual firewall** to control **incoming and outgoing** traffic to/from AWS resources (EC2 instances, databases etc). It Provides additional layer of security - Defense in Depth

How are Security Groups Rules evaluated?

Let's consider the example below:

![](./images/aws/security-group-example.png)

Here are few important things to remember:
- Security groups are **default deny**. If there are no rules configured, no outbound/inbound traffic is allowed.
- You can specify **allow rules ONLY**
- You can configure **separate rules** for inbound and outbound traffic.

You can assign multiple (upto five) security groups to your EC2 instances. 

You can add and delete security groups to EC2 instances at any time. Changes are immediately effective.

Traffic NOT explicitly allowed by Security Group **will not reach** the EC2 instance.

Security Groups are **stateful**:
- If an outgoing request is allowed, the incoming response for it is automatically allowed. 
- If an incoming request is allowed, an outgoing response for it is automatically allowed

## EC2 Security Group - Trivia

What if there are no security group rules configured for inbound and outbound?
- Default DENY. No traffic is allowed in and out of EC2 instance.

Can I change security groups at runtime?
- Yes. Changes are immediately effective.

## Quick Review of Security Groups - Default Security Group

| Direction | Protocol | Port Range | Source/Destination   |
|--|:--:|--:|--|
| Inbound   |    All   |        All | Security Group ID (sg-xyz) |
| Outbound  |    All   |        All | 0.0.0.0/0            |

**Default security group** is created when you create a VPC. A default security group:
- Allows all outbound traffic
- Allows communication between resources assigned with the default security group
- Denies all other inbound traffic (other than resources with the default security group)
- Can be edited but not be deleted

EC2 instances, by default, are assigned the default security group of the VPC. However, you can change it at any point - during launch or later.

Security Group has a **many to many relationship** with Resources (in same VPC).

## New Security Groups

| Direction | Protocol | Port Range | Source/Destination   |
|--|:--:|--:|--|
| Outbound  |    All   |        All | 0.0.0.0/0            |

You can create **new security groups**. By default:
- There are no inbound rules 
- Denies all inbound traffic
- Allows all outbound traffic

You can add, edit and delete outbound and inbound rules.

## Security Groups - Important Ports
 
| Service |Port  | 
|--|--|
| SSH (Linux instances)  | 22  |
| RDP (Remote Desktop - Windows)  | 3389  |
| HTTP   | 80  |
| HTTPS   | 443  |
| PostgreSQL   | 5432  |
| Oracle   | 1521  |
| MySQL/Aurora   | 3306  |
| MSSQL   | 1433  |

## Security Group Scenario Questions
 
| Scenario | Solution  |
|--|--|
| Can source/destination of a security group be another security group?| Yes. It can even be same security group.| 
|A new security group is created and assigned to a database and an ec2 instance. Can these instances talk to each other?| No. New security group does not allow any incoming traffic from same security group. <BR/>Two resources associated with same security group can talk with each other only if you configure rules allowing the traffic.|
|The default security group (unchanged) in the VPC is assigned to a database and an ec2 instance. Can these instances talk to each other?|Yes. Default security group (by default) has a rule allowing traffic between resources with same security group.|

## Network Access Control List
![](/images/aws/00-icons/nacl.png)
 
Security groups control traffic to a specific resource in a subnet. How about stopping traffic from **even entering the subnet**?

NACL provides **stateless firewall** at subnet level. 

Each subnet **must** be associated with a NACL.

**Default NACL** allows all inbound and outbound traffic. **Custom created NACL** denies all inbound and outbound traffic by default.

NACL Rules have a priority number.  Lower number => Higher priority.

## Security Group vs NACL

|Feature | Security Group                                     |NACL                                                                      |
|--|--|--|
|Level | Assigned to a specific instance(s)/resource(s)     | Configured for a subnet. Applies to traffic to all instances in a subnet. |
|Rules | Allow rules only                                   | Both allow and deny rules                                                 |
|State | Stateful. Return traffic is automatically allowed. | Stateless. You should explicitly allow return traffic.                    |
|Evaluation | Traffic allowed if there is a matching rule        | Rules are prioritized. Matching rule with highest priority wins.          |

## Scenario: EC2 instance cannot be accessed from internet 

How do you debug this? An EC2 instance cannot be accessed from internet.

![](/images/aws/00-icons/nacl.png)
![](/images/aws/00-icons/subnet.png)
![](/images/aws/00-icons/securitygroup.png)
![](/images/aws/00-icons/ec2.png)
![](/images/aws/00-icons/elasticip.png)

Here are the things to check:
- Does the EC2 instance have a public IP address or an Elastic IP address assigned?
- Check the network access control list (ACL) for the subnet. Is inbound and outbound traffic allowed from your IP address to the port?
- Check the route table for the subnet. Is there a route to the internet gateway? 
- Check your security group rules. Are you allowing inbound traffic from your IP address to the port?
