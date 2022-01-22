---
layout:     post
title:      Google Cloud Networking : Hybrid Cloud - GCP Certification Cheat Sheet
date:       2021-12-07 10:13:00
summary:    Let's get a quick overview of Google Cloud Networking : Hybrid Cloud in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Google Cloud Networking : Hybrid Cloud in Google Cloud Platform.
categories:  GCP_General GCP_Network_Services
permalink:  /gcp-hybrid-cloud
---
Let's get a quick overview of Google Cloud Networking : Hybrid Cloud in Google Cloud Platform from an GCP certification perspective. We will look at important certification questions regarding Google Cloud Networking : Hybrid Cloud in Google Cloud Platform.


## You will learn

- Cloud VPN
- Cloud Interconnect
- Direct Peering

<BR/>


## Cloud VPN

![vpn](https://user-images.githubusercontent.com/57451228/150633266-4a4a672b-8d0b-46cc-9dd5-200b57c0a841.png)


- Cloud VPN - Connect on-premise network to the GCP network
  - Implemented using **IPSec VPN Tunnel**
  - Traffic through internet (public)
  - Traffic encrypted using **Internet Key Exchange** protocol
- Two types of Cloud VPN solutions:
  - HA VPN (SLA of 99.99% service availability with two external IP addresses)
     - Only dynamic routing (BGP) supported
  - Classic VPN (SLA of 99.9% service availability, a single external IP address)
     - Supports Static routing (policy-based, route-based) and dynamic routing using BGP



## Cloud Interconnect

![interconnect](https://user-images.githubusercontent.com/57451228/150633235-f18e0483-0a2d-4859-a7bf-c6b693baf5f1.png)


- High speed physical connection between on-premise and VPC networks:
  - Highly available and high throughput
  - Two types of connections possible
     - Dedicated Interconnect - 10 Gbps or 100 Gpbs configurations
     - Partner Interconnect - 50 Mbps to 10 Gbps configurations
- Data exchange happens through a private network:
  - Communicate using VPC network's internal IP addresses from on-premise network
  - Reduces egress costs
     - As public internet is NOT used
- (Feature) Supported Google API's and services can be privately accessed from on-premise
- Use only for high bandwidth needs:
  - For low bandwidth, Cloud VPN is recommended



## Direct Peering
- Connect customer network to google network using network peering
  - Direct path from on-premises network to Google services
- **Not a GCP Service**
  - Lower level network connection outside of GCP
- NOT RECOMMENDED:
  - Use Cloud Interconnect and Cloud VPN



<BR/>
<BR/>

<pre>
Thank You for Choosing to Learn from in28Minutes

Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>

Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
