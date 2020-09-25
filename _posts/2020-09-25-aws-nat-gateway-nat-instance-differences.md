---
layout:     post
title:      NAT Gateway vs Instance - A Comparison - AWS Certification
date:       2020-09-25 22:15:00
summary:    Let's compare NAT Gateway and NAT Instance from an AWS certification perspective.
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-security-groups-vs-nacl-comparison
---

# Difference between NAT Gateway and NAT Instance

Greetings from [in28minutes.com](https://courses.in28minutes.com/). 

In this read, we will take a good look at some of the differences between *NAT Gateway* and *NAT Instance* in AWS. Let's get started.

| Attribute | NAT Gateway | NAT Instance |
|--|--|--|
| **Availability** | Highly available and is implemented in each availability zone with redundancy | Uses a script to manage the failover between instances |
|**Bandwidth** | Can scale up to 45 Gbps and can support up to 5500 simultaneous connections to each unique destination | Depends on the bandwidth of the instance type |
|**Maintainence** | Managed by AWS  | Managed by cloud user  |
| **Cost**| Charged depending on the number of NAT gateways, duration of usage, and the amount of data sent through the NAT gateway | Charged depending on the number of NAT instances that we use, duration of usage, and the instance type and size |
| **Type & Size**| Uniform offering | Choose a suitable instance type and size according to the predicted workload |
| **Public IP addresses**| Choose an Elastic IP (EIP) address to associate with a NAT gateway at the time of creation | Use an Elastic IP address or the public IP address with a NAT instance. We can change the public IP address at any time by associating a new elastic IP address with the instance |
| **Private IP addresses**| Automatically selected from the subnet's IP address range when we create the gateway | Assign a specific private IP address from the subnet IP address range when we launch an instance |
|**Security group (SG)** | Not associated with any security group | Associated with security group to control the inbound and outbound traffic |
| **Network access control list (NACL)** | Use the network ACL to control traffic to and from the subnet in which NAT gateway resides | Use the network ACL to control traffic to and from the subnet in which NAT instance resides |
| **Bastion servers** | Not supported | Supported  |
| **Traffic metrics**| Cloudwatch | Cloudwatch |

Good luck and Happy learning! 

Feel free to share it with your friends/colleagues.
