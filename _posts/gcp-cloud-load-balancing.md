---
layout:     post
title:      Cloud Load Balancing in Google Cloud Platform - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Cloud Load Balancing in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Cloud Load Balancing in Google Cloud Platform.
categories:  GCP_General GCP_Computing_Services
permalink:  /gcp-cloud-load-balancing
---
Let's get a quick overview of Cloud Load Balancing in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Cloud Load Balancing in Google Cloud Platform.


## You will learn

- Cloud Load Balancing
- HTTP vs HTTPS vs TCP vs TLS vs UDP
- Cloud Load Balancing - Terminology
- Load Balancing - SSL/TLS Termination/Offloading
- Cloud Load Balancing - Choosing Load Balancer
- Cloud Load Balancing - Features
- Load Balancer Scenarios - QNA

## Cloud Load Balancing

![load-balancing](https://user-images.githubusercontent.com/57451228/148980521-b5ec760a-2ed3-459c-b0cd-f1861082cacb.png)


- Distributes user traffic across instances of an application in single region or multiple regions
  - Fully **distributed, software defined** managed service
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



## HTTP vs HTTPS vs TCP vs TLS vs UDP



![application-transport-layers](https://user-images.githubusercontent.com/57451228/148980583-80434eb9-18ed-4268-b320-d6d86a3bdf4c.png)


- Computers use protocols to communicate
- Multiple layers and multiple protocols
- **Network Layer** - Transfer bits and bytes
- **Transport Layer** - Are the bits and bytes transferred properly?
- **Application Layer** - Make REST API calls and Send Emails
- (Remember) Each layer makes use of the layers beneath it
- (Remember) Most applications talk at application layer. BUT some applications talk at transport layer directly(high performance).

## HTTP vs HTTPS vs TCP vs TLS vs UDP

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

## HTTP vs HTTPS vs TCP vs TLS vs UDP

- **Most applications** typically communicate at application layer
  - Web apps/REST API(HTTP/HTTPS), Email Servers(SMTP), File Transfers(FTP)
  - All these applications use TCP/TLS at network layer(for reliability)
- **HOWEVER** applications needing high performance **directly** communicate at transport layer:
  - Gaming applications and live video streaming use UDP (sacrifice reliability for performance)
- **Objective**: Understand Big Picture. Its OK if you do not understand all details.


## Cloud Load Balancing - Terminology
    
![user-card](https://user-images.githubusercontent.com/57451228/148980808-5aaf1b3f-5bf4-408c-b1d1-e326084302a8.png) &emsp; &emsp; ![arrow-card](https://user-images.githubusercontent.com/57451228/148980817-6a26a606-036e-46b0-ac67-ff63dbd613b0.png) &emsp; &emsp; ![load-balancing-card](https://user-images.githubusercontent.com/57451228/148980835-cecfe577-d53e-4ab6-b7df-0a9c7cbc3764.png) &emsp; &emsp; ![arrow-card-1](https://user-images.githubusercontent.com/57451228/148980845-21c2f344-ce40-4a09-98c1-7fc417ccf693.png) &emsp; &emsp; ![compute-instances-card](https://user-images.githubusercontent.com/57451228/148980858-6739b08e-bb31-4a0e-9d0d-b3eaf4a542ff.png)


- **Backend** - Group of endpoints that receive traffic from a Google Cloud load balancer (example: instance groups)
- **Frontend** - Specify an IP address, port and protocol. This IP address is the frontend IP for your clients requests.
  - For SSL, a certificate must also be assigned.
- **Host and path rules** (For HTTP(S) Load Balancing) - Define rules redirecting the traffic to different backends:
  - Based on **path** - in28minutes.com/a vs in28minutes.com/b
  - Based on **Host** - a.in28minutes.com vs b.in28minutes.com
  - Based on **HTTP headers** (Authorization header) and methods (POST, GET, etc)
  - etc..



## Load Balancing - SSL/TLS Termination/Offloading
    

- Client to Load Balancer: Over internet
  - HTTPS recommended
- Load Balancer to VM instance: Through Google internal network
  - HTTP is ok. HTTPS is preferred.
- SSL/TLS Termination/Offloading
  - Client to Load Balancer: HTTPS/TLS
  - Load Balancer to VM instance: HTTP/TCP

## Cloud Load Balancing - Choosing Load Balancer

![choosing-lb](https://user-images.githubusercontent.com/57451228/148980993-1cce6fcb-d5c1-4b6f-9c24-e5b21b0610ad.png)





## Cloud Load Balancing - Features

|Load Balancer	|Type of Traffic	|Proxy or pass-through	|Destination Ports|
|:--:|--|:--:|--|
|External HTTP(S)	|Global, External, HTTP or HTTPS	|Proxy	|HTTP on 80 or 8080 HTTPS on 443|
|Internal HTTP(S)	|Regional, Internal, HTTP or HTTPS	|Proxy	|HTTP on 80 or 8080 HTTPS on 443|
|SSL Proxy	|Global, External, TCP with SSL offload |	Proxy	|A big list|
|TCP Proxy	|Global, External, TCP without SSL offload	|Proxy	|A big list|
|External Network TCP/UDP	|Regional, External, TCP or UDP	|Pass-through	|any|
|Internal TCP/UDP	|Regional, Internal, TCP or UDP|	Pass-through	|any|


## Load Balancer Scenarios

|Scenario	|Solution|
|:--:|--|
|You want only healthy instances to receive traffic	|Configure health check|
|You want high availability for your VM instances	|Create Multiple MIGs for your VM instances in multiple regions. Load balance using a Load Balancer.|
|You want to route requests to multiple microservices using the same load balancer	|Create individual MIGs and backends for each microservice. Create Host and path rules to redirect to specific microservice backend based on the path (/microservice-a, /microservice-b etc). You can route to a backend Cloud Storage bucket as well. |
|You want to load balance Global external HTTPS traffic across backend instances, across multiple regions	|Choose External HTTP(S) Load Balancer|
|You want SSL termination for Global non-HTTPS traffic with load balancing	|Choose SSL Proxy Load Balancer|



<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
