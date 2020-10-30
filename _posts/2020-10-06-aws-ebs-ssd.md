---
layout:     post
title:      EBS SSD Storages - A Difference - AWS Certification
date:       2020-10-06 20:12:00
summary:    Let's compare the different EBS SSD Storage types
categories:  AWS_CLOUD AWS_STORAGE
permalink:  /aws-certification-ebs-ssd-storage-differences
---

# Understanding different EBS SSD Storages

Greetings from [in28minutes.com](https://courses.in28minutes.com/). 

***SSD (Solid-state drives)*** are those storages that are cost-effective and best for small I/O operations and can be used as a boot volume. It is suitable for -

 - Transactional workloads
 - Business-critical applications that require high throughput performance
 - Large database workloads such as MongoDB, MySQL, PostgreSQL, Oracle, etc.

In this read, we will take a good look at some of the differences between the *different types of EBS SSD storages*. Let's get started.

| Attribute | General purpose SSD (gp2) | Provisioned IOPS SSD (io1) |
|--|--|--|
| **Description** | This volume balances the price and workload | This volume is used for critical low-latency or high-throughput workload applications |
| **Size** | 1 GB to 16 TB | 4 GB to 16 GB |
| **Maximum IOPS/Volume** | 16000 | 64000 |
| **Maximum Throughput/Volume** | 250 MiB/s | 1000 MiB/s |
| **Use case** | *(1)* Low latency interactive apps *(2)* Development or Test environment *(3)* System boot volumes or Virtual desktops | *(1)* Business-critical applications that require high throughput *(2)* Large database workloads such as MongoDB, MySQL, PostgreSQL, Oracle, etc.  |
