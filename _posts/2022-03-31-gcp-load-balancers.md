---
layout:     post
title:      GCP Load Balancers - GCP Certification Cheat Sheet
date:       2022-03-31 00:00:00
summary:    Let's get a quick overview of Google Cloud Load Balancers
categories:  GCP_CLOUD General
permalink:  /gcp-certification-google-cloud-load-balancers
---

Let's get a quick overview of Google Cloud Load Balancers from an GCP certification perspective. We will look at important certification questions regarding different type of load balancers, when to use which load balancers etc.

## You will learn
- What are different type of Google Cloud Load Balancers
- Why it is important and how to set it up?
- Commands Cheatsheet

## GCP Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>

<!-- .slide: class="center" -->
# Cloud Load Balancing
---
## Cloud Load Balancing
<!-- .slide: class="image-right image-thirty" -->
![](./gcpimages/02-architecture/load-balancing.png)

- Distributes user traffic across instances of an application in single region or multiple regions
	- **Fully distributed, software defined** managed service
	- Important Features:
		- Health check - Route to healthy instances
			- Recover from failures
		- Auto Scaling
		- Global load balancing with single anycast IP
			- Also supports internal load balancing
- Enables: 
	- High Availability
	- Auto Scaling
	- Resiliency

---
## HTTP vs HTTPS vs TCP vs TLS vs UDP
<!-- .slide: class="image-right image-forty" -->
![](./gcpimages/application-transport-layers.png)
- Computers use protocols to communicate
- Multiple layers and multiple protocols
- **Network Layer** - Transfer bits and bytes
- **Transport Layer** - Are the bits and bytes transferred properly?
- **Application Layer** - Make REST API calls and Send Emails
- (Remember) Each layer makes use of the layers beneath it
- (Remember) Most applications talk at application layer. BUT some applications talk at transport layer directly(high performance).

---
<!-- .slide: class="image-right image-forty ninety" -->
## HTTP vs HTTPS vs TCP vs TLS vs UDP
![](./gcpimages/application-transport-layers.png)
- Network Layer:
	- IP (Internet Protocol): Transfer bytes. Unreliable.
- Transport Layer:
	- TCP (Transmission Control): Reliability > Performance
	- TLS (Transport Layer Security): Secure TCP
	- UDP (User Datagram Protocol): Performance > Reliability
- Application Layer:
	- HTTP(Hypertext Transfer Protocol): Stateless Request Response Cycle
	- HTTPS: Secure HTTP
	- SMTP: Email Transfer Protocol
	- and a lot of others...

---
<!-- .slide: class="image-right image-forty ninety" -->
## HTTP vs HTTPS vs TCP vs TLS vs UDP
![](./gcpimages/application-transport-layers.png)
- **Most applications** typically communicate at application layer
	- Web apps/REST API(HTTP/HTTPS), Email Servers(SMTP), File Transfers(FTP)
	- All these applications use TCP/TLS at network layer(for reliability)
- **HOWEVER** applications needing high performance **directly** communicate at transport layer:
	- Gaming applications and live video streaming use UDP (sacrifice reliability for performance)
- **Objective**: Understand Big Picture. Its OK if you do not understand all details.

---
## Cloud Load Balancing - Terminology
![](./gcpimages/00-icons/gcp/user-card.png)
![](./gcpimages/arrow-card.png)
![](./gcpimages/00-icons/gcp/load-balancing-card.png)
![](./gcpimages/arrow-card.png)
![](./gcpimages/00-icons/gcp/compute-instances-card.png)

- **Backend** - Group of endpoints that receive traffic from a Google Cloud load balancer (example:  instance groups)
- **Frontend** - Specify an IP address, port and protocol. This IP address is the frontend IP for your clients requests. 
	- For SSL, a certificate must also be assigned.
- **Host and path rules** (For HTTP(S) Load Balancing) - Define rules redirecting the traffic to different backends:
	- Based on **path** - in28minutes.com/a vs in28minutes.com/b
	- Based on **Host** - a.in28minutes.com vs b.in28minutes.com
	- Based on **HTTP headers** (Authorization header) and methods (POST, GET, etc)
	- etc..

---
## Load Balancing - SSL/TLS Termination/Offloading

![](./gcpimages/00-icons/gcp/user-card.png)
![](./gcpimages/arrow-card.png)
![](./gcpimages/00-icons/gcp/load-balancing-card.png)
![](./gcpimages/arrow-card.png)
![](./gcpimages/00-icons/gcp/compute-instances-card.png)

- Client to Load Balancer: Over internet
	- HTTPS recommended
- Load Balancer to VM instance: Through Google internal network
	- HTTP is ok. HTTPS is preferred.
- SSL/TLS Termination/Offloading
	- Client to Load Balancer: HTTPS/TLS
	- Load Balancer to VM instance: HTTP/TCP

---
## Cloud Load Balancing - Choosing Load Balancer
https://cloud.google.com/load-balancing/gcpimages/choose-lb.svg
![](./gcpimages/gcp/choosing-lb.png)

---
## Cloud Load Balancing - Features

| Load Balancer| Type of Traffic | Proxy or pass-through|Destination Ports|
|--|--|--|
|External HTTP(S)|Global, External, HTTP or HTTPS| Proxy|HTTP on 80 or 8080<BR/> HTTPS on 443|
|Internal HTTP(S)|Regional, Internal, HTTP or HTTPS| Proxy|HTTP on 80 or 8080<BR/>HTTPS on 443|
| SSL Proxy  | Global, External, TCP with SSL offload | Proxy|A big list|
|TCP Proxy|Global, External, TCP without SSL offload|Proxy|A big list|
|External Network TCP/UDP|Regional, External, TCP or UDP|Pass-through|any|
|Internal TCP/UDP|Regional, Internal, TCP or UDP|Pass-through|any|

---
## Load Balancer Scenarios
<!-- .slide: class="tdfragment" -->
| Scenario |Solution  |
|:--|:--|
|You want only healthy instances to receive traffic| Configure health check|
|You want high availability for your VM instances| Create Multiple MIGs for your VM instances in multiple regions. Load balance using a Load Balancer.|
|You want to route requests to multiple microservices using the same load balancer| Create individual MIGs and backends for each microservice. <BR/> Create Host and path rules to redirect to specific microservice backend based on the path (/microservice-a, /microservice-b etc). You can route to a backend Cloud Storage bucket as well.|
|You want to load balance Global external HTTPS traffic across backend instances, across multiple regions|Choose External HTTP(S) Load Balancer|
|You want SSL termination for Global non-HTTPS traffic with load balancing|Choose SSL Proxy Load Balancer|
