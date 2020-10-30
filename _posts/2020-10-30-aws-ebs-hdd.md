---
layout:     post
title:      EBS HDD Storages - A Difference - AWS Certification
date:       2020-10-30 14:29:00
summary:    Let's compare the different EBS HDD Storage types
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-ebs-hdd-storage-differences
---

# Understanding different EBS HDD Storages

Greetings from [in28minutes.com](https://courses.in28minutes.com/). 

***HDD (Hard-disk drives)*** are those storages that are useful for large sequential input-output operations. It is suitable for -
 - Large streaming workloads which require fast throughput at a low price
 - Suitable for large volumes of data which is infrequently access

In this read, we will take a good look at some of the differences between the *different types of EBS HDSS storages*. Let's get started.

| Attribute | Throughput optmized HDD (st1) | Cold HDD (sc1) |
|--|--|--|
| **Description** | Useful for throughput intensive workloads which are frequently accessed | Useful for less frequently accessed |
| **Size** | 500 GB to 16 TB | 500 GB to 16 TB |
| **Maximum IOPS/Volume** | 500| 250 |
| **Maximum Throughput/Volume** | 500 MiB/s | 250 MiB/s |
