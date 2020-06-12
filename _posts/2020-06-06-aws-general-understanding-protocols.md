---
layout:     post
title:      HTTP vs HTTPS vs TCP vs TLS vs UDP - AWS Certification
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

## AWS Certification - 25 PDF Cheat Sheets + Free Course

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>



## Understanding Need for Protocols and Layers

Computers use protocols to communicate. Different layers use different  protocols.

Let's first understand the roles of different layers involved in network communication between two systems:
- **Network Layer** - Transfer bits and bytes
- **Transport Layer** - Are the bits and bytes transferred properly?
- **Application Layer** - Make REST API calls and Send Emails

Important things to note:
- Each layer makes use of the layers beneath it
- Most applications talk at application layer. BUT some applications talk at transport layer directly(high performance).

![](/images/application-transport-layers.png)


## Network Layer vs Transport Layer vs Application Layer

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
