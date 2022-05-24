---
layout:     post
title:      HTTP vs HTTPS vs TCP vs TLS vs UDP - Protocol Comparison - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's compare - HTTP vs HTTPS vs TCP vs TLS vs UDP 
categories:  AWS_CLOUD General
permalink:  /http-vs-https-vs-tcp-vs-tls-vs-udp-aws-certification
---

Let's compare - HTTP vs HTTPS vs TCP vs TLS vs UDP. 

## You will learn
- Comparison of HTTP vs HTTPS vs TCP vs TLS vs UDP
- Why do we have multiple layers in the TCP/IP Stack?
- What is the role of Network Layer vs Transport Layer vs Application Layer?

## Get Multi Cloud Certified

<div>
	<p><a href="https://courses.in28minutes.com/p/3-in-1-aws-azure-and-google-cloud-beginner-certifications"><img src="/images/multi-cloud-certified.png" alt="Image" title="AWS Architect Associate Certification"></a></p>
</div>



## Understanding Need for Protocols and Layers

Computers use protocols to communicate. Different layers use different  protocols.

Let's first understand the roles of different layers involved in network communication between two systems:
- **Network Layer** - Transfer bits and bytes
- **Transport Layer** - Are the bits and bytes transferred properly?
- **Application Layer** - Make REST API calls and Send Emails



## Network Layer vs Transport Layer vs Application Layer

![](/images/application-transport-layers.png)

Let's now compare the three important layers:
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


**Most applications** typically communicate at application layer
- Web apps/REST API(HTTP/HTTPS), Email Servers(SMTP), File Transfers(FTP)
- All these applications use TCP/TLS at network layer(for reliability)

**HOWEVER** applications needing high performance **directly** communicate at transport layer:
- Gaming applications and live video streaming use UDP (sacrifice reliability for performance)

Here are a couple of important things to note:
- Each layer makes use of the layers beneath it.
- Most applications talk at application layer. BUT some applications talk at transport layer directly(high performance).
