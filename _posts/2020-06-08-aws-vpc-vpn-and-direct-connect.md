---
layout:     post
title:      AWS VPN vs AWS Direct Connect vs Software VPN vs CloudHub - AWS Certification Cheat Sheet
date:       2020-09-21 00:31:19
summary:    Let's compare the options to connect AWS network with your corporate network -  AWS VPN vs AWS Direct Connect vs Software VPN vs AWS VPN CloudHub from an AWS certification perspective. 
categories:  AWS_CLOUD AWS_VPC
permalink:  /aws-certification-aws-vpn-vs-aws-direct-connect-vs-software-vpn-vs-cloudhub-
---

Let's compare the options to connect AWS network with your corporate network -  AWS VPN vs AWS Direct Connect vs Software VPN vs AWS VPN CloudHub from an AWS certification perspective. 

## You will learn
- What is AWS VPN?
- What is AWS Direct Connect?
- What is Software VPN?
- Comparison - AWS VPN vs AWS Direct Connect vs Software VPN vs AWS VPN CloudHub
- When do we use - AWS VPN vs AWS Direct Connect vs Software VPN vs CloudHub?

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

## AWS and On-Premises - Overview

![](/images/aws/Aws-Onpremises-01.png)

- AWS Managed VPN 
	- IPsec VPN tunnels from  VPC to customer network
- AWS Direct Connect (DX)
	- Private dedicated network connection from on-premises to AWS



## AWS Managed VPN

![](/images/aws/001-basic-drawings/sitetositevpn.png)

- IPsec VPN tunnels from  VPC to customer network
- Traffic over internet - encrypted using IPsec protocol
- VPN gateway to connect one VPC to customer network
- Customer gateway installed in customer network
	- You need a Internet-routable IP address of customer gateway

## AWS Direct Connect (DC)

![](/images/aws/00-icons/datacenter.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/directconnect.png)
![](/images/arrowbi.png)
![](/images/aws/00-icons/aws.png)	

- Private dedicated network connection from on-premises to AWS
- Advantages:
	- Private network 
	- Reduce your (ISP) bandwidth costs
	- Consistent Network performance because of private network
- Connection options:
	- Dedicated: Dedicated 1 Gbps or 10 Gbps network connections
	- Hosted: Shared 50Mbps to 10 Gbps network connections
- (REMEMBER) Establishing DC connection can take more than a month
- (REMEMBER) Establish a redundant DC for maximum reliability
- (REMEMBER) Direct Connect DOES NOT encrypt data (Private Connection ONLY)

## AWS Direct Connect Plus VPN

- IPsec Site-to-Site VPN tunnel from an direct connect location to customer network
- Traffic is encrypted using IPsec protocol

## Software VPN

- Provides flexibility to fully manage both sides of your Amazon VPC connectivity
- Run software VPN appliance in your VPC
- Recommended for compliance - You need to manage both sides of connection
- Recommended when you use gateway devices which are not supported by Amazon VPN solution
- You are responsible for patches and updates to Software VPN appliance
- Software VPN appliance becomes a Single Point of Failure 

## AWS VPN CloudHub

- Use either VPN or AWS Direct Connect to setup connectivity between multiple branch offices
- Operates on a simple hub-and-spoke model 
- Uses Amazon VPC virtual private gateway with multiple gateways