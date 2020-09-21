---
layout:     post
title:      AWS Security Groups and Network Access Control List - A Comparison - AWS Certification
date:       2020-09-21 16:14:00
summary:    Let us understand the differences between security groups and network access control list in aws.
categories:  AWS_CLOUD AWS_SECURITY_GROUPS_VS_NETWORK_ACCESS_CONTROL_LIST
permalink:  /aws-security-groups-vs-network-access-control-list
---

# Difference between Security Groups (SG) and Network Access Control List (NACL)

Greetings from [in28minutes.com](https://courses.in28minutes.com/). 

In this read, we will take a good look at some of the differences between *Security Groups (SG)* and *Network Access Control List (NACL)* in AWS. Let's get started.

| Security Groups (SG) | Network Access Control List (NACL)  | 
|--|--|
| Acts as a firewall for ec2 instances | Acts as a firewall for the associated subnets  |
| Controls both inbound and outbound traffic at instance | Controls both inbound and outbound traffic at the subnet level  |
| Secures virtual private cloud instances using only security groups | Acts as an additional layer of defense |
| Supports allow rules only | Supports both allow and deny rules |
| Stateful in nature (i.e. return traffic automatically allowed regardless of any rules) | Stateless in nature (i.e. return traffic must be explicitly allowed by the rules)|
| Evaluates all rules before deciding whether to allow traffic | Evaluates rules in number order when deciding whether to allow traffic (starting with the lowest numbered rule)  |
| Applies only to the instance that is associated with it | Applies to all the instances in a subnet it is associated with |
| Can assign up to 5 security groups to an ec2 instance | A subnet can be associated with 1 NACL at a time|
| Security Groups are associated with the network interfaces | NACL is associated with multiple subnets |
| In default Security Group - the inbound rule is allowed for the same SG and the outbound rule is all allow | In default NACL - the inbound and outbound rule are all allowed |
| In custom Security Group - the inbound rule is denied and the outbound rule all allows | In custom NACL - the inbound and outbound rule is all denied |

Good luck and Happy learning! 

Feel free to share it with your friends/colleagues.
