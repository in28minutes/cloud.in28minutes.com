---
layout:     post
title:      Google Cloud DNS - GCP Certification Cheat Sheet
date:       2021-12-06 11:13:00
summary:    Let's get a quick overview of Google Cloud DNS from an GCP certification perspective. We will look at important certification questions regarding Google Cloud DNS.
categories:  GCP_General GCP_Other_Services
permalink:  /google-cloud-dns-cli
---

Let's get a quick overview of Google Cloud DNS from an GCP certification perspective. We will look at important certification questions regarding Google Cloud DNS.

## You will learn        ![dns](https://user-images.githubusercontent.com/57451228/144802720-8d5f1ff8-db0d-44c5-a071-6753209b168b.png)
- What is Google Cloud DNS?
- Advantages of Google Cloud DNS?   
- What is Google Cloud DNS - CLI?   

## Google Cloud DNS - CLI - Need

### What would be the steps in setting up a website with a domain name (for example, in28minutes.com)?
- Step I : Buy the domain name in28minutes.com (Domain Registrar)
- Step II : Setup your website content (Website Hosting)
- Step III : Route requests to in28minutes.com to the my website host server (DNS)

## Cloud DNS = Global Domain Name System (Step III)

 - Setup your DNS routing for your website (in28minutes.com)
    - Route api.in28minutes.com to the IP address of api server
    - Route static.in28minutes.com to the IP address of http server
    - Route email (ranga@in28minutes.com) to the mail server(mail.in28minutes.com)
**Public and private managed DNS zones (container for records)**

## Cloud DNS - Images
<BR/>
![Screenshot 2021-12-06 at 12 29 47 PM](https://user-images.githubusercontent.com/57451228/144802315-cb848409-48f1-4301-ab5e-b0a307c5ec3c.png)
<BR/>
![Screenshot 2021-12-06 at 12 30 18 PM](https://user-images.githubusercontent.com/57451228/144802332-e23e47dc-b06b-4390-9163-3d20809a0beb.png)
<BR/>
## Cloud DNS - CLI

### gcloud dns managed-zones create ZONE_NAME
- --description (REQUIRED - Short description for the managed-zone)
- --dns-name (REQUIRED - DNS name suffix that will be managed with the created zone)
- --visibility (private/public)
- --networks (List of networks that the zone should be visible in if the zone visibility is [private])
 
### Three Steps to add records to a managed zone:
- Start Transaction for Zone
  - gcloud dns **record-sets transaction start** --zone
- Make Changes
  - gcloud dns **record-sets transaction add** --name=REC_NAME --ttl --type A/CNAME --zone=ZONE_NAME
- End Transaction for Zone
  - gcloud dns **record-sets transaction execute** --zone

<BR/>


<pre>
Author
- <a href="https://www.linkedin.com/in/rangakaranam/">Ranga Rao Karanam</a>
<br/>
Helping Hand
- <a href="https://www.linkedin.com/in/debrup-365/">Debrup ❤️</a>
</pre>
