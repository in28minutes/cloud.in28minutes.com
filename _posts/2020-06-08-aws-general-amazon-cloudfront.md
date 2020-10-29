---
layout:     post
title:      Amazon CloudFront - Signed URLs, Cookies and OAI - AWS Certification Cheat Sheet
date:       2020-06-06 12:31:19
summary:    Let's get a quick overview of Amazon CloudFront from an AWS certification perspective. We will look at important certification questions regarding Amazon CloudFront. How do you distribute private content from Amazon S3 using Amazon CloudFront ?
categories:  AWS_CLOUD AWS_SERVICES
permalink:  /aws-certification-amazon-cloudfront-signed-urls-cookies-oai-s3
---

Let's get a quick overview of Amazon CloudFront from an AWS certification perspective. We will look at important certification questions regarding Amazon CloudFront. How do you distribute private content from Amazon S3 using Amazon CloudFront ?

## You will learn
- What is Amazon CloudFront?
- Why do we need Amazon CloudFront?
- When do we use Amazon CloudFront?
- How do you distribute private content from Amazon S3 using Amazon CloudFront ?
- What are Signed URLs and Cookies?
- What are Origin Access Identities(OAI)?

## AWS Certification Study Material and Notes - 25 PDF Cheat Sheets

Each cheat sheet contains:
- FAQs and Tutorials with 5-20 slides
- Study Material and Notes to quickly review and prepare for certification exam
- Certification Exam Tips
- Certification and Interview Scenario Questions

<div>
 <a href="https://links.in28minutes.com/cloud-in28minutes-teachable-free-link" target="_blank" class="button instagram">Download</a>
</div>


## Amazon CloudFront

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment. 

Here are some of the important features:
- Serve users from nearest edge location (based on user location)
- Source content can be from S3, EC2, ELB and External Websites
- If content is not available at the edge location, it is retrieved from the origin server and cached
- No minimum usage commitment
- Provides features to protect your private content

Important Use Cases for Amazon CloudFront include:
- Static web apps. Audio, video and software downloads. Dynamic web apps
- Support media streaming with HTTP and RTMP

Amazon CloudFront Integrates with 
- AWS Shield to protect from DDoS attacks
- AWS Web Application Firewall (WAF) to protect from SQL injection, cross-site scripting, etc


Here are the Cost Benefits for Amazon CloudFront:
- Zero cost for data transfer between S3 and CloudFront
- Reduce compute workload for your EC2 instances

## Amazon CloudFront Distribution

To distribute content using CloudFront you need to create a CloudFront Distribution.

Here are some of the important configuration options:
- DNS domain name - example abc.cloudfront.com
- Origins - Where do you get content from? S3, EC2, ELB, External Website
- Cache-Control
	- By default objects expire after 24 hours
	- Customize min, max, default TTL in CloudFront distribution
	- (For file level customization) Use Cache-Control max-age and Expires headers in origin server

![](/images/aws/001-basic-drawings/cloudfrontdistribution.png)

You can configure CloudFront to only use HTTPS (or) use HTTPS for certain objects
- Default is to support both HTTP and HTTPS
- You can configure CloudFront to redirect HTTP to HTTPS



## Amazon CloudFront - Cache Behaviors

Cache Behaviors help you to configure different CloudFront behavior for different URL path patterns from same origin.

You need to configure:
- Path pattern(can use wild cards - `*.php, *.jsp`), 
- Do you want to forward query strings?
- Should we use https?
- TTL

## Amazon CloudFront - Private content - Securing & Restricting Access

Options to secure content include:
- Signed URLs
- Signed cookies using key pairs
- Origin Access Identities(OAI) 
	- Ensures that only CloudFront can access S3
	- Allow access to S3 only to a special CloudFront user

### Amazon CloudFront - Signed URLs and Cookies

![](/images/aws/04-content-delivery/04-SignedUrl.png)

Signed URLS are used for:
- RTMP distribution
- Application downloads (individual files) and 
- Situations where cookies are not supported

Signed Cookies are used when you have multiple files (You have a subscriber website). Signed Cookies do not need any change in application URLs

### Amazon CloudFront - Origin Access Identities(OAI)
Origin Access Identities(OAI) allow Only CloudFront to access content in S3.

Here are the steps in creating OAI:
- 1: Create a Special CloudFront user - Origin Access Identities(OAI)
- 2: Associate OAI with CloudFront distribution
- 3: Create a S3 Bucket Policy allowing access to OAI

Here is the bucket policy configuration:

```
{
    "Version": "2012-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": 
                "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity YOUR_IDENTIFIER"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mybucket/*"
        }
    ]
}
```

## Amazon CloudFront - Remember

Here are a few important things to remember:
- Old content automatically expires from CloudFront
- Invalidation API - remove object from cache
	- REMEMBER : Designed for use in emergencies
- Best Practice - Use versioning in object path name 
	- Example : /images/profile.png?version=1
	- Prevents the need to invalidated content
- Do not use CloudFront for
	- all requests from single location
	- all requests from corporate VPN
- Scenario: Restrict content to users in certain countries
	- Enable CloudFront Geo restriction
	- Configure White list(countries to be allowed) and Blacklist(countries to be blocked)
